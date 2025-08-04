# pyright: reportCallIssue=false
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    app_host: str = "127.0.0.1"
    app_port: int = 8000
    debug: bool = True

    SECRET_KEY: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )


# Функция с кэшем — создаёт один экземпляр настроек на всё приложение
@lru_cache
def get_settings() -> Settings:
    return Settings()