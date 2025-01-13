from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int 
    REDIS_PASSWORD: str
    MONGODB_URI: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()