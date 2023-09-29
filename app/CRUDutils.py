##Sensibly should be its own folder, be OOPed and seperate CRUD but ehh

from sqlalchemy.orm import Session
from . import schemas, models


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ItemModel).offset(skip).limit(limit).all()

def get_item(db: Session, id: int):
    return db.query(models.ItemModel).filter(models.ItemModel.id == id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    print(dict(item))
    db_item = models.ItemModel(**dict(item))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, id: int):
    obj = db.query(models.ItemModel).filter(models.ItemModel.id == id).first()
    if not obj:
        raise Exception("Item does not exist")

    db.delete(obj)
    db.commit()
    return obj

#ahhh ill do it later
def update(db: Session, id: int, item: schemas.ItemUpdate):
    obj = db.query(models.ItemModel).filter(models.ItemModel.id == id).first()
    return obj




