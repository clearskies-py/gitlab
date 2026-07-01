from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_group_access_token import (
        GitlabRestGroupAccessToken,
    )


class GitlabRestGroupAccessTokenReference(ModelClassReference["GitlabRestGroupAccessToken"]):
    """Reference to GitlabRestGroupAccessToken model."""

    def get_model_class(self) -> type["GitlabRestGroupAccessToken"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_group_access_token

        return gitlab_rest_group_access_token.GitlabRestGroupAccessToken
