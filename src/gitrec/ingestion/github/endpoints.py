# src/gitrec/ingestion/github/endpoints.py

"""
GitHub REST API endpoint builders.

This module provides immutable endpoint builders for GitHub REST API resources
used by the ingestion layer.

Responsibilities
----------------
This module is responsible only for constructing endpoint paths.

It does not:

- perform HTTP requests
- authenticate requests
- serialize or deserialize payloads
- validate API responses
- implement retries, pagination, or rate limiting

Examples
--------
>>> repo = repository("psf", "requests")
>>> repo.base
'/repos/psf/requests'

>>> repo.languages
'/repos/psf/requests/languages'

>>> repo.commit("main")
'/repos/psf/requests/commits/main'

>>> user = user("octocat")
>>> user.starred
'/users/octocat/starred'
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


__all__ = [
    "SearchEndpoint",
    "RepositoryEndpoints",
    "UserEndpoints",
    "repository",
    "user",
]


class SearchEndpoint(StrEnum):
    """GitHub search API endpoints."""

    REPOSITORIES = "/search/repositories"
    USERS = "/search/users"
    CODE = "/search/code"
    ISSUES = "/search/issues"
    COMMITS = "/search/commits"


@dataclass(frozen=True, slots=True)
class _EndpointBuilder:
    """Base class for endpoint builders."""

    _base: str = field(init=False, repr=False)

    @property
    def base(self) -> str:
        """Base endpoint."""
        return self._base

    def _join(self, *parts: str) -> str:
        """Append path segments to the base endpoint."""
        return "/".join((self.base, *parts))


@dataclass(frozen=True, slots=True)
class RepositoryEndpoints(_EndpointBuilder):
    """GitHub REST endpoints for a repository."""

    owner: str
    repo: str

    def __post_init__(self) -> None:
        if not self.owner:
            raise ValueError("owner cannot be empty")

        if not self.repo:
            raise ValueError("repo cannot be empty")

        object.__setattr__(
            self,
            "_base",
            f"/repos/{self.owner}/{self.repo}",
        )

    #
    # Collection endpoints
    #

    @property
    def topics(self) -> str:
        return self._join("topics")

    @property
    def languages(self) -> str:
        return self._join("languages")

    @property
    def contributors(self) -> str:
        return self._join("contributors")

    @property
    def commits(self) -> str:
        return self._join("commits")

    @property
    def releases(self) -> str:
        return self._join("releases")

    @property
    def branches(self) -> str:
        return self._join("branches")

    @property
    def tags(self) -> str:
        return self._join("tags")

    @property
    def issues(self) -> str:
        return self._join("issues")

    @property
    def pulls(self) -> str:
        return self._join("pulls")

    @property
    def forks(self) -> str:
        return self._join("forks")

    @property
    def stargazers(self) -> str:
        return self._join("stargazers")

    @property
    def subscribers(self) -> str:
        return self._join("subscribers")

    @property
    def readme(self) -> str:
        return self._join("readme")

    #
    # Parameterized endpoints
    #

    def commit(self, sha: str) -> str:
        return self._join("commits", sha)

    def branch(self, name: str) -> str:
        return self._join("branches", name)

    def release(self, release_id: int | str) -> str:
        return self._join("releases", str(release_id))

    def issue(self, number: int) -> str:
        return self._join("issues", str(number))

    def pull_request(self, number: int) -> str:
        return self._join("pulls", str(number))

    def contents(self, path: str = "") -> str:
        if path:
            return self._join("contents", path)

        return self._join("contents")


@dataclass(frozen=True, slots=True)
class UserEndpoints(_EndpointBuilder):
    """GitHub REST endpoints for a user."""

    username: str

    def __post_init__(self) -> None:
        if not self.username:
            raise ValueError("username cannot be empty")

        object.__setattr__(
            self,
            "_base",
            f"/users/{self.username}",
        )

    @property
    def profile(self) -> str:
        return self.base

    @property
    def repositories(self) -> str:
        return self._join("repos")

    @property
    def starred(self) -> str:
        return self._join("starred")

    @property
    def followers(self) -> str:
        return self._join("followers")

    @property
    def following(self) -> str:
        return self._join("following")

    @property
    def organizations(self) -> str:
        return self._join("orgs")

    @property
    def gists(self) -> str:
        return self._join("gists")

    @property
    def events(self) -> str:
        return self._join("events")

    @property
    def received_events(self) -> str:
        return self._join("received_events")


def repository(owner: str, repo: str) -> RepositoryEndpoints:
    """Create a repository endpoint builder."""
    return RepositoryEndpoints(owner, repo)


def user(username: str) -> UserEndpoints:
    """Create a user endpoint builder."""
    return UserEndpoints(username)