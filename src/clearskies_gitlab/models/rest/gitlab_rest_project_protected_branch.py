from __future__ import annotations

from typing import Self

from clearskies.columns import BelongsToId, BelongsToModel

from clearskies_gitlab.models import gitlab_branch_protection, gitlab_rest_model
from clearskies_gitlab.models.rest import gitlab_rest_project_reference


class GitlabRestProjectProtectedBranch(
    gitlab_rest_model.GitlabRestModel,
    gitlab_branch_protection.GitlabBranchProtection,
):
    """Model for gitlab project protected branches."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "projects/:project_id/protected_branches"

    project_id = BelongsToId(gitlab_rest_project_reference.GitlabRestProjectReference)
    project = BelongsToModel("project_id")
