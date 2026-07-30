"""
GitHub API endpoint builders.

Provides centralized GitHub API route definitions used by
the ingestion layer.

This module only constructs endpoint paths. It does not:
- perform HTTP requests
- handle authentication
- transform responses
"""

from __future__ import annotations


SEARCH_REPOSITORIES = "/search/repositories"


def repository(owner: str, repo: str) -> str:
    """Return repository details endpoint."""
    return f"/repos/{owner}/{repo}"


def repository_topics(owner: str, repo: str) -> str:
    """Return repository topics endpoint."""
    return f"/repos/{owner}/{repo}/topics"


def repository_languages(owner: str, repo: str) -> str:
    """Return repository languages endpoint."""
    return f"/repos/{owner}/{repo}/languages"


def repository_contributors(owner: str, repo: str) -> str:
    """Return repository contributors endpoint."""
    return f"/repos/{owner}/{repo}/contributors"


def repository_commits(owner: str, repo: str) -> str:
    """Return repository commits endpoint."""
    return f"/repos/{owner}/{repo}/commits"


def repository_releases(owner: str, repo: str) -> str:
    """Return repository releases endpoint."""
    return f"/repos/{owner}/{repo}/releases"


def user(username: str) -> str:
    """Return user profile endpoint."""
    return f"/users/{username}"


def user_repositories(username: str) -> str:
    """Return user repositories endpoint."""
    return f"/users/{username}/repos"


def user_starred_repositories(username: str) -> str:
    """Return user starred repositories endpoint."""
    return f"/users/{username}/starred"