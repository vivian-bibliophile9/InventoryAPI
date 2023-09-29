from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

#This is an example of an item in the inventory.
#Using this model the API can read requests from the website and return back
#information
class Item(BaseModel):
    name: str
    description: str
    quantity: int
    dateAdded: datetime
    dateEdited: datetime
    tags: List[str]

