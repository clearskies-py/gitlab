from __future__ import annotations

from collections import OrderedDict
from typing import Any, Self

from clearskies.columns import (
    BelongsToId,
    BelongsToModel,
    BelongsToSelf,
    Boolean,
    Datetime,
    HasMany,
    Integer,
    Json,
    Select,
    String,
)

from clearskies_gitlab.models import gitlab_group, gitlab_rest_model
from clearskies_gitlab.models.rest import (
    gitlab_rest_group_access_token,
    gitlab_rest_group_subgroup_reference,
    gitlab_rest_group_variable,
    gitlab_rest_project_reference,
)


class GitlabRestGroupSubgroup(gitlab_rest_model.GitlabRestModel, gitlab_group.GitlabGroup):
    """Model for Subgroups."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "groups/:group_id/subgroups"

    group_id = String()
