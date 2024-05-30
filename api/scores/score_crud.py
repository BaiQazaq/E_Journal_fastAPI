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

