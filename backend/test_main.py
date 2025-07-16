import pytest
from fastapi.testclient import TestClient
from main import app, init_db
import sqlite3
import os

client = TestClient(app)

@pytest.fixture(scope="function")
def test_db():
    test_db_name = "test_cars.db"
    if os.path.exists(test_db_name):
        os.remove(test_db_name)
    
    # Temporarily change database name for testing
    import main
    original_db = main.DATABASE
    main.DATABASE = test_db_name
    
    init_db()
    
    yield test_db_name
    
    # Cleanup
    main.DATABASE = original_db
    if os.path.exists(test_db_name):
        os.remove(test_db_name)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Car Rental API"}

def test_get_cars_empty(test_db):
    # Clear the database first
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cars")
    conn.commit()
    conn.close()
    
    response = client.get("/cars")
    assert response.status_code == 200
    assert response.json() == []

def test_get_cars_with_data(test_db):
    response = client.get("/cars")
    assert response.status_code == 200
    
    cars = response.json()
    assert len(cars) == 4
    assert cars[0]["make"] == "Toyota"
    assert cars[0]["model"] == "Camry"
    assert cars[0]["year"] == 2023
    assert cars[0]["daily_rate"] == 45.0
    assert cars[0]["available"] == True

def test_get_cars_only_available(test_db):
    # Mark one car as unavailable
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE cars SET available = FALSE WHERE id = 1")
    conn.commit()
    conn.close()
    
    response = client.get("/cars")
    assert response.status_code == 200
    
    cars = response.json()
    assert len(cars) == 3  # Only available cars
    for car in cars:
        assert car["available"] == True

def test_car_data_structure(test_db):
    response = client.get("/cars")
    assert response.status_code == 200
    
    cars = response.json()
    if cars:
        car = cars[0]
        required_fields = ["id", "make", "model", "year", "daily_rate", "available"]
        for field in required_fields:
            assert field in car
        
        assert isinstance(car["id"], int)
        assert isinstance(car["make"], str)
        assert isinstance(car["model"], str)
        assert isinstance(car["year"], int)
        assert isinstance(car["daily_rate"], (int, float))
        assert isinstance(car["available"], bool)