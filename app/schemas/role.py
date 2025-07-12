from pydantic import BaseModel, Field
from typing import Optional


class RoleBase(BaseModel):
    role: str = Field(..., description="Name of the role")
    description: Optional[str] = Field(None, description="Description of the role")
    permissions: str = Field(..., description="Permissions associated with the role")


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    role: Optional[str] = None
    description: Optional[str] = None
    permissions: Optional[str] = None


class Role(RoleBase):
    id: int = Field(..., description="Unique identifier for the role")

    class Config:
        orm_mode = True
