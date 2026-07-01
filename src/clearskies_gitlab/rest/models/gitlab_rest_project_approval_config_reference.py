from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project_approval_config import (
        GitlabRestProjectApprovalConfig,
    )


class GitlabRestProjectApprovalConfigReference(ModelClassReference["GitlabRestProjectApprovalConfig"]):
    """Reference to GitlabRestProjectApprovalConfig model."""

    def get_model_class(self) -> type["GitlabRestProjectApprovalConfig"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project_approval_config

        return gitlab_rest_project_approval_config.GitlabRestProjectApprovalConfig
