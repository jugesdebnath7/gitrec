# src/gitrec/domain/mapper/user/organization_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.organization_item import OrganizationItem


class OrganizationMapper:
    """
    Maps GitHub organization responses into domain organization entities.
    """

    @staticmethod
    def to_organization_item(data: dict[str, Any]) -> OrganizationItem:
        """
        Convert a GitHub organization response into an OrganizationItem.

        Args:
            data: Raw organization data returned by the GitHub API.

        Returns:
            An OrganizationItem representing the GitHub organization.
        """
        return OrganizationItem(
            login=data["login"],
            id=data["id"],
            node_id=data["node_id"],
            avatar_url=data["avatar_url"],
            gravatar_id=data["gravatar_id"],
            url=data["url"],
            html_url=data["html_url"],
        )