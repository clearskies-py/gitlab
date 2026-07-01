from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.graphql.models.gitlab_container_repository import (
        GitlabContainerRepository,
    )


class GitlabContainerRepositoryReference(ModelClassReference["GitlabContainerRepository"]):
    """Reference to GitlabContainerRepository model."""

    def get_model_class(self) -> type["GitlabContainerRepository"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.graphql.models import gitlab_container_repository

        return gitlab_container_repository.GitlabContainerRepository
