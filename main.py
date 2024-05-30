import uvicorn
from fastapi import FastAPI
from core.models.database import db_helper, Base
from core import models

models.Base.metadata.create_all(bind=db_helper.engine)

app = FastAPI()

def get_db():
    db = db_helper.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def read_root(name: str = "Luna-Corn"):
    name = name.strip().title()
    return  f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)