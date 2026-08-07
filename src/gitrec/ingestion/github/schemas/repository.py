# src/gitrec/ingestion/github/schemas/repository.py

from __future__ import annotations

from pydantic import BaseModel


class RepositorySearchResult(BaseModel):
    """
    Repository search result schema.

    This schema represents the structure of a GitHub repository search result
    returned by the GitHub search API. It is used to validate and parse the
    raw JSON payloads received from the API.

    Attributes:
        owner (str): The username of the repository owner.
        name (str): The name of the repository.
    """
    owner: str
    name: str