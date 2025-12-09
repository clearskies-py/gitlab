from __future__ import annotations

from clearskies_gitlab import models


class GitlabGqlGroup(models.GitlabGqlModel, models.GitlabGroup):
    """Model for gitlab projects via GQL."""

    gitlab_id_pattern: str = "gid://gitlab/Group/[ID]"
    id_column_name: str = "id"
    root_list = True

    @classmethod
    def destination_name(cls) -> str:
        """Return the slug of the api endpoint for this model."""
        return "group"
