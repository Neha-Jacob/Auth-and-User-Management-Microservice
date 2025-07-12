from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Auth and User Management Service"

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "userdb"
    postgres_port: str = "5432"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
