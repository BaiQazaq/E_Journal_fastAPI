from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from core.models.database import db_helper
from .students_schemas import Student, StudentCreate, StudentUpdate
from .students_crud import (
                            create_student as make_student,
                            get_student, 
                            delete_student as del_student,
                            update_student as change_student,)

router = APIRouter(tags=["Students"])

@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(db_helper.get_db)):
    return make_student(db=db, student=student)

@router.get("/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(db_helper.get_db)):
    db_student = get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student by id -> {student_id} not found for showig")
    return db_student

@router.delete("/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(db_helper.get_db)):
    db_student = del_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student by id -> {student_id} not found for deleting")
    return db_student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(db_helper.get_db)):
    db_student = change_student(db=db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student by id -> {student_id} not found for updeting")
    return db_student