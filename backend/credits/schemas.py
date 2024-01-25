from pydantic import BaseModel

class CreditBase(BaseModel):
  artist_id: int
  song_id: int