from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_group_member import (
        GitlabRestGroupMember,
    )


class GitlabRestGroupMemberReference(ModelClassReference["GitlabRestGroupMember"]):
    """Reference to GitlabRestGroupMember model."""

    def get_model_class(self) -> type["GitlabRestGroupMember"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_group_member

        return gitlab_rest_group_member.GitlabRestGroupMember
