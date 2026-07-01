from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project_repository_contributor import (
        GitlabRestProjectRepositoryContributor,
    )


class GitlabRestProjectRepositoryContributorReference(ModelClassReference["GitlabRestProjectRepositoryContributor"]):
    """Reference to GitlabRestProjectRepositoryContributor model."""

    def get_model_class(self) -> type["GitlabRestProjectRepositoryContributor"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project_repository_contributor

        return gitlab_rest_project_repository_contributor.GitlabRestProjectRepositoryContributor
