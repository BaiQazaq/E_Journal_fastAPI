from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    api_prefix: str = "/api"
    db_url: str = f"sqlite:///./test.db"
    connect_args={"check_same_thread": False}
    #db_echo: bool = False #Only on production
    db_echo: bool = True

settings = Settings()