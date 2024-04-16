import pydantic
from pydantic import BaseModel

class PropertyExample(BaseModel):
    # Location
    # country: str
    # city: str
    # region: str
    country_iso_code: str = None
    countryIsoCode: str = None

    @property
    def iso_code(self):
        """A hack since sometime the API return country_iso_code and other times countryIsoCode..."""
        return self.country_iso_code or self.countryIsoCode
    

if __name__ == "__main__":
    print(pydantic.__version__ )
    temp_01 = PropertyExample(country_iso_code="country_iso_code")
    temp_02 = PropertyExample(countryIsoCode="countryIsoCode")
    print(temp_01.iso_code)
    print(temp_02.iso_code)