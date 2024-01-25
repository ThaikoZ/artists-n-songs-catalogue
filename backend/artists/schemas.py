from pydantic import BaseModel

class ArtistBase(BaseModel):
  name: str
  bio: str
  
class ArtistInDB(ArtistBase):
  artist_id: int