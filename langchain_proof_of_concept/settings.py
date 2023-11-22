from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings

import langchain_proof_of_concept


class Settings(BaseSettings):
    """
    Settings are automatically loaded from environment variables and
    can be additionally configured via .env files or directly in code.

    Attributes:
        openai_api_key: API key for OpenAI services.
    """

    openai_api_key: Optional[str] = Field(None, env="OPENAI_API_KEY")
    openai_endpoint: str = Field("https://api.openai.com/v1/chat/completions", env="OPENAI_ENDPOINT")

    class Config:
        env_file = Path(langchain_proof_of_concept.__file__).parent.parent / ".env"
        env_file_encoding = "utf-8"


settings = Settings()


__all__ = ["settings"]
