from fastapi import APIRouter

__all__ = (
    "Score",
    "ScoreBase",
    "ScoreCreate",
    "ScoreUpdate",
    "Student",
    "StudentBase",
    "StudentCreate",
    "StudentUpdate",
)

from .scores.score_schemas import  Score, ScoreBase, ScoreCreate, ScoreUpdate
from .students.students_schemas import Student, StudentBase, StudentCreate, StudentUpdate

from .students.students_view import router as students_router
#from .scores.score_views import router as scores_router

student_router = APIRouter()
student_router.include_router(router=students_router, prefix="/students")

#score_router = APIRouter()
#score_router.include_router(router=scores_router, prefix="/scores")
