from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from app.core.config import get_settings

settings = get_settings()

# SQLAlchemy engine
engine = create_engine(settings.database_url, echo=True)

# SessionLocal is a factory for session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model declarations
Base = declarative_base()


# Dependency to use in FastAPI routes
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
