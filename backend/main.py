from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI(title="Car Rental API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE = "cars.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            daily_rate REAL NOT NULL,
            available BOOLEAN DEFAULT TRUE,
            type TEXT NOT NULL,
            fuel_capacity INTEGER NOT NULL,
            transmission TEXT NOT NULL,
            passenger_capacity INTEGER NOT NULL,
            category TEXT NOT NULL,
            is_popular BOOLEAN DEFAULT FALSE
        )
    """)
    
    cursor.execute("""
        INSERT OR IGNORE INTO cars (make, model, year, daily_rate, available, type, fuel_capacity, transmission, passenger_capacity, category, is_popular)
        VALUES 
        ('Koenigsegg', 'Sport', 2024, 99.00, 1, 'Sport', 90, 'Manual', 2, 'Popular Car', 1),
        ('Nissan', 'GT-R', 2024, 80.00, 1, 'Sport', 80, 'Manual', 2, 'Popular Car', 1),
        ('Rolls-Royce', 'Sedan', 2024, 96.00, 1, 'Sedan', 70, 'Manual', 4, 'Popular Car', 1),
        ('All New Rush', 'SUV', 2024, 72.00, 1, 'SUV', 70, 'Manual', 6, 'Recommendation Car', 0),
        ('CR-V', 'SUV', 2024, 80.00, 1, 'SUV', 80, 'Manual', 6, 'Recommendation Car', 0),
        ('All New Terios', 'SUV', 2024, 74.00, 1, 'SUV', 90, 'Manual', 6, 'Recommendation Car', 0),
        ('MG ZX Exclusive', 'Hatchback', 2024, 76.00, 1, 'Hatchback', 70, 'Manual', 4, 'Recommendation Car', 0),
        ('New MG ZS', 'SUV', 2024, 80.00, 1, 'SUV', 80, 'Manual', 6, 'Recommendation Car', 0),
        ('MG ZX Excite', 'Hatchback', 2024, 74.00, 1, 'Hatchback', 90, 'Manual', 4, 'Recommendation Car', 0)
    """)
    
    conn.commit()
    conn.close()

class Car(BaseModel):
    id: Optional[int] = None
    make: str
    model: str
    year: int
    daily_rate: float
    available: bool = True
    type: str
    fuel_capacity: int
    transmission: str
    passenger_capacity: int
    category: str
    is_popular: bool = False

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to Car Rental API"}

@app.get("/cars", response_model=List[Car])
async def get_cars():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE available = TRUE")
    cars = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return cars

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)