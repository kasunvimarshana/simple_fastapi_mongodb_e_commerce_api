from pydantic import BaseModel, Field, computed_field, model_validator

class ParentModel(BaseModel):
    ...


class SourceLayer(ParentModel):
    source: str = Field(default="randomTest")
    source_uid: str = Field(description="random source uid", default=None)


class ChildModel(SourceLayer):
    account_id: str = Field(..., description="account id")

    '''
    # @computed_field(description="source uid")
    # @property
    # def source_uid(self) -> str:
    #     print("Getting value ...")
    #     return self.account_id
    '''
    
    @model_validator(mode="after")
    def assign_source_uid(self):
        print("Getting value ...")
        self.source_uid = self.account_id
        return self

child = ChildModel(account_id="123")
print(child.model_dump())
# > Getting value ...
# > {'source': 'randomTest', 'account_id': '123', 'source_uid': '123'}
