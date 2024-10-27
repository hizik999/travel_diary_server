from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    run("main:app", reload=True)