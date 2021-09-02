from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import os

app = FastAPI()

fakedb = []

# environment variable specified in Dockerfile
csv_file = os.environ["CSV_FILE"]

course_data = pd.read_csv(
    filepath_or_buffer=csv_file,
    sep=";",
    header=0)

course_data = course_data.to_dict(orient='records')

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None

@app.get("/")
def read_root():
    return {"greetings": "Welcome!"}

@app.get("/courses")
def get_courses():
    return fakedb

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = course_id - 1
    return fakedb[course]

@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {"task": "deletion succesful"}

@app.get("/reload")
def reload_courses():
    global fakedb
    fakedb = course_data[:]
    return fakedb