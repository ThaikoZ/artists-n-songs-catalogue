from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from artists import crud, schemas as s

def get_artists(db: Session, skip: int = 0, limit: int = 100):
  return crud.get_artists(db, skip, limit)