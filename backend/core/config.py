import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings

env_path = Path('.') / ".env"

load_dotenv()

class Settings(BaseSettings):
  DATABASE_URL: str = os.getenv("DATABASE_URL")


def get_settings() -> Settings:
  return Settings()