from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud, app.schemas as schemas
from uvicorn import run

app = FastAPI()


@app.post("/users/", response_model=schemas.UserInDB)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.UserInDB)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[schemas.UserInDB])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

@app.put("/users/{user_id}", response_model=schemas.UserInDB)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.UserInDB)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



if __name__ == "__main__":
    run("main:app", reload=True)