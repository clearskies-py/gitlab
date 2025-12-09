from __future__ import annotations

from typing import Self

from clearskies_gitlab.models import gitlab_project, gitlab_rest_model


class GitlabRestGroupProject(
    gitlab_rest_model.GitlabRestModel,
    gitlab_project.GitlabProject,
):
    """Model for groups projects."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "groups/:group_id/projects"
