# src/gitrec/ingestion/github/search.py

"""
GitHub REST API search operations.

Provides a typed interface for executing GitHub search requests through the
configured GitHub client.

Responsibilities
----------------
This module is responsible for:
- selecting the appropriate GitHub search endpoint
- forwarding search parameters to the GitHub client
- exposing resource-specific search operations

It does not:
- construct HTTP requests
- manage authentication
- handle retries or pagination
- validate GitHub search syntax
- transform API responses

The query parameters passed to search methods follow GitHub's REST API
search syntax.

Examples
--------
>>> search = GitHubSearch(client)
>>> repositories = search.repositories({"q": "python"})
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeAlias

from gitrec.ingestion.github.client import GitHubClient, JSON

from .endpoints import SearchEndpoint


QueryParams: TypeAlias = Mapping[str, Any]
"""GitHub REST API query parameters."""


class GitHubSearch:
    """GitHub REST API search operations.

    Delegates request execution to :class:`GitHubClient` while providing
    resource-specific search methods.
    """

    def __init__(self, client: GitHubClient) -> None:
        self._client = client

    def repositories(self, query: QueryParams) -> JSON:
        return self._client.get(
            SearchEndpoint.REPOSITORIES,
            query,
        )

    def users(self, query: QueryParams) -> JSON:
        return self._client.get(
            SearchEndpoint.USERS,
            query,
        )

    def code(self, query: QueryParams) -> JSON:
        return self._client.get(
            SearchEndpoint.CODE,
            query,
        )

    def issues(self, query: QueryParams) -> JSON:
        return self._client.get(
            SearchEndpoint.ISSUES,
            query,
        )

    def commits(self, query: QueryParams) -> JSON:
        return self._client.get(
            SearchEndpoint.COMMITS,
            query,
        )