from fastapi import status, HTTPException
from core import models as m
from sqlalchemy.orm import Session
from artists import schemas as s


def get_artists(db: Session):
  return db.query(m.Artist).all()

def get_artist_by_id(db: Session, artist_id: int):
  result = db.query(m.Artist).filter(m.Artist.artist_id == artist_id).first()
  if not result:
     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {artist_id} not found")
  return result

def create_artist(db: Session, data: s.CreateArtist):
  new_artist = m.Artist(
    name=data.name,
    bio=data.bio
  )
  
  db.add(new_artist)
  db.commit()
  db.refresh(new_artist)
  return new_artist

def delete_artist_by_id(db: Session, artist_id: int):
  result = db.query(m.Artist).filter(m.Artist.artist_id == artist_id).first()
  if not result:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {artist_id} not found")
  db.delete(result)
  db.commit()
  return result

def update_artist(db: Session, artist_id: int, data: s.CreateArtist):
  result = db.query(m.Artist).filter(m.Artist.artist_id == artist_id).first()
  if not result:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {artist_id} not found")
  
  result.name = data.name
  result.bio = data.bio
  
  db.commit()
  db.refresh(result)
  return result