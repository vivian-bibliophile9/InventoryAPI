from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from .database import Base

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    quantity = Column(Integer, index=True)
    dateAdded = Column(DateTime, nullable=False, default=func.now())
    dateEdited = Column(DateTime, nullable=False, 
                        default=func.now(), onupdate=func.now())
    
    #add tags later



"""
    columns to be added
    name: str
    description: str
    quantity: int
    dateAdded: datetime
    dateEdited: datetime
    tags: List[str]
"""