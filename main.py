from fastapi import FastAPI
import uvicorn
from db import Database
from fastapi import HTTPException
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def home():
    return { "message": f"Home page" }


@app.get("/tickets")
def tickets(id: int = None):
    db = Database()
    if id is None:
        return db.tickets
    results = [ticket for ticket in db.tickets if ticket['id'] == id]
    if results:
        return results[0]
    raise HTTPException(status_code=404, detail=f"Ticket {id} not found")


# @app.get("/tickets/{id}")
# def one_ticket(id: int):
#     db = Database()
#     results = [ticket for ticket in db.tickets if ticket['id'] == id]
#     return results

class TicketModel(BaseModel):
    id: int
    title: str|None

### продвинутый get (поиск)
@app.post("/ticketpost")
def ticketpost(item: TicketModel):
    return item

### добавление
@app.put("/ticketput")
def ticketput(item: TicketModel):
    return item


### изменение
@app.patch("/ticketpatch")
def ticketpatch(item: TicketModel):
    return item


### удаление
@app.delete("/ticket/{id}")
def ticketdelete(id: int):
    return id


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)