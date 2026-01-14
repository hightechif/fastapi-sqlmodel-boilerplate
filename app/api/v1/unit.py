"""API routes and endpoints"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.db.schema import UnitCreate, UnitUpdate, UnitResponse
from app.services import unit_service as crud

router = APIRouter(prefix="/units", tags=["units"])


@router.post("/", response_model=UnitResponse, status_code=status.HTTP_201_CREATED)
def create_unit(
    unit: UnitCreate,
    session: Session = Depends(get_session)
):
    """Create a new unit"""
    return crud.create_unit(session=session, unit=unit)


@router.get("/", response_model=List[UnitResponse])
def read_units(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session)
):
    """Get all units with pagination"""
    units = crud.get_units(session=session, skip=skip, limit=limit)
    return units


@router.get("/{unit_id}", response_model=UnitResponse)
def read_unit(
    unit_id: int,
    session: Session = Depends(get_session)
):
    """Get a single unit by ID"""
    db_unit = crud.get_unit(session=session, unit_id=unit_id)
    if not db_unit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unit with id {unit_id} not found"
        )
    return db_unit


@router.put("/{unit_id}", response_model=UnitResponse)
def update_unit(
    unit_id: int,
    unit: UnitUpdate,
    session: Session = Depends(get_session)
):
    """Update an existing unit"""
    db_unit = crud.update_unit(session=session, unit_id=unit_id, unit_update=unit)
    if not db_unit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unit with id {unit_id} not found"
        )
    return db_unit


@router.delete("/{unit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_unit(
    unit_id: int,
    session: Session = Depends(get_session)
):
    """Delete an unit"""
    success = crud.delete_unit(session=session, unit_id=unit_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unit with id {unit_id} not found"
        )
    return None
