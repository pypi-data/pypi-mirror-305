from amsdal_utils.models.enums import SchemaTypes as SchemaTypes
from pathlib import Path
from pydantic import BaseModel

class SchemasDirectory(BaseModel):
    """
    Schema for a schemas' directory.

    This class represents the schema for a directory containing schemas, including the path
    to the directory and the type of schemas it contains.

    Attributes:
        path (Path): The path to the directory containing schemas.
        schema_type (SchemaTypes): The type of schemas contained in the directory.
    """
    path: Path
    schema_type: SchemaTypes
