from pydantic import BaseModel, EmailStr
from typing import List
from api.scores.score_schemas import Score

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
