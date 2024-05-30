from sqlalchemy.orm import Session

from core.models import models
from .score_schemas import ScoreCreate, ScoreUpdate


def create_score(db: Session, score: ScoreCreate, student_id: int):
    db_score = models.Score(subject=score.subject, value=score.value, student_id=student_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def get_score(db: Session, score_id: int, student_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id, models.Score.student_id == student_id).first()

def update_score(db: Session, score_id: int, score: ScoreUpdate):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        for key, value in score.model_dump(exclude_unset=True).items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
