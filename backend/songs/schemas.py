from pydantic import BaseModel
from typing import List, Optional

class CreateSong(BaseModel):
  title: str
  duration_in_seconds: int
  album_title: str
  sold_copies: int
  artists: List[str]
  
class SongInDB(CreateSong):
  song_id: int