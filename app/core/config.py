import logging
import os
import sys
from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

env_file_to_load = os.getenv("ENV_FILE", ".env.local")


class EnvState(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


class GlobalSettings(BaseSettings):
    """Global configurations shared across all environments."""
    ENV_STATE: EnvState = EnvState.DEV
    PROJECT_NAME: str = "CoGym eCommerce"
    SECRET_KEY: str = "your-super-secret-key-change-this-in-prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database Settings (Common keys)
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=env_file_to_load, extra="ignore")


class DevSettings(GlobalSettings):
    DEBUG: bool = True


class StagingSettings(GlobalSettings):
    DEBUG: bool = True


class ProdSettings(GlobalSettings):
    DEBUG: bool = False
    # In prod, you might want stricter CORS or different logging


# --- The Factory Function ---
def get_settings():
    # Read the base settings just to find out which environment we are in
    state = GlobalSettings().ENV_STATE

    if state == EnvState.PROD:
        return ProdSettings()
    elif state == EnvState.STAGING:
        return StagingSettings()
    return DevSettings()


def setup_logging():

    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    # 2. Determine logging level based on your ENV_STATE/DEBUG flag
    # DEBUG in Dev, INFO in Production
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO

    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            # StreamHandler prints to your Docker/Terminal logs
            logging.StreamHandler(sys.stdout),
            # FileHandler saves logs to a file (useful for EC2)
            logging.FileHandler("app_log.log")
        ]
    )

    if not settings.DEBUG:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


settings = get_settings()

logger = logging.getLogger("cogym")
