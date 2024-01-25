from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from credits import crud


router = APIRouter(
  prefix='/credits',
  tags=['Credits'],
  responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

@router.get('/')
def get_credits(db: Session = Depends(get_db)):
  return crud.get_credits(db)
