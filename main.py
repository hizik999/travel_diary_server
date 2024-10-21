from fastapi import FastAPI
import uvicorn
from db import Database
from fastapi import HTTPException
from models import TicketModel


app = FastAPI()
db = Database()
db.load_database()

@app.get("/")
def home():
    return { "message": f"Home page" }


@app.get("/tickets")
def tickets(id: int = None):
    db.load_database()
    if id is None:
        return db.tickets
    results = [ticket for ticket in db.tickets if ticket.id == id]
    if results:
        return results[0]
    raise HTTPException(status_code=404, detail=f"Ticket {id} not found")


# @app.get("/tickets/{id}")
# def one_ticket(id: int):
#     db = Database()
#     results = [ticket for ticket in db.tickets if ticket['id'] == id]
#     return results



### продвинутый get (поиск)
@app.post("/ticketpost")
def ticketpost(item: TicketModel):
    return item

### добавление
@app.put("/ticketput")
def ticketput(item: TicketModel):
    items = db.tickets
    item.id = items[-1].id + 1
    db.append(item)
    return item


### изменение
@app.patch("/ticket")
def ticketpatch(item: TicketModel):
    results = [ticket for ticket in db.tickets if ticket.id == item.id]
    if results:
        results[0].title = item.title
        results[0].status = item.status
        results[0].type = item.type
        db.save_database()    
    return item


### удаление
@app.delete("/ticket/{id}")
def ticketdelete(id: int):
    db.delete(id)
    return db.load_database()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)