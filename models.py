from pydantic import BaseModel, Field
from enum import Enum


class TypeEnum(Enum):
    Bug = "Bug"
    Epic = "Epic"
    Story = "Story"

class TicketModel(BaseModel):
    id: int
    title: str = Field(max_length=30, default=None)
    type: TypeEnum = TypeEnum.Bug
    status: str = "Draft"
    severity: int = Field(default=0, ge=0, le=10, multiple_of=2)