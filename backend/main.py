import uvicorn
from fastapi import FastAPI
from core import models
from core.database import engine
from songs.routes import router as songs_router
from artists.routes import router as artists_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

# Routers
app = FastAPI()
app.include_router(songs_router)
app.include_router(artists_router)
  
# CORS Middleware
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
  
if __name__ == '__main__':
  uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)