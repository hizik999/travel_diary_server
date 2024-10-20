from fastapi import FastAPI
import uvicorn
from db import Database


app = FastAPI()


@app.get("/")
def home():
    return { "message": f"Home page" }


@app.get("/tickets")
def tickets():
    db = Database()
    return db.tickets

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)