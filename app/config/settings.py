import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):

    APP_NAME: str = "FastAPI"
    DEBUG: bool = False

    # MySQL Database Config
    MYSQL_HOST: str = "mysql"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "secret"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "fastapi"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"mysql+pymysql://{quote_plus(self.MYSQL_USER)}:{quote_plus(self.MYSQL_PASSWORD)}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"


    # App Secret Key
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "changeme")

    # class Config:
    #     env_file = ".env"
    #     env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()