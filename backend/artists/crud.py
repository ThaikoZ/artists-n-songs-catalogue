from sqlalchemy.orm import Session
from artists import schemas
from core import models

def get_artists(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.ArtistInDB]:
    return db.query(models.Artist).offset(skip).limit(limit).all()

def get_artist_by_id(db: Session, artist_id: int) -> schemas.ArtistInDB:
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()

def get_artist_by_name(db: Session, name: str) -> schemas.ArtistInDB:
    return db.query(models.Artist).filter(models.Artist.name == name).first()

def create_artist(db: Session, data: schemas.ArtistBase):
    db_artist = models.Artist(
        name=data.name,
        bio=data.bio,
    )
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist