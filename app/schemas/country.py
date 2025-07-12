from pydantic import BaseModel, Field
from typing import Optional


class CountryBase(BaseModel):
    name: str = Field(..., description="Name of the country")
    phonecode: str = Field(..., description="Phone code of the country")
    iso_code: str = Field(..., description="ISO code of the country")
    currency: str = Field(..., description="Currency of the country")


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryBase):
    name: Optional[str] = None
    phonecode: Optional[str] = None
    iso_code: Optional[str] = None
    currency: Optional[str] = None


class Country(CountryBase):
    id: int = Field(..., description="Unique identifier for the country")

    class Config:
        orm_mode = True
