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
            available BOOLEAN DEFAULT TRUE
        )
    """)
    
    cursor.execute("""
        INSERT OR IGNORE INTO cars (make, model, year, daily_rate, available)
        VALUES 
        ('Toyota', 'Camry', 2023, 45.00, 1),
        ('Honda', 'Civic', 2022, 35.00, 1),
        ('Tesla', 'Model 3', 2024, 75.00, 1),
        ('Ford', 'Explorer', 2023, 65.00, 1)
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