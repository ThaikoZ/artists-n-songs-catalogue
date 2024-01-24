from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Credit(Base):
    __tablename__ = 'credits'
    song_id = Column(Integer, ForeignKey('songs.song_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    artist_id = Column(Integer, ForeignKey('artists.artist_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    song = relationship('Song', back_populates='credits')
    artist = relationship('Artist', back_populates='credits')

class Song(Base):
    __tablename__ = 'songs'

    song_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False)
    duration_in_seconds = Column(Integer, nullable=False, default=180)
    album_title = Column(String(45), nullable=True)
    sold_copies = Column(Integer, default=0)
    
    credits = relationship('Credit', back_populates='song')
    
class Artist(Base):
    __tablename__ = 'artists'

    artist_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)
    bio = Column(String(255), nullable=True)
    
    credits = relationship('Credit', back_populates='artist')
  