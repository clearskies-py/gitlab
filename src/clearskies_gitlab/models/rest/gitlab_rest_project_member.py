from __future__ import annotations

from typing import Self

from clearskies.columns import Boolean, Json, String

from clearskies_gitlab.models import gitlab_member, gitlab_rest_model


class GitlabRestProjectMember(
    gitlab_rest_model.GitlabRestModel,
    gitlab_member.GitlabMember,
):
    """Model for project members."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "projects/:project_id/members"

    project_id = String()
    query = String()
    user_ids = Json()
    skip_users = Json()
    show_seat_info = Boolean()
    all = Boolean()
