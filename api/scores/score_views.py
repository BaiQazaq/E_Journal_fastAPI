from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from core.models.database import db_helper
from .score_schemas import Score, ScoreCreate, ScoreUpdate
from .score_crud import (
                            create_score as make_score,
                            get_score, 
                        )

router = APIRouter(tags=["Score"])

@router.post("/student/{student_id}/scores/", response_model=Score)
def create_score_for_student(student_id: int, score: ScoreCreate, db: Session = Depends(db_helper.get_db)):
    return make_score(db=db, score=score, student_id=student_id)

@router.get("/student/{student_id}/scores/{score_id}", response_model=Score)
def read_score(student_id: int, score_id: int, db: Session = Depends(db_helper.get_db)):
    db_score = get_score(db=db, score_id=score_id, student_id=student_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score
