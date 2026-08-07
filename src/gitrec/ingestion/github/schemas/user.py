# src/gitrec/ingestion/github/schemas/user.py

from __future__ import annotations

from pydantic import BaseModel


class UserSearchResult(BaseModel):
    """
    User search result schema.

    This schema represents the structure of a GitHub user search result
    returned by the GitHub search API. It is used to validate and parse the
    raw JSON payloads received from the API.

    Attributes:
        login (str): The username of the user.
    """
    login: str