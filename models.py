from pydantic import BaseModel

class TicketModel(BaseModel):
    id: int
    title: str|None = None
    type: str = "Bug"
    status: str = "Draft"