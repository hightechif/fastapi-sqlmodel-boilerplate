"""FastAPI application entry point"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.session import create_db_and_tables
from app.api.v1 import unit
from app.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown"""
    # Configure logging
    setup_logging()
    # Startup: Create database tables
    create_db_and_tables()
    yield
    # Shutdown: Clean up resources if needed


# Create FastAPI application
app = FastAPI(
    title="FastAPI SQLModel Boilerplate",
    description="A boilerplate FastAPI project using SQLModel for database operations",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )


# Include routers
app.include_router(unit.router, prefix="/api/v1")


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI SQLModel Boilerplate",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
