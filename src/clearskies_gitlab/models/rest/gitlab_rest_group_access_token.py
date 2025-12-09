from __future__ import annotations

from typing import Self

from clearskies.columns import Boolean, Datetime, Integer, Json, String

from clearskies_gitlab.models import gitlab_rest_model


class GitlabRestGroupAccessToken(
    gitlab_rest_model.GitlabRestModel,
):
    """Model for groups access tokens."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "groups/:group_id/access_tokens"

    group_id = String()
    id = Integer()
    user_id = Integer()
    name = String()
    created_at = Datetime()
    expires_at = Datetime(date_format="%Y-%m-%d")
    active = Boolean()
    revoked = Boolean()
    access_level = Integer()
    token = String()
    scopes = Json()
