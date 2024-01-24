from pydantic import BaseModel
from typing import List

class CreateSong(BaseModel):
  title: str
  duration_in_seconds: int = 180
  album_title: str
  sold_copies: int = 0
  