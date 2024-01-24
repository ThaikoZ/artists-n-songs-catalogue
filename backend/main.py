from fastapi import FastAPI
from core import models
from core.database import engine
import uvicorn
from songs.routes import router as songs_router
from artists.routes import router as artists_router


models.Base.metadata.create_all(bind=engine)

# Routers
app = FastAPI()
app.include_router(songs_router)
app.include_router(artists_router)
  
if __name__ == '__main__':
  uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)