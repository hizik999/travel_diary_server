# schema.py
from pydantic import BaseModel, Field, conint, validator
from typing import Optional

class CoarseSchema(BaseModel):
    id: conint(ge=0, le=1000)  # Ограничение на диапазон ID от 0 до 8
    name: str = Field(..., max_length=50)

    class Config:
        orm_mode = True  # Позволяет работать с объектами SQLAlchemy напрямую

class MotionSchema(BaseModel):
    time: int = Field(..., description="Unix timestamp")
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float
    magnetometer_x: float
    magnetometer_y: float
    magnetometer_z: float
    pressure: float
    coarse_id: Optional[conint(ge=0, le=1000)] = Field(default=0, description="Coarse ID value from 0 to 8")

    @validator('time')
    def validate_time(cls, v):
        if v < 0:
            raise ValueError("Time must be a positive Unix timestamp")
        return v

    class Config:
        allow_mutation = False  # Поля неизменяемы, кроме coarse_id

    def set_coarse_id(self, value: int):
        if not 0 <= value <= 8:
            raise ValueError("Coarse ID value must be between 0 and 8")
        object.__setattr__(self, 'coarse_id', value)
