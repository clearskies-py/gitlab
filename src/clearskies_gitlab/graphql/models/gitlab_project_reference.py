from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.graphql.models.gitlab_project import GitlabProject


class GitlabProjectReference(ModelClassReference["GitlabProject"]):
    """Reference to GitlabProject model."""

    def get_model_class(self) -> type["GitlabProject"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.graphql.models import gitlab_project

        return gitlab_project.GitlabProject
