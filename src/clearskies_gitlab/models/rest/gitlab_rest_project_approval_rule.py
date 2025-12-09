from __future__ import annotations

from typing import Self

from clearskies.columns import BelongsToId, BelongsToModel, Boolean, Json

from clearskies_gitlab.models import gitlab_project_approval_rule, gitlab_rest_model
from clearskies_gitlab.models.rest import gitlab_rest_project_reference


class GitlabRestProjectApprovalRule(
    gitlab_rest_model.GitlabRestModel,
    gitlab_project_approval_rule.GitlabProjectApprovalRule,
):
    """Model for gitlab project protected branches."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "projects/:project_id/approval_rules"

    project_id = BelongsToId(gitlab_rest_project_reference.GitlabRestProjectReference)
    project = BelongsToModel("project_id")

    eligible_approvers = Json()
    users = Json()
    groups = Json()
    protected_branches = Json()
    contains_hidden_groups = Boolean()
