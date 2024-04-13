# Entity.py

from typing import TYPE_CHECKING, List
from beanie import Document

# Need to avoid IDE static type checkings
if TYPE_CHECKING:
    from .Folder import Folder

class Entity(Document):
    path: List["Folder"] = []

# Need to be here, AFTER `Entity` class definition
from .Folder import Folder

# Updating ForwardRefs
# Entity.update_forward_refs(Folder=Folder)
Entity.model_rebuild(Folder=Folder)