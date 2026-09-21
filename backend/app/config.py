from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    overpass_api_url: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
