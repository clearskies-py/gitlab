from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.graphql.models.gitlab_container_repository_tag import (
        GitlabContainerRepositoryTag,
    )


class GitlabContainerRepositoryTagReference(ModelClassReference["GitlabContainerRepositoryTag"]):
    """Reference to GitlabContainerRepositoryTag model."""

    def get_model_class(self) -> type["GitlabContainerRepositoryTag"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.graphql.models import gitlab_container_repository_tag

        return gitlab_container_repository_tag.GitlabContainerRepositoryTag
