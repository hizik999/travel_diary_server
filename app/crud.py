from sqlalchemy.orm import Session
from app.models import Label, Motion
from app.schemas import MotionSchema, LabelSchema
from app.labels import Labels

### валидация через pydantic (то что в models) в аргументах фунеции, а создание экземпляра бд через sqlalchemy (то что в schemas) внутри функции

### CRUD label - доступные операции: очистить и заполнить заново labels, получить label по id, получить все labels
### очистить и заполнить заново labels из enum класса Labels
def create_labels(db: Session):
    db.query(LabelSchema).delete()
    for label in Labels:
        db.add(LabelSchema(id=label.value['id'], name=label.value['name']))
    db.commit()
    return {'msg': 'labels created successfully'}


# def create_coarse(db: Session, coarse: CoarseSchema):
#     db_coarse = Coarse(id=coarse.id, name=coarse.name)
#     db.add(db_coarse)
#     db.commit()
#     db.refresh(db_coarse)
#     return db_coarse

# def get_coarse(db: Session, coarse_id: int):
#     return db.query(Coarse).filter(Coarse.id == coarse_id).first()

# def get_coarses(db: Session):
#     return db.query(Coarse).all()

# def update_coarse(db: Session, coarse_id: int, name: str):
#     db_coarse = db.query(Coarse).filter(Coarse.id == coarse_id).first()
#     if db_coarse is None:
#         return None
#     db_coarse.name = name
#     db.commit()
#     db.refresh(db_coarse)
#     return db_coarse

# def delete_coarse(db: Session, coarse_id: int):
#     db_coarse = db.query(Coarse).filter(Coarse.id == coarse_id).first()
#     if db_coarse is None:
#         return None
#     db.delete(db_coarse)
#     db.commit()
#     return db_coarse



# def create_motion(db: Session, motion: MotionSchema):
#     db_coarse = get_coarse(db, motion.coarse_id)
#     if db_coarse is None:
#         raise ValueError(f"Coarse with id {motion.coarse_id} does not exist")
    
#     db_motion = Motion(
#         time=motion.time,
#         acceleration_x=motion.acceleration_x,
#         acceleration_y=motion.acceleration_y,
#         acceleration_z=motion.acceleration_z,
#         gyro_x=motion.gyro_x,
#         gyro_y=motion.gyro_y,
#         gyro_z=motion.gyro_z,
#         magnetometer_x=motion.magnetometer_x,
#         magnetometer_y=motion.magnetometer_y,
#         magnetometer_z=motion.magnetometer_z,
#         pressure=motion.pressure,
#         coarse_id=motion.coarse_id,
#     )
#     db.add(db_motion)
#     db.commit()
#     db.refresh(db_motion)
#     return db_motion

# def get_motion(db: Session, motion_id: int):
#     return db.query(Motion).filter(Motion.id == motion_id).first()

# def get_motions(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Motion).offset(skip).limit(limit).all()

# def update_motion(db: Session, motion_id: int, motion_data: MotionSchema):
#     db_motion = db.query(Motion).filter(Motion.id == motion_id).first()
#     print(db_motion)
#     if db_motion is None:
#         return None
#     if motion_data.coarse_id is not None:
#         db_coarse = get_coarse(db, motion_data.coarse_id)
#         if db_coarse is None:
#             raise ValueError(f"Coarse with id {motion_data.coarse_id} does not exist")
#         db_motion.coarse_id = motion_data.coarse_id

    
#     db.commit()
#     db.refresh(db_motion)
#     return db_motion

# def delete_motion(db: Session, motion_id: int):
#     db_motion = db.query(Motion).filter(Motion.id == motion_id).first()
#     if db_motion is None:
#         return None
#     db.delete(db_motion)
#     db.commit()
#     return db_motion
