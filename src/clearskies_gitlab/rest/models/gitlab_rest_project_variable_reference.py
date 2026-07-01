from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_project_variable import (
        GitlabRestProjectVariable,
    )


class GitlabRestProjectVariableReference(ModelClassReference["GitlabRestProjectVariable"]):
    """Reference to GitlabRestProjectVariable model."""

    def get_model_class(self) -> type["GitlabRestProjectVariable"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_project_variable

        return gitlab_rest_project_variable.GitlabRestProjectVariable
