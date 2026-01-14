# FastAPI SQLModel Boilerplate

A production-ready **FastAPI** + **SQLModel** boilerplate project. This starter template provides a clean, modular architecture with built-in best practices for building scalable database-driven APIs.

## 🚀 Features

- ✅ **FastAPI** - Modern, fast web framework
- ✅ **SQLModel** - Type-safe database interactions (SQLAlchemy + Pydantic)
- ✅ **Boilerplate Structure** - Modular `api`, `core`, `db`, `models`, `services` layout
- ✅ **API Versioning** - Built-in `v1` structure
- ✅ **Dependency Management** - Powered by `uv`
- ✅ **Docker Ready** - Optimized `Dockerfile` and `docker-compose.yml`
- ✅ **Testing** - Pre-configured `pytest` suite
- ✅ **Logging** - configured logging setup

## 📁 Project Structure

```
fastapi-sqlmodel-boilerplate/
├── app/
│   ├── api/                  # API endpoints
│   │   └── v1/               # API v1 routes
│   │       └── unit.py       # Unit endpoints (example resource)
│   ├── core/                 # Configuration & Logging
│   ├── db/                   # Database setup & Schemas
│   ├── models/               # SQLModel models
│   ├── services/             # Business logic (CRUD)
│   ├── main.py               # Application entry point
│   └── __init__.py
├── tests/                    # Automated tests
├── .env                      # Environment variables
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
├── Dockerfile                # Docker build instruction
└── docker-compose.yml        # Docker composition
```

## 🛠️ Installation

### Prerequisites

- [uv](https://github.com/astral-sh/uv)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/fastapi-sqlmodel-boilerplate.git
cd fastapi-sqlmodel-boilerplate
```

2. **Install dependencies**

```bash
uv sync
```

3. **Configure environment variables**

Ensure `.env` exists:
```env
DATABASE_URL=sqlite:///./test.db
```

## 🏃 Running the Service

### Development
```bash
uv run uvicorn app.main:app --reload
```

### via Docker
```bash
docker-compose up --build
```

The API will be available at: `http://localhost:8000`

## 📚 API Endpoints (v1)

### Units (Example Resource)

- `POST /api/v1/units/` - Create a new unit
- `GET /api/v1/units/` - Get all units
- `GET /api/v1/units/{unit_id}` - Get a specific unit
- `PUT /api/v1/units/{unit_id}` - Update a unit
- `DELETE /api/v1/units/{unit_id}` - Delete a unit

## 🧪 Testing

```bash
uv run pytest
```

## 📝 License

Open Source.
