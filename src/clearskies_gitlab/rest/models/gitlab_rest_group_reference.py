from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_group import GitlabRestGroup


class GitlabRestGroupReference(ModelClassReference["GitlabRestGroup"]):
    """Reference to GitlabRestGroup model."""

    def get_model_class(self) -> type["GitlabRestGroup"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_group

        return gitlab_rest_group.GitlabRestGroup
