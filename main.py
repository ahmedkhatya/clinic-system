from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from psycopg2 import sql, errors

app = FastAPI()

# CORS عشان الموبايل يقدر يتصل
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# نموذج بيانات المريض
class Patient(BaseModel):
    name: str
    phone: str
    age: int

# اتصال قاعدة البيانات
conn = psycopg2.connect(
    dbname="clinic_db",
    user="postgres",
    password="postgres123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# إنشاء جدول لو مش موجود
cur.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    age INT NOT NULL,
    UNIQUE(name, phone)
)
""")
conn.commit()

# إضافة مريض
@app.post("/patients")
def add_patient(patient: Patient):
    try:
        cur.execute(
            "INSERT INTO patients (name, phone, age) VALUES (%s, %s, %s)",
            (patient.name, patient.phone, patient.age)
        )
        conn.commit()
        return {"message": "تم إضافة المريض بنجاح"}
    except errors.UniqueViolation:
        conn.rollback()
        raise HTTPException(status_code=400, detail="المريض موجود بالفعل")

# جلب كل المرضى
@app.get("/patients")
def get_patients():
    cur.execute("SELECT name, phone, age FROM patients ORDER BY id DESC")
    rows = cur.fetchall()
    return [{"name": r[0], "phone": r[1], "age": r[2]} for r in rows]

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory=".", html=True), name="static")