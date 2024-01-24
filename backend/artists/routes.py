from fastapi import APIRouter, status, Depends
from artists import crud
from artists import schemas 
from sqlalchemy.orm import Session
from core.database import get_db


router = APIRouter(
  prefix='/artists',
  tags=['Artists'],
  responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

@router.get('/')
def get_artists(db: Session = Depends(get_db)):
   # TODO: Get Search Query params: limit, skip, order by, etc
  return crud.get_artists(db)

@router.get('/{artist_id}')
def get_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
  return crud.get_artist_by_id(db, artist_id)

@router.post('/')
def create_artist(data: schemas.CreateArtist, db: Session = Depends(get_db)):
  return crud.create_artist(db, data)

@router.delete('/{artist_id}')
def delete_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
  return crud.delete_artist_by_id(db, artist_id)

@router.put('/{artist_id}')
def update_artist(artist_id: int, data: schemas.CreateArtist, db: Session = Depends(get_db)):
  return crud.update_artist(db, artist_id, data)
