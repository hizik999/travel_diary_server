from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uvicorn import run
from app.database import get_db
import app.crud as crud
import app.models as models

app = FastAPI()


### Label endpoints
### обновление labels
@app.post("/label/")
def create_labels(db: Session = Depends(get_db)):
    return crud.create_labels(db)


@app.get("/label/{label_id}", response_model=models.Label)
def get_label(label_id: int, db: Session = Depends(get_db)):
    db_label = crud.get_label(db=db, label_id=label_id)
    validate(db_label)
    return db_label

@app.get("/label/", response_model=list[models.Label])
def get_labels(db: Session = Depends(get_db)):
    db_label = crud.get_labels(db=db)
    validate(db_label)
    return db_label

### Motion endpoints
@app.post("/motion/")
def create_motion(motion: models.Motion, db: Session = Depends(get_db)):

    return crud.create_motion(db=db, motion=motion)

@app.get("/motion/")
def get_motions(db: Session = Depends(get_db)):
    db_motions = crud.get_motions(db=db)
    validate(db_motions)
    return db_motions

# @app.put("/motion")
# def update_motion_label(motion_id: int, label_id: int, db: Session = Depends(get_db)):
#     return crud.update_motion_label(db=db, motion_id=motion_id, label_id=label_id)


def validate(obj):
    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")


if __name__ == "__main__":
    run("main:app", reload=True)