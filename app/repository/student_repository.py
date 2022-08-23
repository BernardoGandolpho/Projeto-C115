from os import environ

from pymongo import MongoClient
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from ..models import StudentModel

class StudentRepository():
    def __init__(self):
        self.mongo_url = (environ["DB_URI"])
        self.client = MongoClient(self.mongo_url)
        self.db = self.client['inatel']

    def list_all(self):
        students = self.db['students'].find(projection={"_id": 0})

        return list(students)

    def list_one_student(self, id):
        return self.db['students'].find_one({"student_id": id}, projection={"_id": 0})

    def add(self, student: StudentModel):
        if (self.list_one_student(id=student['student_id'])) is not None:
            return HTTPException(status_code=400, detail="ID do estudante já existente")
        
        try:
            self.db["students"].insert_one(student)
            student.pop("_id", None)

            return JSONResponse(status_code=status.HTTP_201_CREATED, content=student)
        
        except:
            return HTTPException(status_code=500, detail="Internar Server Error")

    def remove(self, id):
        delete_result = self.db["students"].delete_one({"student_id": id})

        if delete_result.deleted_count == 1:
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})

        return HTTPException(status_code=404, detail=f"Estudante {id} não encontrado")