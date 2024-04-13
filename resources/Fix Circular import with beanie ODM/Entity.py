from beanie import Document
from typing import TYPE_CHECKING, \
    List

# Need to avoid IDE static type checkings
if TYPE_CHECKING:
    from .Folder import Folder

class Entity(Document):
    path: List["Folder"] = []
