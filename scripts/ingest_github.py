# scripts/ingest_github.py

import logging

from src.gitrec.config.settings import get_settings
from src.gitrec.ingestion.github.client import GitHubClient
from src.gitrec.ingestion.github.loader import (
    GitHubLoader,
    RepositoryLoader,
    ResourceLoader,
    UserLoader,
)
from src.gitrec.ingestion.github.search import GitHubSearch 
from src.gitrec.ingestion.service import IngestionService
from src.gitrec.persistence.postgres.connection import PostgresConnection
from src.gitrec.persistence.service import PersistenceService


logger = logging.getLogger(__name__)


def main() -> None:
    """Execute GitHub ingestion and persist results to PostgreSQL."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

    settings = get_settings()

    # Phase 1: Ingest GitHub data.
    logger.info("Starting GitHub ingestion")

    with GitHubClient(settings=settings) as github_client:
        github_search = GitHubSearch(client=github_client)

        resource_loader = ResourceLoader(client=github_client)

        repository_loader = RepositoryLoader(
            resource_loader=resource_loader,
        )

        user_loader = UserLoader(
            resource_loader=resource_loader,
        )

        github_loader = GitHubLoader(
            repo_loader=repository_loader,
            user_loader=user_loader,
        )

        ingestion_service = IngestionService(
            github_search=github_search,
            github_loader=github_loader,
            test_limit=3,
        )

        result = ingestion_service.run()

    logger.info(
        "GitHub ingestion completed: %d repositories, %d users",
        len(result.repositories),
        len(result.users),
    )

    # Phase 2: Persist ingested data.
    logger.info("Starting PostgreSQL persistence")

    with PostgresConnection(settings=settings) as postgres_connection:
        persistence_service = PersistenceService(
            connection=postgres_connection,
        )

        persistence_service.persist(
            repositories=result.repositories,
            users=result.users,
        )

    logger.info("PostgreSQL persistence completed successfully")


if __name__ == "__main__":
    main()
