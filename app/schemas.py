from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CoarseSchema(Base):
    __tablename__ = "coarses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)  # No auto-increment to restrict IDs 0-8
    name = Column(String, nullable=False)

    # Опционально: определение строкового представления для удобства отладки
    def __repr__(self):
        return f"<Coarse(id={self.id}, name={self.name})>"

class MotionSchema(Base):
    __tablename__ = "motions"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer, nullable=False)
    acceleration_x = Column(Float, nullable=True)
    acceleration_y = Column(Float, nullable=True)
    acceleration_z = Column(Float, nullable=True)
    gyro_x = Column(Float, nullable=True)
    gyro_y = Column(Float, nullable=True)
    gyro_z = Column(Float, nullable=True)
    magnetometer_x = Column(Float, nullable=True)
    magnetometer_y = Column(Float, nullable=True)
    magnetometer_z = Column(Float, nullable=True)
    pressure = Column(Float, nullable=True)
    coarse_id = Column(Integer, ForeignKey(f'{CoarseSchema.__tablename__}.id'), nullable=True)

    # Связь с моделью Coarse
    coarse = relationship("Coarse")

    def set_coarse_id(self, value: int):
        if not 0 <= value <= 8:
            raise ValueError("Coarse ID must be between 0 and 8")
        self.coarse_id = value
