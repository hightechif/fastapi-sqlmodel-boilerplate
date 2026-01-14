"""CRUD operations for database models"""
from typing import List, Optional
from sqlmodel import Session, select
from app.models.unit import Unit
from app.db.schema import UnitCreate, UnitUpdate


def create_unit(session: Session, unit: UnitCreate) -> Unit:
    """Create a new unit in the database"""
    db_unit = Unit(**unit.model_dump())
    session.add(db_unit)
    session.commit()
    session.refresh(db_unit)
    return db_unit


def get_unit(session: Session, unit_id: int) -> Optional[Unit]:
    """Get a single unit by ID"""
    return session.get(Unit, unit_id)


def get_units(session: Session, skip: int = 0, limit: int = 100) -> List[Unit]:
    """Get a list of units with pagination"""
    statement = select(Unit).offset(skip).limit(limit)
    results = session.exec(statement)
    return results.all()


def update_unit(session: Session, unit_id: int, unit_update: UnitUpdate) -> Optional[Unit]:
    """Update an existing unit"""
    db_unit = session.get(Unit, unit_id)
    if not db_unit:
        return None
    
    # Update only provided fields
    unit_data = unit_update.model_dump(exclude_unset=True)
    for key, value in unit_data.items():
        setattr(db_unit, key, value)
    
    session.add(db_unit)
    session.commit()
    session.refresh(db_unit)
    return db_unit


def delete_unit(session: Session, unit_id: int) -> bool:
    """Delete an unit from the database"""
    db_unit = session.get(Unit, unit_id)
    if not db_unit:
        return False
    
    session.delete(db_unit)
    session.commit()
    return True
