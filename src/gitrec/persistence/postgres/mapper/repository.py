# scr/gitrec/persistence/postgres/mapper/repository.py

"""Map repository aggregates into database-ready records."""

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.repository_item import RepositoryItem


Record = dict[str, Any]
Records = dict[str, list[Record]]


class RepositoryMapper:
    """Flatten repository aggregates into table-specific record groups."""

    def flatten(
        self,
        repositories: list[RepositoryItem],
    ) -> Records:
        """Convert repositories and nested resources into database-ready records.

        Args:
            repositories: Repository aggregates to flatten.

        Returns:
            A dictionary containing one list per persistence resource.

        Raises:
            TypeError: If repositories is not a list of RepositoryItem instances.
        """
        self._validate_repositories(repositories)

        records: Records = {
            "repositories": [],
            "branches": [],
            "commits": [],
            "contributors": [],
            "forks": [],
            "issues": [],
            "languages": [],
            "pull_requests": [],
            "readme": [],
            "releases": [],
            "tags": [],
            "topics": [],
        }

        for repository in repositories:
            records["repositories"].append(
                self._map_repository(repository)
            )

            records["branches"].extend(
                self._map_branches(repository)
            )

            records["commits"].extend(
                self._map_commits(repository)
            )

            records["contributors"].extend(
                self._map_contributors(repository)
            )

            records["forks"].extend(
                self._map_forks(repository)
            )

            records["issues"].extend(
                self._map_issues(repository)
            )

            records["languages"].extend(
                self._map_languages(repository)
            )

            records["pull_requests"].extend(
                self._map_pull_requests(repository)
            )

            records["readme"].extend(
                self._map_readme(repository)
            )

            records["releases"].extend(
                self._map_releases(repository)
            )

            records["tags"].extend(
                self._map_tags(repository)
            )

            records["topics"].extend(
                self._map_topics(repository)
            )

        return records

    @staticmethod
    def _validate_repositories(repositories: list[RepositoryItem]) -> None:
        """Validate that the input is a list of RepositoryItem instances."""
        if not isinstance(repositories, list):
            raise TypeError(
                "Expected a list of RepositoryItem instances, "
                f"got {type(repositories).__name__}."
            )
            
        for index, repository in enumerate(repositories):
            if not isinstance(repository, RepositoryItem):
                raise TypeError(
                    f"Expected RepositoryItem at index {index}, "
                    f"got {type(repository).__name__}."
                )


    @staticmethod
    def _map_repository(repository: RepositoryItem) -> Record:
        """Map core repository metadata."""
        return {
            "id": repository.id,
            "owner": repository.owner,
            "name": repository.name,
            "full_name": repository.full_name,
            "description": repository.description,
            "visibility": repository.visibility,
            "default_branch": repository.default_branch,
            "language": repository.language,
            "stars_count": repository.stars_count,
            "forks_count": repository.forks_count,
            "watchers_count": repository.watchers_count,
            "open_issues_count": repository.open_issues_count,
            "fork": repository.fork,
            "archived": repository.archived,
            "disabled": repository.disabled,
        }

    @staticmethod
    def _map_branches(repository: RepositoryItem) -> list[Record]:
        """Map a repository's branches."""
        return [
            {
                "repo_id": branch.repo_id,
                "name": branch.name,
                "commit_sha": branch.commit_sha,
                "protected": branch.protected,
            }
            for branch in repository.branches
        ]

    @staticmethod
    def _map_commits(repository: RepositoryItem) -> list[Record]:
        """Map a repository's commits."""
        return [
            {
                "sha": commit.sha,
                "repo_id": commit.repo_id,
                "message": commit.message,
                "author_id": commit.author_id,
                "author_login": commit.author_login,
                "committer_id": commit.committer_id,
                "committer_login": commit.committer_login,
                "authored_at": commit.authored_at,
                "committed_at": commit.committed_at,
                "html_url": commit.html_url,
            }
            for commit in repository.commits
        ]
    
    @staticmethod
    def _map_contributors(repository: RepositoryItem) -> list[Record]:
        """Map a repository's contributors."""
        return [
            {
                "repo_id": contributor.repo_id,
                "user_id": contributor.user_id,
                "login": contributor.login,
                "contributions": contributor.contributions,
                "type": contributor.type,
            }
            for contributor in repository.contributors
        ]

    @staticmethod
    def _map_forks(repository: RepositoryItem) -> list[Record]:
        """Map a repository's forks."""
        return [
            {
                "repo_id": fork.repo_id,
                "fork_id": fork.fork_id,
                "owner_id": fork.owner_id,
                "owner_login": fork.owner_login,
                "created_at": fork.created_at,
            }
            for fork in repository.forks
        ]

    @staticmethod
    def _map_issues(repository: RepositoryItem) -> list[Record]:
        """Map a repository's issues."""
        return [
            {
                "id": issue.id,
                "number": issue.number,
                "repo_id": issue.repo_id,
                "title": issue.title,
                "body": issue.body,
                "state": issue.state,
                "user_id": issue.user_id,
                "user_login": issue.user_login,
                "created_at": issue.created_at,
                "updated_at": issue.updated_at,
                "closed_at": issue.closed_at,
                "comments": issue.comments,
                "html_url": issue.html_url,
            }
            for issue in repository.issues
        ]

    @staticmethod
    def _map_languages(repository: RepositoryItem) -> list[Record]:
        """Map a repository's languages."""
        return [
            {
                "repo_id": language.repo_id,
                "language": language.language,
            }
            for language in repository.languages
        ]

    @staticmethod
    def _map_pull_requests(repository: RepositoryItem) -> list[Record]:
        """Map a repository's pull requests."""
        return [
            {
                "id": pull_request.id,
                "number": pull_request.number,
                "repo_id": pull_request.repo_id,
                "title": pull_request.title,
                "body": pull_request.body,
                "state": pull_request.state,
                "user_id": pull_request.user_id,
                "user_login": pull_request.user_login,
                "created_at": pull_request.created_at,
                "updated_at": pull_request.updated_at,
                "closed_at": pull_request.closed_at,
                "merged_at": pull_request.merged_at,
                "html_url": pull_request.html_url,
            }
            for pull_request in repository.pull_requests
        ]

    @staticmethod
    def _map_readme(repository: RepositoryItem) -> list[Record]:
        """Map the optional repository README."""
        if repository.readme is None:
            return []
        readme = repository.readme

        return [
            {
                "repo_id": readme.repo_id,
                "content": readme.content,
            }
        ]

    @staticmethod
    def _map_releases(repository: RepositoryItem) -> list[Record]:
        """Map a repository's releases."""
        return [
            {
                "id": release.id,
                "repo_id": release.repo_id,
                "tag_name": release.tag_name,
                "name": release.name,
                "body": release.body,
                "draft": release.draft,
                "prerelease": release.prerelease,
                "author_id": release.author_id,
                "author_login": release.author_login,
                "created_at": release.created_at,
                "published_at": release.published_at,
                "html_url": release.html_url,
            }
            for release in repository.releases
        ]

    @staticmethod
    def _map_tags(repository: RepositoryItem) -> list[Record]:
        """Map a repository's tags."""
        return [
            {
                "repo_id": tag.repo_id,
                "tag_name": tag.tag_name,
                "commit_sha": tag.commit_sha,
                "created_at": tag.created_at,
            }
            for tag in repository.tags
        ]

    @staticmethod
    def _map_topics(repository: RepositoryItem) -> list[Record]:
        """Map a repository's topics."""
        return [
            {
                "repo_id": topic.repo_id,
                "topic": topic.topic,
            }
            for topic in repository.topics
        ]
        
