from fastapi import FastAPI
import motor.motor_asyncio
from database import Base
from student import Student
from bson import ObjectId
import os
import sentry_sdk
from dotenv import load_dotenv
import models
import schemas
from database import engine
import teachers

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
load_dotenv()

app = FastAPI()

app.include_router(teachers.router)

models.Base.metadata.create_all(bind=engine)

uri = os.getenv("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

try:
    client.server_info()
    print("Connected to MongoDB")
except Exception as e:
    print(e)


@app.get("/")
async def root():
    return {"message": "Hello World we we working on argoCD"}


@app.post("/students/")
async def create_student(student: Student):
    try:
        student = student.dict()
        result = await client.students.student.insert_one(student)
        print(f"Student with id {result.inserted_id} created")
    except Exception as e:
        print(e)
    return {"message": "Student created successfully"}


@app.get("/students")
async def get_students():
    students = []
    async for student in client.students.student.find():
        students.append(Student(**student))
    return students


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = await client.students.student.find_one({"_id": ObjectId(student_id)})
    print(student)
    if student:
        student["id"] = str(student["_id"])
        del student["_id"]
        return student
    else:
        return {"message": "Student not found"}


@app.get("/sentry_debug")
async def sentry_debug():
    division_by_zero = 1 / 0
    return division_by_zero
