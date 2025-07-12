from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., description="Name of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    mobile: Optional[str] = Field(None, description="Mobile number of the user")
    address_line_1: Optional[str] = Field(
        None, description="First line of the user's address"
    )
    address_line_2: Optional[str] = Field(
        None, description="Second line of the user's address"
    )
    pincode: Optional[str] = Field(None, description="Pincode of the user's address")
    country_id: int = Field(..., description="ID of the country")
    role_id: int = Field(..., description="ID of the assigned role")


class UserCreate(UserBase):
    password: str = Field(..., description="Password for the user account")


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    pincode: Optional[str] = None
    country_id: Optional[int] = None
    role_id: Optional[int] = None
    password: Optional[str] = None
    verified_email: Optional[bool] = None
    verified_mobile: Optional[bool] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: UUID
    verified_email: bool
    verified_mobile: bool
    is_active: bool
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
