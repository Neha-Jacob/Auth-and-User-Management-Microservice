from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    permissions = Column(String, nullable=False)

    users = relationship("User", back_populates="role")
