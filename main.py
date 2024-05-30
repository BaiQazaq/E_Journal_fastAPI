import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def read_root(name: str = "Luna-Corn"):
    name = name.strip().title()
    return  f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)