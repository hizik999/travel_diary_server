from pydantic import BaseModel


class TicketViewModel(BaseModel):
    title: str|None = None
    type: str = "Bug"
    status: str = "Draft"


class TicketModel(TicketViewModel):
    id: int