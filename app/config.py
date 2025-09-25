from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_MODE: str
    model_config = SettingsConfigDict(env_file='.env')

    @property
    def DATABASE_URL_async(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

settings = Settings()