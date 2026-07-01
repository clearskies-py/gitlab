from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project_protected_branch import (
        GitlabRestProjectProtectedBranch,
    )


class GitlabRestProjectProtectedBranchReference(ModelClassReference["GitlabRestProjectProtectedBranch"]):
    """Reference to GitlabRestProjectProtectedBranch model."""

    def get_model_class(self) -> type["GitlabRestProjectProtectedBranch"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project_protected_branch

        return gitlab_rest_project_protected_branch.GitlabRestProjectProtectedBranch
