from core import models as m
from sqlalchemy.orm import Session
from songs import schemas as s


def get_songs(db: Session, skip: int = 0, limit: int = 100) -> list[s.SongInDB]:
  results = db.query(m.Song, m.Artist) \
      .outerjoin(m.Credit, m.Credit.song_id == m.Song.song_id) \
      .outerjoin(m.Artist, m.Credit.artist_id == m.Artist.artist_id) \
      .limit(limit).offset(skip).all()
      
  songs = {}
  for song, artist in results:
    if song.song_id not in songs:
      songs[song.song_id] = song
      songs[song.song_id].artists = []
    if artist:
      songs[song.song_id].artists.append(artist.name)
      
  return [songs[song_id] for song_id in songs]


def get_song_by_id(db: Session, song_id: int) -> s.SongInDB:
  results = db.query(m.Song, m.Artist) \
      .outerjoin(m.Credit, m.Credit.song_id == m.Song.song_id) \
      .outerjoin(m.Artist, m.Credit.artist_id == m.Artist.artist_id) \
      .filter(m.Song.song_id == song_id) \
      .all()
    
  if not results:
    return 
  
  songs = {}
  for song, artist in results:
    if song.song_id not in songs:
      songs[song.song_id] = song
      songs[song.song_id].artists = []
    if artist:
      songs[song.song_id].artists.append(artist.name)
      
  return songs[song_id]
  

def create_song(db: Session, data: s.CreateSong) -> s.SongInDB:
  db_song = m.Song(
    title=data.title,
    duration_in_seconds=data.duration_in_seconds,
    album_title=data.album_title,
    sold_copies=data.sold_copies,
  )
  db.add(db_song)
  db.commit()
  db.refresh(db_song)
  return db_song