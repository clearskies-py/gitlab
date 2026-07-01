from __future__ import annotations

from typing import TYPE_CHECKING

from clearskies.model import ModelClassReference

if TYPE_CHECKING:
    from clearskies_gitlab.rest.models.gitlab_rest_group_subgroup import (
        GitlabRestGroupSubgroup,
    )


class GitlabRestGroupSubgroupReference(ModelClassReference["GitlabRestGroupSubgroup"]):
    """Reference to GitlabRestGroupSubgroup model."""

    def get_model_class(self) -> type["GitlabRestGroupSubgroup"]:
        """Return the model class this reference points to."""
        from clearskies_gitlab.rest.models import gitlab_rest_group_subgroup

        return gitlab_rest_group_subgroup.GitlabRestGroupSubgroup
