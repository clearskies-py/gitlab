from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project import GitlabRestProject


class GitlabRestProjectReference(ModelClassReference["GitlabRestProject"]):
    """Reference to GitlabRestProject model."""

    def get_model_class(self) -> type["GitlabRestProject"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project

        return gitlab_rest_project.GitlabRestProject
