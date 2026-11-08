# src/gitrec/domain/entity/repository/repository_item.py

from __future__ import annotations

from pydantic import BaseModel, Field

from src.gitrec.domain.entity.repository.branch_item import BranchItem
from src.gitrec.domain.entity.repository.commit_item import CommitItem
from src.gitrec.domain.entity.repository.contributor_item import ContributorItem
from src.gitrec.domain.entity.repository.fork_item import ForkItem
from src.gitrec.domain.entity.repository.issue_item import IssueItem
from src.gitrec.domain.entity.repository.language_item import LanguageItem
from src.gitrec.domain.entity.repository.pull_request_item import PullRequestItem
from src.gitrec.domain.entity.repository.readme_item import ReadmeItem
from src.gitrec.domain.entity.repository.release_item import ReleaseItem
from src.gitrec.domain.entity.repository.tag_item import TagItem
from src.gitrec.domain.entity.repository.topic_item import TopicItem

class RepositoryItem(BaseModel):
    """
    Represents a GitHub repository within the GitRec domain.

    RepositoryItem acts as the aggregate root for a repository and
    contains both repository-level metadata and the nested resources
    associated with that repository.

    Attributes:
        id: Unique GitHub repository identifier.
        owner: GitHub login of the repository owner.
        name: Repository name.
        full_name: Full repository name in owner/name format.
        description: Repository description, if available.
        visibility: Repository visibility, if available.
        default_branch: Name of the repository's default branch,
            if available.
        language: Primary programming language of the repository,
            if available.
        stars_count: Number of stars received by the repository.
        forks_count: Number of forks of the repository.
        watchers_count: Number of users watching the repository.
        open_issues_count: Number of open issues associated with the
            repository.
        fork: Whether the repository is a fork.
        archived: Whether the repository has been archived.
        disabled: Whether the repository is disabled.
        branches: Branches belonging to the repository.
        commits: Commits associated with the repository.
        contributors: Contributors associated with the repository.
        forks: Fork repositories associated with the repository.
        issues: Issues associated with the repository.
        languages: Programming languages detected in the repository.
        pull_requests: Pull requests associated with the repository.
        readme: Repository README, if available.
        releases: Releases associated with the repository.
        tags: Tags associated with the repository.
        topics: Topics associated with the repository.
    """

    # Core repository identity
    id: int
    owner: str
    name: str
    full_name: str

    # Repository metadata
    description: str | None = None
    visibility: str | None = None
    default_branch: str | None = None
    language: str | None = None

    # Repository statistics
    stars_count: int = 0
    forks_count: int = 0
    watchers_count: int = 0
    open_issues_count: int = 0

    # Repository state
    fork: bool = False
    archived: bool = False
    disabled: bool = False

    # Nested repository resources
    branches: list[BranchItem] = Field(default_factory=list)
    commits: list[CommitItem] = Field(default_factory=list)
    contributors: list[ContributorItem] = Field(default_factory=list)
    forks: list[ForkItem] = Field(default_factory=list)
    issues: list[IssueItem] = Field(default_factory=list)
    languages: list[LanguageItem] = Field(default_factory=list)
    pull_requests: list[PullRequestItem] = Field(default_factory=list)
    readme: ReadmeItem | None = None
    releases: list[ReleaseItem] = Field(default_factory=list)
    tags: list[TagItem] = Field(default_factory=list)
    topics: list[TopicItem] = Field(default_factory=list)