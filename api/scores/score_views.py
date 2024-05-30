from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from core.models.database import db_helper
from .score_schemas import Score, ScoreCreate, ScoreUpdate
from .score_crud import (
                            create_score as make_score,
                            get_score,
                            update_score as change_score,
                            delete_score as remove_score,
                        )

router = APIRouter(tags=["Score"])

@router.post("/student/{student_id}/scores/", response_model=Score)
def create_score_for_student(student_id: int, score: ScoreCreate, db: Session = Depends(db_helper.get_db)):
    return make_score(db=db, score=score, student_id=student_id)

@router.get("/student/{student_id}/scores/{score_id}", response_model=Score)
def read_score(student_id: int, score_id: int, db: Session = Depends(db_helper.get_db)):
    db_score = get_score(db=db, score_id=score_id, student_id=student_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found for reading")
    return db_score

@router.put("/student/{student_id}/scores/{score_id}", response_model=Score)
def update_score(student_id: int, score_id: int, score: ScoreUpdate, db: Session = Depends(db_helper.get_db)):
    db_score = change_score(db=db, score_id=score_id, score=score)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found for changing")
    return db_score

@router.delete("/student/{student_id}/scores/{score_id}", response_model=Score)
def delete_score(student_id: int, score_id: int, db: Session = Depends(db_helper.get_db)):
    db_score = remove_score(db=db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found for removing")
    return db_score
