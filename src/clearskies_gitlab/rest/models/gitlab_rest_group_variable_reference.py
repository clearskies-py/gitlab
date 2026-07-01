from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_group_variable import (
        GitlabRestGroupVariable,
    )


class GitlabRestGroupVariableReference(ModelClassReference["GitlabRestGroupVariable"]):
    """Reference to GitlabRestGroupVariable model."""

    def get_model_class(self) -> type["GitlabRestGroupVariable"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_group_variable

        return gitlab_rest_group_variable.GitlabRestGroupVariable
