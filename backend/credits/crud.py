from sqlalchemy.orm import Session
from credits import schemas
from core import models

def get_credits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Credit).offset(skip).limit(limit).all()


def get_credit_by_id(db: Session, credit_id: int):
    return db.query(models.Credit).filter(models.Credit.credit_id == credit_id).first()


def create_credit(db: Session, data: schemas.CreditBase):
    db_credit = models.Credit(
        artist_id=data.artist_id,
        song_id=data.song_id
    )
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit