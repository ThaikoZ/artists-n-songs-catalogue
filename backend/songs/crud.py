from fastapi import status, HTTPException
from core import models as m
from sqlalchemy.orm import Session
from songs import schemas as s


def get_songs(db: Session):
  return db.query(m.Song).all()


def get_song_by_id(db: Session, song_id: int):
  result = db.query(m.Song).filter(m.Song.song_id == song_id).first()
  if not result:
     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with id {song_id} not found")
  return result


def create_song(db: Session, data: s.CreateSong):
  new_song = m.Song(
    title=data.title,
    duration_in_seconds=data.duration_in_seconds,
    album_title=data.album_title,
    sold_copies=data.sold_copies
  )
  
  db.add(new_song)
  db.commit()
  db.refresh(new_song)
  return new_song


def delete_song_by_id(db: Session, song_id: int):
  result = db.query(m.Song).filter(m.Song.song_id == song_id).first()
  if not result:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with id {song_id} not found")
  db.delete(result)
  db.commit()
  return result


def update_song(db: Session, song_id: int, data: s.CreateSong): 
  result = db.query(m.Song).filter(m.Song.song_id == song_id).first()
  if not result:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with id {song_id} not found")
  
  result.title = data.title
  result.duration_in_seconds = data.duration_in_seconds
  result.album_title = data.album_title
  result.sold_copies = data.sold_copies
  
  db.commit()
  db.refresh(result)
  return result
  


