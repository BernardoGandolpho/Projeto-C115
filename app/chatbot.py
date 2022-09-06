from fastapi import FastAPI, HTTPException, Body, Path, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from .answers import answers
from .models import StudentModel
from .repository.student_repository import StudentRepository

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chatbot")
def start_conversation():
    return answers[0]

@app.post("/chatbot/{step}")
def conversation(
    step: int = Path(...),
    matricula: str = Query(...),
    materia: int = Query(None),
    nota: int = Query(None),
    repository: StudentRepository = Depends(StudentRepository)
):
    try:
        id = int(matricula)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="A matrícula deve ser um número"
        )

    if step == 1:
        student = repository.list_one_student(id)

        if student is None:
            raise HTTPException(
                status_code=400,
                detail=f"Não encontrei o aluno com matrícula {id}"
            )

        response = answers[1]
        response["possible_answers"] = []
        for i in student["subjects"]:
            response["possible_answers"].append(i["subject_id"])

    elif step == 2:
        student = repository.list_one_student(id)

        response = answers[2]
        response["possible_answers"] = []
        for i in student["subjects"][materia]["grade"].keys():
            response["possible_answers"].append(i)

    elif step == 3:
        student = repository.list_one_student(id)
        grade = student["subjects"][materia]["grade"]
        response = answers[3]
        str_grade = list(grade.keys())[nota]

        messages = []
        messages.append(response["messages"][0])
        messages.append(
            f"O aluno {student['name']} teve a {str_grade} igual a {grade[str_grade]}")
        response["messages"] = messages 

    else:
        return "O Front retornou algum treco esquisito"

    return response


@ app.get("/database")
def list_students(
    repository: StudentRepository = Depends(StudentRepository)


):

    students = repository.list_all()

    if students is not None:
        return {"Estudantes": students}

    raise HTTPException(
        status_code=404, detail=f"Não existem estudantes matriculados")


@ app.post("/database", response_model=StudentModel)
def create_student(
        student: StudentModel = Body(...),
        repository: StudentRepository = Depends(StudentRepository)
):
    new_student = jsonable_encoder(student)

    response = repository.add(new_student)

    if type(response) is type(HTTPException(status_code=400)):
        raise response

    return response


@ app.delete("/database/{id}")
def delete_student(
    id: int = Path(...),
    repository: StudentRepository = Depends(StudentRepository)
):
    response = repository.remove(id)

    if type(response) is type(HTTPException(status_code=400)):
        raise response

    return response
