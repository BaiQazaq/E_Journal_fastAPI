from pydantic import BaseModel
from typing import List

class ScoreBase(BaseModel):
    subject: str
    value: float

class ScoreCreate(ScoreBase):
    pass

class ScoreUpdate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True