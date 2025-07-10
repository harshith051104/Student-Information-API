# config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # This tells Pydantic to load variables from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKENS_EXPIRE_MINUTES: int

    # Database Settings
    MONGO_URI: str


# Create a single instance of the Settings class
# All other files will import this `settings` object
settings = Settings()