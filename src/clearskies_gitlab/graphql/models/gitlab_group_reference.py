from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.graphql.models.gitlab_group import GitlabGroup


class GitlabGroupReference(ModelClassReference["GitlabGroup"]):
    """Reference to GitlabGroup model."""

    def get_model_class(self) -> type["GitlabGroup"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.graphql.models import gitlab_group

        return gitlab_group.GitlabGroup
