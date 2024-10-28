from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uvicorn import run
from app.database import get_db
import app.crud as crud
import app.schemas as schemas


app = FastAPI()


@app.post("/coarse/", response_model=schemas.CoarseSchema, status_code=status.HTTP_201_CREATED)
def create_coarse(coarse: schemas.CoarseSchema, db: Session = Depends(get_db)):
    db_coarse = crud.get_coarse(db, coarse.id)
    if db_coarse:
        raise HTTPException(status_code=400, detail="Coarse ID already exists")
    return crud.create_coarse(db=db, coarse=coarse)

@app.get("/coarse/{coarse_id}", response_model=schemas.CoarseSchema)
def read_coarse(coarse_id: int, db: Session = Depends(get_db)):
    db_coarse = crud.get_coarse(db, coarse_id)
    if db_coarse is None:
        raise HTTPException(status_code=404, detail="Coarse not found")
    return db_coarse

@app.get("/coarse/", response_model=list[schemas.CoarseSchema])
def read_coarses(db: Session = Depends(get_db)):
    return crud.get_coarses(db=db)

@app.put("/coarse/{coarse_id}", response_model=schemas.CoarseSchema)
def update_coarse(coarse_id: int, name: str, db: Session = Depends(get_db)):
    db_coarse = crud.update_coarse(db=db, coarse_id=coarse_id, name=name)
    if db_coarse is None:
        raise HTTPException(status_code=404, detail="Coarse not found")
    return db_coarse

@app.delete("/coarse/{coarse_id}", response_model=schemas.CoarseSchema)
def delete_coarse(coarse_id: int, db: Session = Depends(get_db)):
    db_coarse = crud.delete_coarse(db=db, coarse_id=coarse_id)
    if db_coarse is None:
        raise HTTPException(status_code=404, detail="Coarse not found")
    return db_coarse

# Motion Endpoints

@app.post("/motion/", response_model=schemas.MotionSchema, status_code=status.HTTP_201_CREATED)
def create_motion(motion: schemas.MotionSchema, db: Session = Depends(get_db)):
    db_coarse = crud.get_coarse(db, motion.coarse_id)
    if db_coarse is None:
        raise HTTPException(status_code=400, detail="Invalid coarse_id")
    return crud.create_motion(db=db, motion=motion)

@app.get("/motion/{motion_id}", response_model=schemas.MotionSchema)
def read_motion(motion_id: int, db: Session = Depends(get_db)):
    db_motion = crud.get_motion(db, motion_id)
    if db_motion is None:
        raise HTTPException(status_code=404, detail="Motion not found")
    return db_motion

@app.get("/motion/", response_model=list[schemas.MotionSchema])
def read_motions(db: Session = Depends(get_db)):
    return crud.get_motions(db=db)

@app.put("/motion/{motion_id}", response_model=schemas.MotionSchema)
def update_motion(motion_id: int, motion_data: schemas.MotionSchema, db: Session = Depends(get_db)):
    if motion_data.coarse_id is not None:
        db_coarse = crud.get_coarse(db, motion_data.coarse_id)
        if db_coarse is None:
            raise HTTPException(status_code=400, detail="Invalid coarse_id")
    db_motion = crud.update_motion(db=db, motion_id=motion_id, motion_data=motion_data)
    if db_motion is None:
        raise HTTPException(status_code=404, detail="Motion not found")
    return db_motion

@app.delete("/motion/{motion_id}", response_model=schemas.MotionSchema)
def delete_motion(motion_id: int, db: Session = Depends(get_db)):
    db_motion = crud.delete_motion(db=db, motion_id=motion_id)
    if db_motion is None:
        raise HTTPException(status_code=404, detail="Motion not found")
    return db_motion


if __name__ == "__main__":
    run("main:app", reload=True)