from _typeshed import Incomplete
from amsdal_utils.errors import AmsdalError

class AmsdalValidationError(AmsdalError):
    message: Incomplete
    def __init__(self, message: str) -> None: ...
