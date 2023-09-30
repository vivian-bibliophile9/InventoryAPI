from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db, Base
from . import schemas, CRUDutils


#This creates the main application.
app = FastAPI()


#This is an example of a API route.
#On whatever URL this app is hosted on, for example 127.0.0.1
#127.0.0.1/ will return with this JSON message 
@app.get("/")
def root():
    return {"message": "Hello World"}


#CRUD stuff
Base.metadata.create_all(bind=engine)


@app.get("/items")
def getItems(db: Session = Depends(get_db)):
    return CRUDutils.get_items(db)

@app.get("/item{id}")
def getItem(id: int, db: Session = Depends(get_db)):
    return CRUDutils.get_item(db, id)


@app.post("/add")
def addItem(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return CRUDutils.create_item(db, item)

@app.patch("/edit/{id}")
def editItem(id: int, item : schemas.ItemUpdate, db: Session = Depends(get_db)):
    return CRUDutils.update(db, id, item)

@app.delete("/remove/{id}")
def removeItem(id: int, db: Session = Depends(get_db)):
    return CRUDutils.delete(db, id)
