# src/gitrec/ingestion/github/pyloader.py

from __future__ import annotations

import logging
from gitrec.ingestion.github.client import GitHubClient


class GitHubLoader:
    def __init__(self, client: GitHubClient) -> None:
        self._client = client

    def load(self) -> dict[str, str]:    
        ...