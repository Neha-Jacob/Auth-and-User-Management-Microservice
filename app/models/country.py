from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    phonecode = Column(String, nullable=False)
    iso_code = Column(String, nullable=False, unique=True)
    currency = Column(String, nullable=False)

    users = relationship("User", back_populates="country")
