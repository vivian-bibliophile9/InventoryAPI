from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

#This is an example of an item in the inventory.
#Using this model the API can read requests from the website and return back
#information
#
#This is an example of Object Oriented Design: we can add validators, make child
#models, custom funcs, etc.
class ItemBase(BaseModel):
    name: str
    description: str
    quantity: int
    #tags: List[str] This is tough since its a list. We could use an arraytype in whatever ORM or most sensibly create a posts table and backpopulate it
    #add an id for the db

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass



class Item(ItemBase):
    id: int
    dateAdded: datetime
    dateEdited: datetime

    class config:
        orm_mode = True


