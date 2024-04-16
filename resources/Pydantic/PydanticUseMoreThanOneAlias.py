import pydantic
from pydantic import BaseModel, Field, AliasChoices

class PydanticUseMoreThanOneAlias(BaseModel):
    first_name: str = Field(validation_alias=AliasChoices('first_name', 'fname'))


if __name__ == "__main__":
    print(pydantic.__version__ )
    temp_01 = PydanticUseMoreThanOneAlias(first_name="Sam")
    temp_02 = PydanticUseMoreThanOneAlias(fname="toto")
    print(temp_01.model_dump())
    print(temp_02.model_dump())