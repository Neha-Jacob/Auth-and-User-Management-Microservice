from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Auth and User Management Service"
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
