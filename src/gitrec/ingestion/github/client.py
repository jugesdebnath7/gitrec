# src/gitrec/ingestion/github/client.py

import logging
from types import TracebackType
from typing import Any, Literal, Self

import httpx

from src.gitrec.config.settings import Settings
from src.gitrec.core.exceptions import (
    APITimeoutError,
    GitHubAPIError,
    NetworkError,
    NotFoundError,
    RateLimitError,
)


logger = logging.getLogger(__name__)


JSON = (
    dict[str, Any]
    | list[Any]
    | str
    | int
    | float
    | bool
    | None
)

HTTPMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


class GitHubClient:
    """
    HTTP client wrapper for interacting with the GitHub REST API.

    This client is responsible for:
        - Managing the underlying HTTP connection.
        - Applying GitHub-specific request headers.
        - Injecting authentication when configured.
        - Translating HTTP/network failures into application exceptions.
        - Handling GitHub-specific responses such as rate limits.

    The client supports context manager usage:

        with GitHubClient(settings) as client:
            repositories = client.get("/user/repos")
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initialize the GitHub API client.

        Args:
            settings: Application configuration containing GitHub,
                HTTP, and authentication settings.
        """
        self._settings = settings

        self._client = httpx.Client(
            base_url=str(self._settings.github.base_url),
            headers=self._headers(),
            follow_redirects=True,
            timeout=self._settings.http.timeout,
            transport=self._create_transport(),
        )

        logger.debug("Initialized GitHub REST API client.")

    def _headers(self) -> dict[str, str]:
        """
        Build default HTTP headers for GitHub API requests.

        Returns:
            Dictionary containing API version, accepted content type,
            user agent, and optional authentication token.
        """
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": self._settings.http.user_agent,
            "X-GitHub-Api-Version": "2022-11-28",
        }

        token = self._settings.github.token_value

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return headers

    def _create_transport(self) -> httpx.HTTPTransport:
        return httpx.HTTPTransport(
            retries=self._settings.http.retries
        )

    def _request(
        self,
        method: HTTPMethod,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute an HTTP request against GitHub.

        Args:
            method: HTTP method to execute.
            url: API endpoint path.
            **kwargs: Additional arguments forwarded to httpx.

        Returns:
            Parsed JSON response.

        Raises:
            APITimeoutError: When the request exceeds the configured timeout.
            NetworkError: When a network-level failure occurs.
            RateLimitError: When GitHub API rate limits are exhausted.
            NotFoundError: When the requested resource does not exist.
            GitHubAPIError: For other GitHub HTTP errors or invalid responses.
        """
        try:
            response = self._client.request(
                method,
                url,
                **kwargs,
            )
    
        except httpx.TimeoutException as exc:
            logger.warning(
                "GitHub request timed out: %s %s",
                method,
                url,
            )
            raise APITimeoutError() from exc

        except httpx.NetworkError as exc:
            logger.error(
                "GitHub network error: %s %s",
                method,
                url,
            )
            raise NetworkError() from exc

        if response.status_code in (
            httpx.codes.FORBIDDEN, 
            httpx.codes.TOO_MANY_REQUESTS,
            ):
            remaining = response.headers.get("X-RateLimit-Remaining")
            retry_after = response.headers.get("Retry-After")

            if remaining == "0":
                reset = response.headers.get(
                    "X-RateLimit-Reset"
                )
                logger.warning(
                    "GitHub API rate limit exceeded. Reset timestamp: %s",
                    reset,
                )
                raise RateLimitError(reset)

            if retry_after is not None:
                raise RateLimitError(retry_after)
        
        try:
            response.raise_for_status()

        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code

            logger.error(
                "GitHub API request failed: %s %s returned %s: %s",
                method,
                url,
                status_code,
                response.text,
            )

            if status_code == httpx.codes.NOT_FOUND:
                raise NotFoundError(
                    resource=url,
                ) from exc

            raise GitHubAPIError(
                status_code=status_code,
                message=f"GitHub API request failed with status {status_code}"

            ) from exc

        if response.status_code == httpx.codes.NO_CONTENT:
            return None

        try:
            return response.json()
        except ValueError as exc:
            raise GitHubAPIError(
                status_code=response.status_code,
                message="GitHub returned invalid JSON response.",
            ) from exc

    def get(
        self,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute a GET request.

        Args:
            url: API endpoint path.
            **kwargs: Additional httpx request arguments.

        Returns:
            Parsed JSON response.
        """
        return self._request(
            method="GET",
            url=url,
            **kwargs,
        )

    def post(
        self,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute a POST request.

        Args:
            url: API endpoint path.
            **kwargs: Additional httpx request arguments.

        Returns:
            Parsed JSON response.
        """
        return self._request(
            method="POST",
            url=url,
            **kwargs,
        )

    def patch(
        self,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute a PATCH request.

        Args:
            url: API endpoint path.
            **kwargs: Additional httpx request arguments.

        Returns:
            Parsed JSON response.
        """
        return self._request(
            method="PATCH",
            url=url,
            **kwargs,
        )

    def put(
        self,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute a PUT request.

        Args:
            url: API endpoint path.
            **kwargs: Additional httpx request arguments.

        Returns:
            Parsed JSON response.
        """
        return self._request(
            method="PUT",
            url=url,
            **kwargs,
        )

    def delete(
        self,
        url: str,
        **kwargs: Any,
    ) -> JSON:
        """
        Execute a DELETE request.

        Args:
            url: API endpoint path.
            **kwargs: Additional httpx request arguments.

        Returns:
            Parsed JSON response.
        """
        return self._request(
            method="DELETE",
            url=url,
            **kwargs,
        )

    def close(self) -> None:
        """
        Close the underlying HTTP connection pool.
        """
        self._client.close()
        logger.debug("GitHub client connection closed.")

    def __enter__(self) -> Self:
        """
        Support context manager usage.

        Returns:
            The initialized GitHub client instance.
        """
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """
        Close resources when leaving a context manager block.
        """
        self.close()