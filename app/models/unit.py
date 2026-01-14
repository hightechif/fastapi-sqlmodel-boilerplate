"""SQLModel database models"""
from typing import Optional
from sqlmodel import Field, SQLModel


class UnitBase(SQLModel):
    """Base model with shared fields"""
    name: str = Field(index=True, min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(gt=0)
    is_available: bool = Field(default=True)


class Unit(UnitBase, table=True):
    """Unit model representing units in the database"""
    id: Optional[int] = Field(default=None, primary_key=True)
