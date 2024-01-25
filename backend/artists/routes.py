from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from artists import crud


router = APIRouter(
  prefix='/artists',
  tags=['Artists'],
  responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

@router.get('/')
def get_artists(db: Session = Depends(get_db)):
  return crud.get_artists(db)