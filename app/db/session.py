"""Database configuration and session management"""
import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings


# Get database URL from environment or use default SQLite
DATABASE_URL = settings.DATABASE_URL

# Create engine
# connect_args is only needed for SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session
