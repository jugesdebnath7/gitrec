# src/gitrec/domain/mapper/repository/repository_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.repository_item import RepositoryItem
from src.gitrec.domain.mapper.repository.branch_mapper import BranchMapper
from src.gitrec.domain.mapper.repository.commit_mapper import CommitMapper
from src.gitrec.domain.mapper.repository.contributor_mapper import ContributorMapper
from src.gitrec.domain.mapper.repository.fork_mapper import ForkMapper
from src.gitrec.domain.mapper.repository.issue_mapper import IssueMapper
from src.gitrec.domain.mapper.repository.language_mapper import LanguageMapper
from src.gitrec.domain.mapper.repository.pull_request_mapper import PullRequestMapper
from src.gitrec.domain.mapper.repository.readme_mapper import ReadmeMapper
from src.gitrec.domain.mapper.repository.release_mapper import ReleaseMapper
from src.gitrec.domain.mapper.repository.tag_mapper import TagMapper
from src.gitrec.domain.mapper.repository.topic_mapper import TopicMapper


class RepositoryMapper:
    """
    Maps a fully loaded GitHub repository resource to a RepositoryItem.

    RepositoryMapper is responsible for assembling the repository aggregate.
    Nested repository resources are delegated to their specialized mappers.
    """

    @staticmethod
    def to_repository_item(resource: dict[str, Any]) -> RepositoryItem:
        """
        Convert a loaded repository resource into a RepositoryItem.

        Args:
            resource: Complete repository resource containing the core
                repository data and any nested resources loaded by the
                ingestion layer.

        Returns:
            A fully mapped RepositoryItem.

        Raises:
            KeyError: If required repository fields are missing.
        """
        repository_data = resource["repository"]
        owner = repository_data.get("owner") or {}

        return RepositoryItem(
            # Core repository data
            id=repository_data["id"],
            owner=owner["login"],
            name=repository_data["name"],
            full_name=repository_data["full_name"],
            description=repository_data.get("description"),
            visibility=repository_data.get("visibility"),
            default_branch=repository_data.get("default_branch"),
            language=repository_data.get("language"),

            stars_count=repository_data.get("stargazers_count", 0),
            forks_count=repository_data.get("forks_count", 0),
            watchers_count=repository_data.get("watchers_count", 0),
            open_issues_count=repository_data.get("open_issues_count", 0),

            fork=repository_data.get("fork", False),
            archived=repository_data.get("archived", False),
            disabled=repository_data.get("disabled", False),

            # Nested repository resources
            branches=[
                BranchMapper.to_branch_item(
                    branch, 
                    repository_data["id"],
                )
                for branch in resource.get("branches", [])
            ],

            commits=[
                CommitMapper.to_commit_item(
                    commit,
                    repository_data["id"],
                )
                for commit in resource.get("commits", [])
            ],

            contributors=[
                ContributorMapper.to_contributor_item(
                    contributor,
                    repository_data["id"],
                )
                for contributor in resource.get("contributors", [])
            ],

            forks=[
                ForkMapper.to_fork_item(
                    fork,
                    repository_data["id"],
                )
                for fork in resource.get("forks", [])
            ],

            issues=[
                IssueMapper.to_issue_item(
                    issue,
                    repository_data["id"],
                )
                for issue in resource.get("issues", [])
            ],

            languages=LanguageMapper.to_language_item(
                resource.get("languages", {}),
                repository_data["id"],
            ),

            pull_requests=[
                PullRequestMapper.to_pull_request_item(
                    pull_request,
                    repository_data["id"],
                )
                for pull_request in resource.get("pull_requests", [])
            ],

            readme=ReadmeMapper.to_readme_item(
                resource.get("readme"), 
                repository_data["id"],
            ),

            releases=[
                ReleaseMapper.to_release_item(
                    release,
                    repository_data["id"],
                )
                for release in resource.get("releases", [])
            ],

            tags=[
                TagMapper.to_tag_item(
                    tag,
                    repository_data["id"],
                    resource.get("created_at", ""),
                )
                for tag in resource.get("tags", [])
            ],

            topics=TopicMapper.to_topic_item(
                resource.get("topics", {}),
                repository_data["id"],
            ),
        )