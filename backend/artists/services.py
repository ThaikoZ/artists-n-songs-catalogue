from sqlalchemy.orm import Session
from artists import crud

def get_artists(db: Session, skip: int = 0, limit: int = 100):
  return crud.get_artists(db, skip, limit)