from core import models as m
from sqlalchemy.orm import Session
from songs import schemas as s


def get_songs(db: Session, skip: int = 0, limit: int = 100) -> list[s.SongInDB]:
  results = db.query(m.Song, m.Artist) \
      .join(m.Credit, m.Credit.song_id == m.Song.song_id) \
      .join(m.Artist, m.Credit.artist_id == m.Artist.artist_id) \
      .all()
      
  songs = {}
  for song, artist in results:
    if song.song_id not in songs:
      songs[song.song_id] = song
      songs[song.song_id].artists = []
    if artist:
      songs[song.song_id].artists.append(artist.name)
      
  return songs


def get_song_by_id(db: Session, song_id: int) -> s.SongInDB:
  results = db.query(m.Song, m.Artist) \
      .join(m.Credit, m.Credit.song_id == m.Song.song_id) \
      .join(m.Artist, m.Credit.artist_id == m.Artist.artist_id) \
      .filter(m.Song.song_id == song_id) \
      .all()
    
  if not results:
    return 
  
  song = results[0][0] 
  artists = [artist.name for _, artist in results if artist]
  song_in_db = s.SongInDB(
    song_id=song.song_id,
    title=song.title,
    duration_in_seconds=song.duration_in_seconds,
    album_title=song.album_title,
    sold_copies=song.sold_copies,
    artists=artists
  )

  return song_in_db


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