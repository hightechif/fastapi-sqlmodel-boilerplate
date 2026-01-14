"""Pydantic schemas for API requests and responses"""
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


from app.models.unit import UnitBase


class UnitCreate(UnitBase):
    """Schema for creating a new unit"""
    pass


class UnitUpdate(BaseModel):
    """Schema for updating an existing unit"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    is_available: Optional[bool] = None


class UnitResponse(UnitBase):
    """Schema for unit response"""
    id: int

    model_config = ConfigDict(from_attributes=True)
