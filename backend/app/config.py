from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    aws_region: str = "ap-south-1"
    s3_bucket: str
    database_url: str
    embed_model_id: str = "amazon.titan-embed-text-v2:0"
    llm_model_id: str = "meta.llama3-1-8b-instruct-v1:0"
    
settings = Settings()