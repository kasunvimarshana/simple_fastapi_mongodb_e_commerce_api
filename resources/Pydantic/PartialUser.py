import pydantic
from pydantic import BaseModel, Field

class PartialUser(BaseModel):
    def __init__(self, **data):
        super().__init__(
            id=data.pop("old_id", None) or data.pop("id", None),
            **data,
        )

    id: int
    name: str
    display_name: str


if __name__ == "__main__":
    print(pydantic.__version__ )
    temp_01 = PartialUser(id=1, name="name", display_name="display_name")
    temp_02 = PartialUser(old_id=1, name="username", display_name="display_name")
    print(temp_01)
    print(temp_02)
