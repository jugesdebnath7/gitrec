# src/gitrec/core/exceptions.py

from typing import Any, Optional


class GitRecError(Exception):
    """
    Base exception for the GitRec project.

    All custom exceptions should inherit from this.
    """
    def __init__(
            self, 
            message: str, 
            *,
            code: Optional[str] = None,
            details: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    def __str__(self) -> str:
        return f"{self.message} (code={self.code}, details={self.details})"   


# ---------------------------
# External API (GitHub, etc.)
# ---------------------------

class ExternalAPIError(GitRecError):
    """Base class for all external API related errors."""
    pass


class RateLimitError(ExternalAPIError):
    """Raised when API rate limit is exceeded."""
    def __init__(
            self, 
            reset_time: Optional[float] = None, 
            **kwargs,
    ) -> None: 
        super().__init__(
           message="GitHub API rate limit exceeded", 
           code="RATE_LIMIT_EXCEEDED", 
           details={"reset_time": reset_time},
           **kwargs,
        )


class NotFoundError(ExternalAPIError):
    """Raised when a resource is not found (404)."""
    def __init__(
            self,
            resource: Optional[str] = None,
            **kwargs,
    ) -> None:
        super().__init__(
            message=f"{resource or 'Resource'} not found",
            code="NOT_FOUND", 
            details={"resource": resource}, 
            **kwargs,
        )


class APITimeoutError(ExternalAPIError):
    """Raised when request times out."""
    def __init__(self, **kwargs) -> None:
        super().__init__(
            message="GitHub API request timed out", 
            code="TIMEOUT", 
            **kwargs,
        )


class NetworkError(ExternalAPIError):
    """Raised for network-related issues."""
    def __init__(self, **kwargs) -> None:
        super().__init__(
            message="Network error while calling GitHub API",
            code="NETWORK_ERROR", 
            **kwargs,
        )        


class GitHubAPIError(ExternalAPIError):
    """
    Raised for GitHub API HTTP errors that are not handled
    by a more specific exception.
    """

    def __init__(
        self,
        status_code: int,
        message: str = "GitHub API request failed",
        **kwargs,
    ) -> None:
        super().__init__(
            message=message,
            code="GITHUB_API_ERROR",
            details={"status_code": status_code},
            **kwargs,
        )
