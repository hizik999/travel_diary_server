from sqlalchemy.orm import Session
from app.schemas import MotionSchema, LabelSchema
from app.models import Motion
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

### получить label(id, name) по id 
def get_label(db: Session, label_id: int):
    return db.query(LabelSchema).filter(LabelSchema.id == label_id).first()

### получить все labels
def get_labels(db: Session):
    return db.query(LabelSchema).all()

### CRUD motions - создать motion, получить motion по timestamp, получить все motions в интервале time_start и time_end, обновить label_id в motion по timestamp, ->
### -> получить все motions по user_imei, 

def create_motion(db: Session, motion: Motion):
    db_motion = MotionSchema(**motion.dict())
    db.add(db_motion)
    db.commit()
    db.refresh(db_motion)
    return db_motion

def get_motion(db: Session, time: int):
    return db.query(MotionSchema).filter(MotionSchema.time == time).all()

def get_motions(db: Session, time_start: int, time_end: int):
    return db.query(MotionSchema).filter(MotionSchema.time >= time_start, MotionSchema.time <= time_end).all()

def get_motions(db: Session, user_imei: str):
    return db.query(MotionSchema).filter(MotionSchema.user_imei == user_imei).all()

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
