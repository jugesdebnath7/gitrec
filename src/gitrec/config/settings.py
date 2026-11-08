# src/gitrec/config/settings.py

from functools import lru_cache
from typing import Optional, Literal
from pathlib import Path
from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    PostgresDsn,
    SecretStr,
    field_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


# -------------------------------
# DATABASE
# -------------------------------

class DatabaseSettings(BaseModel):
    url: PostgresDsn = Field(..., description="Postgres connection URL")

    pool_size: int = Field(default=5, ge=1)
    max_overflow: int = Field(default=10, ge=0)
    pool_timeout: int = Field(default=30, gt=0)
    pool_recycle: int = Field(default=1800, gt=0)

    @property
    def dsn(self) -> str:
        return str(self.url)


# ------------------------------
# HTTP CLIENT
# ------------------------------
class HTTPSettings(BaseModel):
    timeout: int = Field(default=10, ge=1, le=60)
    retries: int = Field(default=3, ge=0, le=10)
    user_agent: str = "gitrec-app"


# ------------------------------
# GITHUB
# ------------------------------
class GitHubSettings(BaseModel):
    token: Optional[SecretStr] = None
    base_url: HttpUrl = "https://api.github.com"
    api_version: str = "2022-11-28"

    @property
    def token_value(self) -> Optional[str]:
        return self.token.get_secret_value() if self.token else None


class TrainingSettings(BaseModel):
    model_path: Path = Field(default=Path("artifacts/models/"))
    embedding_dim: int = Field(default=64, gt=0)
    batch_size: int = Field(default=128, gt=0)

    @field_validator("model_path")
    @classmethod
    def validate_model_path(cls, v: Path) -> Path:
        v = v.expanduser().resolve(strict=False)

        # Create if missing (ML-friendly behaviour)
        v.mkdir(parents=True, exist_ok=True)

        if not v.is_dir():
            raise ValueError(f"{v} is not a directory")

        return v

    
# -----------------------------
# MAIN SETTINGS
# -----------------------------
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        extra="ignore",
        frozen=True,
    )

    # Environment
    env: Literal["development", "staging", "production"] = "development"

    # Training 
    training: TrainingSettings = Field(default_factory=TrainingSettings)

    # Nested configs
    postgres: DatabaseSettings = Field(...)
    http: HTTPSettings = Field(default_factory=HTTPSettings)
    github: GitHubSettings = Field(default_factory=GitHubSettings)

    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    
# ---------------------------------
# Singleton
# ---------------------------------
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()