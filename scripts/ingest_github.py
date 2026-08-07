# scripts/ingest_github.py

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


def main():
    settings = get_settings()

    with GitHubClient(settings=settings) as github_client:
        github_search = GitHubSearch(github_client=github_client)

        resource_loader = ResourceLoader(github_client=github_client)

        repository_loader = RepositoryLoader(resource_loader=resource_loader)
        user_loader = UserLoader(resource_loader=resource_loader)


        github_loader = GitHubLoader(
            repository_loader=repository_loader,
            user_loader=user_loader,
        )

        service = IngestionService(
            github_search=github_search,
            github_loader=github_loader,
        )
        service.run()


if __name__ == "__main__":
    main()