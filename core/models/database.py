from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.settings import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_engine(
            url = url,
            echo = echo,
        )
        self.SessionLocal = sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False,
            expire_on_commit = False,
        )

db_helper = DatabaseHelper(
    url = settings.db_url, 
    echo = settings.db_echo,
)

Base = declarative_base()