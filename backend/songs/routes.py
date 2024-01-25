from fastapi import APIRouter, status, Depends
from songs import schemas 
from songs import services 
from sqlalchemy.orm import Session
from core.database import get_db


router = APIRouter(
  prefix='/songs',
  tags=['Songs'],
  responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

@router.get('/')
def get_songs(db: Session = Depends(get_db)):
  return services.get_songs(db)

@router.get('/{song_id}')
def get_song(song_id: int, db: Session = Depends(get_db)):
  return services.get_song_by_id(db, song_id)

@router.post('/')
def create_song(data: schemas.CreateSong, db: Session = Depends(get_db)):
  return services.create_song(db, data)
