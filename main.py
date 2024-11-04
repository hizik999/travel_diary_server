from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uvicorn import run
from app.database import get_db
import app.crud as crud
import app.models as models
from typing import List

app = FastAPI()


### Label endpoints
### обновление labels
@app.post("/label/")
def create_labels(db: Session = Depends(get_db)):
    return crud.create_labels(db)


@app.get("/label/{label_id}", response_model=models.Label)
def get_label(label_id: int, db: Session = Depends(get_db)):
    db_label = crud.get_label(db=db, label_id=label_id)
    if db_label is None:
        raise HTTPException(status_code=404, detail="Label not found")
    return db_label

@app.get("/label/", response_model=list[models.Label])
def get_labels(db: Session = Depends(get_db)):
    return crud.get_labels(db=db)

### Motion endpoints
@app.post("/motion/")
def create_motion(motion: models.Motion, db: Session = Depends(get_db)):
    return crud.create_motion(db=db, motion=motion)

@app.get("/motion/{time}")
def get_motion(time: int, db: Session = Depends(get_db)):
    db_motion = crud.get_motion(db=db, time=time)
    if db_motion is None:
        raise HTTPException(status_code=404, detail=f"Motion not found")
    return db_motion

@app.get("/motion/")
def get_motions(time_start: int, time_end: int, db: Session = Depends(get_db)):
    db_motions = crud.get_motions(db=db, time_start=time_start, time_end=time_end)
    if db_motions is None:
        raise HTTPException(status_code=404, detail="Motions not found")
    return db_motions

@app.get("/motion/{user_imei}")
def get_motions(user_imei: str, db: Session = Depends(get_db)):
    db_motions = crud.get_motions(db=db, user_imei=user_imei)
    if db_motions is None:
        raise HTTPException(status_code=404, detail="Motions not found")
    return db_motions
# @app.post("/coarse/", response_model=models.Coarse, status_code=status.HTTP_201_CREATED)
# def create_coarse(coarse: models.Coarse, db: Session = Depends(get_db)):
#     db_coarse = crud.get_coarse(db, coarse.id)
#     if db_coarse:
#         raise HTTPException(status_code=400, detail="Coarse ID already exists")
#     return crud.create_coarse(db=db, coarse=coarse)

# @app.get("/coarse/{coarse_id}", response_model=models.Coarse)
# def read_coarse(coarse_id: int, db: Session = Depends(get_db)):
#     db_coarse = crud.get_coarse(db, coarse_id)
#     if db_coarse is None:
#         raise HTTPException(status_code=404, detail="Coarse not found")
#     return db_coarse

# @app.get("/coarse/", response_model=list[models.Coarse])
# def read_coarses(db: Session = Depends(get_db)):
#     return crud.get_coarses(db=db)

# @app.put("/coarse/{coarse_id}", response_model=models.Coarse)
# def update_coarse(coarse_id: int, name: str, db: Session = Depends(get_db)):
#     db_coarse = crud.update_coarse(db=db, coarse_id=coarse_id, name=name)
#     if db_coarse is None:
#         raise HTTPException(status_code=404, detail="Coarse not found")
#     return db_coarse

# @app.delete("/coarse/{coarse_id}", response_model=models.Coarse)
# def delete_coarse(coarse_id: int, db: Session = Depends(get_db)):
#     db_coarse = crud.delete_coarse(db=db, coarse_id=coarse_id)
#     if db_coarse is None:
#         raise HTTPException(status_code=404, detail="Coarse not found")
#     return db_coarse

# # Motion Endpoints

# @app.post("/motion/", response_model=models.Motion, status_code=status.HTTP_201_CREATED)
# def create_motion(motion: models.Motion, db: Session = Depends(get_db)):
#     db_coarse = crud.get_coarse(db, motion.coarse_id)
#     if db_coarse is None:
#         raise HTTPException(status_code=400, detail="Invalid coarse_id")
#     return crud.create_motion(db=db, motion=motion)

# @app.get("/motion/{motion_id}", response_model=models.Motion)
# def read_motion(motion_id: int, db: Session = Depends(get_db)):
#     db_motion = crud.get_motion(db, motion_id)
#     if db_motion is None:
#         raise HTTPException(status_code=404, detail="Motion not found")
#     return db_motion

# @app.get("/motion/", response_model=list[models.Motion])
# def read_motions(db: Session = Depends(get_db)):
#     return crud.get_motions(db=db)

# @app.put("/motion/{motion_id}", response_model=models.Motion)
# def update_motion(motion_id: int, motion_data: models.Motion, db: Session = Depends(get_db)):
#     if motion_data.coarse_id is not None:
#         db_coarse = crud.get_coarse(db, motion_data.coarse_id)
#         if db_coarse is None:
#             raise HTTPException(status_code=400, detail="Invalid coarse_id")
#     db_motion = crud.update_motion(db=db, motion_id=motion_id, motion_data=motion_data)
#     if db_motion is None:
#         raise HTTPException(status_code=404, detail="Motion not found")
#     return db_motion

# @app.delete("/motion/{motion_id}", response_model=models.Motion)
# def delete_motion(motion_id: int, db: Session = Depends(get_db)):
#     db_motion = crud.delete_motion(db=db, motion_id=motion_id)
#     if db_motion is None:
#         raise HTTPException(status_code=404, detail="Motion not found")
#     return db_motion


if __name__ == "__main__":
    run("main:app", reload=True)