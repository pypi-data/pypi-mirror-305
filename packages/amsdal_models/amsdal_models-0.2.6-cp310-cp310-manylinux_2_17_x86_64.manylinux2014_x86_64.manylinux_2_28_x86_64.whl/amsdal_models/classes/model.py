import contextlib
import json
import logging
from typing import Any
from typing import ClassVar
from typing import Literal

import typing_extensions
from amsdal_data.transactions.decorators import transaction
from amsdal_utils.errors import AmsdalError
from amsdal_utils.models.enums import SchemaTypes
from amsdal_utils.query.utils import Q
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PrivateAttr
from pydantic import model_validator
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.errors import PydanticUserError
from typing_extensions import Self
from typing_extensions import dataclass_transform

from amsdal_models.classes.base import BaseModel
from amsdal_models.classes.constants import REFERENCE_FIELD_SUFFIX
from amsdal_models.classes.errors import AmsdalRecursionError
from amsdal_models.classes.errors import AmsdalUniquenessError
from amsdal_models.classes.errors import ObjectAlreadyExistsError
from amsdal_models.classes.handlers.reference_handler import ReferenceHandler
from amsdal_models.classes.mixins.model_hooks_mixin import ModelHooksMixin
from amsdal_models.classes.utils import is_partial_model
from amsdal_models.managers.base_manager import BaseManager
from amsdal_models.querysets.executor import DEFAULT_DB_ALIAS
from amsdal_models.querysets.executor import LAKEHOUSE_DB_ALIAS

# should be `set[int] | set[str] | dict[int, IncEx] | dict[str, IncEx] | None`, but mypy can't cope
IncEx: typing_extensions.TypeAlias = 'set[int] | set[str] | dict[int, Any] | dict[str, Any] | None'

logger = logging.getLogger(__name__)


class TypeModel(
    ModelHooksMixin,
    ReferenceHandler,
    BaseModel,
):
    @model_validator(mode='before')
    @classmethod
    def convert_string_to_dict(cls, data: Any) -> Any:
        """
        Converts a string to a dictionary if possible.

        Args:
            data (Any): The data to convert.

        Returns:
            Any: The converted data.
        """
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                pass

        return data


@dataclass_transform(kw_only_default=True, field_specifiers=(Field,))
class AmsdalModelMetaclass(ModelMetaclass):
    def __new__(
        mcs,  # noqa: N804
        cls_name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        *args: Any,
        **kwargs: Any,
    ) -> type:
        cls = super().__new__(mcs, cls_name, bases, namespace, *args, **kwargs)

        if 'objects' in namespace:
            namespace['objects'].model = cls
        else:
            for base in bases:
                if hasattr(base, 'objects'):
                    cls.objects = base.objects.copy(cls=cls)  # type: ignore[attr-defined]
                    break

        return cls


