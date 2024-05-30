import uvicorn
from fastapi import FastAPI

from core.models.database import db_helper
from core.models.models import Base
from api import student_router, score_router
from core.settings import settings


Base.metadata.create_all(bind=db_helper.engine)

app = FastAPI()
app.include_router(router=student_router, prefix=settings.api_prefix)
app.include_router(router=score_router)

@app.get('/')
def read_root(name: str = "Luna-Corn"):
    name = name.strip().title()
    return  f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)