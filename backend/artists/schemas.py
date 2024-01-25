from pydantic import BaseModel
from typing import Optional

class ArtistBase(BaseModel):
  name: str
  bio: str
  
class ArtistInDB(ArtistBase):
  artist_id: int