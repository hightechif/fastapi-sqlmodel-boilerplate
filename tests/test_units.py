from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.unit import Unit

def test_create_unit(client: TestClient):
    response = client.post(
        "/api/v1/units/",
        json={"name": "Test Unit", "price": 10.5, "description": "Test Desc"},
    )
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "Test Unit"
    assert data["price"] == 10.5
    assert data["description"] == "Test Desc"
    assert data["id"] is not None


def test_read_unit(client: TestClient, session: Session):
    unit = Unit(name="Read Unit", price=5.0)
    session.add(unit)
    session.commit()
    session.refresh(unit)

    response = client.get(f"/api/v1/units/{unit.id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Read Unit"
    assert data["id"] == unit.id


def test_read_units(client: TestClient, session: Session):
    unit1 = Unit(name="Unit 1", price=1.0)
    unit2 = Unit(name="Unit 2", price=2.0)
    session.add(unit1)
    session.add(unit2)
    session.commit()

    response = client.get("/api/v1/units/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2


def test_update_unit(client: TestClient, session: Session):
    unit = Unit(name="Update Unit", price=10.0)
    session.add(unit)
    session.commit()
    session.refresh(unit)

    response = client.put(
        f"/api/v1/units/{unit.id}",
        json={"price": 20.0, "is_available": False},
    )
    data = response.json()
    assert response.status_code == 200
    assert data["price"] == 20.0
    assert data["is_available"] is False
    assert data["name"] == "Update Unit"


def test_delete_unit(client: TestClient, session: Session):
    unit = Unit(name="Delete Unit", price=10.0)
    session.add(unit)
    session.commit()
    session.refresh(unit)

    response = client.delete(f"/api/v1/units/{unit.id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/units/{unit.id}")
    assert response.status_code == 404


def test_unit_not_found(client: TestClient):
    response = client.get("/api/v1/units/999")
    assert response.status_code == 404
