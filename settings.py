from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):

    token: str
    api_url: str
    temp_url: str
    api_key: str

    model_config = SettingsConfigDict(env_file='.env')


setting = Settings()