class Model(TypeModel, metaclass=AmsdalModelMetaclass):
    """
    Base class for all model classes.

    Attributes:
        model_config (ConfigDict): Configuration for the model.
        objects (ClassVar[BaseManager[Self]]): Manager for the Model class.
    """

    _is_inside_save: bool = PrivateAttr(default=False)
    model_config = ConfigDict(validate_assignment=True)

    objects: ClassVar[BaseManager[Self]] = BaseManager()

    def __init__(self, **kwargs: Any) -> None:
        is_new_object = not kwargs.get('_object_id', None)

        self.pre_init(is_new_object=is_new_object, kwargs=kwargs)
        super().__init__(**kwargs)
        self.post_init(is_new_object=is_new_object, kwargs=kwargs)
        self._is_inside_save = False

    @transaction
    def save(self, *, force_insert: bool = False, using: str | None = None, skip_hooks: bool = False) -> Self:
        """
        Saves the record of the Model object into the database.

        By default, the object will be updated in the database if it already exists.
        If `force_insert` is set to True, the object will be inserted into the database even if it already exists,
        which may result in an `ObjectAlreadyExistsError`.

        The method first checks if `force_insert` is True, and if the object already exists in the database.
        If it does, it raises an `ObjectAlreadyExistsError`.

        Then, depending on the object existence, the method either creates a new record in the database or updates
        the existing record. It also triggers the corresponding `pre_create()`, `post_create()`, `pre_update()`, and
        `post_update()` hooks.

        Finally, the method returns the saved Model object.

        Args:
            force_insert (bool): Indicates whether to force insert the object into the database,
            even if it already exists.
            using (str | None): The name of the database to use.
            skip_hooks (bool): Indicates whether to skip the hooks.

        Returns:
            Model: The saved Model object.
        """
        if is_partial_model(self.__class__):
            msg = 'Partial models cannot be saved!'
            raise AmsdalError(msg)

        if self._is_inside_save:
            msg = 'Trying to save an object that is already being saved'
            raise AmsdalRecursionError(msg)

        self._is_inside_save = True

        try:
            if force_insert:
                if (
                    self.objects.using(using or DEFAULT_DB_ALIAS)
                    .filter(_address__object_id=self._object_id)
                    .count()
                    .execute()
                ):
                    raise ObjectAlreadyExistsError(address=self._metadata.address)

                self._is_new_object = True

            _is_new_object = self._is_new_object

            if _is_new_object:
                self._create(using=using, skip_hooks=skip_hooks)
            else:
                self._update(using=using, skip_hooks=skip_hooks)

        finally:
            self._is_inside_save = False

        return self

    @transaction
    def delete(self, using: str | None = None, *, skip_hooks: bool = False) -> None:
        """
        Deletes the existing record of the Model object from the database.

        This method first calls the `pre_delete()` method, then deletes the record from the database by calling
            the `_delete()` method, and finally calls the `post_delete()` method.
        It changes the flag `is_deleted` to True in the metadata of the record.

        Args:
            using (str | None): The name of the database to use.
            skip_hooks (bool): Indicates whether to skip the `pre_delete()` and `post_delete()` hooks.

        Returns:
            None
        """
        if is_partial_model(self.__class__):
            msg = 'Partial models cannot be deleted!'
            raise AmsdalError(msg)

        if self._is_inside_save:
            msg = 'Trying to delete an object that is already being saved'
            raise AmsdalRecursionError(msg)

        self._is_inside_save = True

        try:
            if not skip_hooks:
                self.pre_delete()

            if not self._metadata.is_latest:
                msg = 'Error! Trying to make a new version of an object that is not the latest version!'
                raise ValueError(msg)

            self.objects.bulk_delete([self], using=using)  # type: ignore[arg-type,call-arg]

            if not skip_hooks:
                self.post_delete()

        finally:
            self._is_inside_save = False

    @property
    def display_name(self) -> str:
        """
        Gets the display name of the Model object.

        This method returns the string representation of the object's address.

        Returns:
            str: The display name of the Model object.
        """
        return str(self.get_metadata().address)

    def _check_unique(self) -> None:
        from amsdal_models.classes.manager import ClassManager

        if self.__class__.__name__ in ['ClassObject', 'ClassObjectMeta', 'Object']:
            return

        meta_model = ClassManager().import_model_class('ClassObjectMeta', SchemaTypes.CORE)
        obj = (
            meta_model.objects.using(LAKEHOUSE_DB_ALIAS).latest().filter(title=self.__class__.__name__).get().execute()
        )

        if obj.unique:
            qs = self.objects.latest().filter(_metadata__is_deleted=False)

            if not self._is_new_object:
                qs = qs.exclude(_address__object_id=self._object_id)

            _q: Q | None = None

            for unique_properties in obj.unique:
                _sub_q = Q(**{_property: getattr(self, _property) for _property in unique_properties})
                _q = _sub_q if _q is None else _q | _sub_q

            if qs.filter(_q).count().execute():  # type: ignore[arg-type]
                msg = f'Object with these unique properties {obj.unique} already exists'
                raise AmsdalUniquenessError(msg)

    def _create(self, using: str | None, *, skip_hooks: bool = False) -> None:
        if not skip_hooks:
            self.pre_create()

        self._process_nested_objects()
        self._check_unique()
        self.objects.bulk_create([self], using=using)  # type: ignore[arg-type,call-arg]

        try:
            self._is_new_object = False

            if not skip_hooks:
                self.post_create()
        except Exception:
            self._is_new_object = True
            raise

    def _update(self, using: str | None, *, skip_hooks: bool = False) -> None:
        if not skip_hooks:
            self.pre_update()

        if not self._metadata.is_latest:
            msg = 'Error! Trying to make a new version of an object that is not the latest version!'
            raise ValueError(msg)

        self._process_nested_objects()
        self._check_unique()
        self.objects.bulk_update([self], using=using)  # type: ignore[arg-type,call-arg]

        if not skip_hooks:
            self.post_update()

    def _process_nested_objects(self) -> None:
        for field in sorted(self.model_fields_set):
            setattr(self, field, self._process_nested_field(getattr(self, field)))

    def _process_nested_field(self, field_value: Any) -> Any:
        if isinstance(field_value, LegacyModel):
            return field_value.get_metadata().reference
        if isinstance(field_value, Model):
            if field_value.is_new_object:
                field_value.save()  # type: ignore
            return field_value.get_metadata().reference
        elif isinstance(field_value, (list, set, tuple)):  # noqa: UP038
            return [self._process_nested_field(item) for item in field_value]
        elif isinstance(field_value, dict):
            return {
                self._process_nested_field(key): self._process_nested_field(value) for key, value in field_value.items()
            }
        return field_value

    def model_dump_refs(
        self,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> dict[str, Any]:
        """
        Dumps the record and its references into a dictionary of data.

        Args:
            mode (Literal['json', 'python'] | str): The mode in which `to_python` should run. If mode is 'json',
                the dictionary will only contain JSON serializable types. If mode is 'python',
                the dictionary may contain any Python objects.
            include (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to include
                in the output.
            exclude (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to exclude from
                the output.
            by_alias (bool): Whether to use the field's alias in the dictionary key if defined.
            exclude_unset (bool): Whether to exclude fields that are unset or None from the output.
            exclude_defaults (bool): Whether to exclude fields that are set to their default value from the output.
            exclude_none (bool): Whether to exclude fields that have a value of `None` from the output.
            round_trip (bool): Whether to enable serialization and deserialization round-trip support.
            warnings (bool): Whether to log warnings when invalid fields are encountered.

        Returns:
            dict[str, Any]: A dictionary representation of the model.
        """
        return super().model_dump_refs(
            mode=mode,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )

    def model_dump(  # type: ignore[override]
        self,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> dict[str, Any]:
        """
        This method is used to dump the record dictionary of data, although the referenced objects will be represented
        in reference format. Here is an example of reference format:

            {
              "$ref": {
                "resource": "sqlite",
                "class_name": "Person",
                "class_version": "1234",
                "object_id": "4567",
                "object_version": "8901"
              }
            }

        Args:
            mode (Literal['json', 'python'] | str): The mode in which `to_python` should run. If mode is 'json', the
                dictionary will only contain JSON serializable types. If mode is 'python', the dictionary may contain
                any Python objects.
            include (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to include
                in the output.
            exclude (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to exclude from
                the output.
            by_alias (bool): Whether to use the field's alias in the dictionary key if defined.
            exclude_unset (bool): Whether to exclude fields that are unset or None from the output.
            exclude_defaults (bool): Whether to exclude fields that are set to their default value from the output.
            exclude_none (bool): Whether to exclude fields that have a value of `None` from the output.
            round_trip (bool): Whether to enable serialization and deserialization round-trip support.
            warnings (bool): Whether to log warnings when invalid fields are encountered.

        Returns:
            dict[str, Any]: A dictionary representation of the model.
        """
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )

    def model_dump_json_refs(
        self,
        *,
        indent: int | None = None,
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> str:
        """
        Similar to `model_dump_refs`, but returns a JSON string instead of a dictionary.

        Args:
            indent (int | None): Indentation to use in the JSON output. If None is passed, the output will be compact.
            include (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to include
                in the output.
            exclude (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to exclude from
                the output.
            by_alias (bool): Whether to use the field's alias in the dictionary key if defined.
            exclude_unset (bool): Whether to exclude fields that are unset or None from the output.
            exclude_defaults (bool): Whether to exclude fields that are set to their default value from the output.
            exclude_none (bool): Whether to exclude fields that have a value of `None` from the output.
            round_trip (bool): Whether to enable serialization and deserialization round-trip support.
            warnings (bool): Whether to log warnings when invalid fields are encountered.

        Returns:
            str: A JSON string representation of the model.
        """

        return super().model_dump_json_refs(
            indent=indent,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )

    def model_dump_json(  # type: ignore[override]
        self,
        *,
        indent: int | None = None,
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> str:
        """
        Similar to `model_dump`, but returns a JSON string instead of a dictionary.

        Args:
            indent (int | None): Indentation to use in the JSON output. If None is passed, the output will be compact.
            include (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to include
                in the output.
            exclude (set[int] | set[str] | dict[int, Any] | dict[str, Any] | None): A list of fields to exclude from
                the output.
            by_alias (bool): Whether to use the field's alias in the dictionary key if defined.
            exclude_unset (bool): Whether to exclude fields that are unset or None from the output.
            exclude_defaults (bool): Whether to exclude fields that are set to their default value from the output.
            exclude_none (bool): Whether to exclude fields that have a value of `None` from the output.
            round_trip (bool): Whether to enable serialization and deserialization round-trip support.
            warnings (bool): Whether to log warnings when invalid fields are encountered.

        Returns:
            str: A JSON string representation of the model.
        """

        return super().model_dump_json(
            indent=indent,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )

    def previous_version(self) -> Self | None:
        """
        Gets the previous version of the Model object from the database.

        This method returns the Model object that is the previous version of the current object, if it exists.
            Otherwise, it returns None.

        Returns:
            Self | None: The previous version of the Model object.
        """
        return self.objects.previous_version(obj=self)

    def next_version(self) -> Self | None:
        """
        Gets the next version of the Model object from the database.

        This method returns the Model object that is the next version of the current object, if it exists. Otherwise,
            it returns None.

        Returns:
            Self | None: The next version of the Model object.
        """
        return self.objects.next_version(obj=self)

    def refetch_from_db(self) -> Self:
        """
        Gets the object with the current version from the database.

        Returns:
            Self: The object with the current version from the database.
        """
        refetched_object = self.objects.get_specific_version(
            object_id=self.object_id,
            object_version=self.object_version,
        )

        if refetched_object is None:
            msg = f'Object with id {self.object_id} and version {self.object_version} does not exist'
            raise AmsdalError(msg)

        return refetched_object

    def __getattribute__(self, name: str) -> Any:
        from amsdal_utils.models.data_models.reference import Reference

        from amsdal_models.classes.helpers.reference_loader import ReferenceLoader

        if name.endswith(REFERENCE_FIELD_SUFFIX):
            return super().__getattribute__(name[: -len(REFERENCE_FIELD_SUFFIX)])

        res = super().__getattribute__(name)

        with contextlib.suppress(PydanticUserError, AmsdalError):
            if isinstance(res, Reference):
                res = ReferenceLoader(res).load_reference()
        return res

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False

        current_metadata = self.get_metadata()
        other_metadata = other.get_metadata()

        if (
            current_metadata.address.class_name != other_metadata.address.class_name
            or current_metadata.address.object_id != other_metadata.address.object_id
        ):
            return False
        if current_metadata.is_latest and other_metadata.is_latest:
            return True

        return current_metadata.address.object_version == other_metadata.address.object_version

    def __neq__(self, other: Any) -> bool:
        return not self.__eq__(other)


class LegacyModel(TypeModel, metaclass=AmsdalModelMetaclass):
    """
    LegacyModel class that inherits from TypeModel and uses AmsdalModelMetaclass as its metaclass.

    Attributes:
        model_config (ConfigDict): Configuration for the model.
    """

    model_config = ConfigDict(extra='allow')
