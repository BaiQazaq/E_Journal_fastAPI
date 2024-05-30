from sqlalchemy.orm import Session

from core.models import models
from .students_schemas import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
