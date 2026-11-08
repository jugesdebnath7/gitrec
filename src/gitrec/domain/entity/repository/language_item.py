# src/gitrec/domain/entity/repository/language_item.py

from __future__ import annotations

from pydantic import BaseModel


class LanguageItem(BaseModel):
    """
    Represents a programming language used in a repository within the
    GitRec domain.

    The entity contains the repository association and programming
    language name used by downstream storage and feature-engineering
    pipelines.

    Attributes:
        repo_id: Unique identifier of the repository that uses the
            programming language.
        language: Name of the programming language.
    """
    repo_id: int
    language: str

