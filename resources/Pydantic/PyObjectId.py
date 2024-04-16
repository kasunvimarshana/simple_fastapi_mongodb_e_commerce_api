import pydantic
from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

class User_1(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

if __name__ == "__main__":
    print(pydantic.__version__ )
    print(User_1(_id="id"))