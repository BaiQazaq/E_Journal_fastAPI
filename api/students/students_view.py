from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from core.models.database import db_helper
from .students_schemas import Student, StudentCreate
from .students_crud import create_student

router = APIRouter(tags=["Students"])

@router.post("/", response_model=Student)
def make_student(student: StudentCreate, db: Session = Depends(db_helper.get_db)):
    return create_student(db=db, student=student)