from pydantic_settings import BaseSettings
from urllib.parse import urlparse

class Settings(BaseSettings):
    CONN_STRING: str
    OPENAI_API_KEY: str
    
    @property
    def DATABASE_NAME(self) -> str:
        """Extract database name from connection string"""
        parsed = urlparse(self.CONN_STRING)
        return parsed.path.lstrip('/')

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings() 