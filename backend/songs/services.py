from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from songs import crud, schemas as s
from artists import crud as artist_crud, schemas as artist_schemas
from credits import crud as credit_crud, schemas as credit_schemas

def get_songs(db: Session, skip: int = 0, limit: int = 100):
  return crud.get_songs(db, skip, limit)
  
  
def get_song_by_id(db: Session, song_id: int):
  result = crud.get_song_by_id(db, song_id)
  if not result:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with id {song_id} not found")
  return result


def create_song(db: Session, data: s.CreateSong):
  new_song = crud.create_song(db, data)
  
  for name in data.artists:
    artist = artist_crud.get_artist_by_name(db, name)
    if not artist_crud.get_artist_by_name(db, name):
      artist = artist_crud.create_artist(db, artist_schemas.ArtistBase(name=name, bio=''))
  
    credit_crud.create_credit(db, credit_schemas.CreditBase(artist_id=artist.artist_id, song_id=new_song.song_id))

  return new_song 