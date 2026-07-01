from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project_member import (
        GitlabRestProjectMember,
    )


class GitlabRestProjectMemberReference(ModelClassReference["GitlabRestProjectMember"]):
    """Reference to GitlabRestProjectMember model."""

    def get_model_class(self) -> type["GitlabRestProjectMember"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project_member

        return gitlab_rest_project_member.GitlabRestProjectMember
