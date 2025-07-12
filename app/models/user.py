from datetime import datetime, timezone
from app.db.session import Base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    verified_email = Column(Boolean, default=False)
    mobile = Column(String, unique=True, nullable=True)
    verified_mobile = Column(Boolean, default=False)
    password = Column(String, nullable=False)
    address_line_1 = Column(String, nullable=True)
    address_line_2 = Column(String, nullable=True)
    pincode = Column(String, nullable=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    is_active = Column(Boolean, default=True)

    country = relationship("Country", back_populates="users")
    role = relationship("Role", back_populates="users")
