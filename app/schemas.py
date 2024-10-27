from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field(..., max_length=50, min_length=1)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
