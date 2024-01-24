from pydantic import BaseModel
from typing import Optional

class CreateArtist(BaseModel):
  name: str
  bio: str = Optional[None]
  