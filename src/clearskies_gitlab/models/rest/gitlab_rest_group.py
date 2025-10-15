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


class GitlabRestGroup(
    gitlab_rest_model.GitlabRestModel,
    gitlab_group.GitlabGroup,
):
    """Model for groups."""

    @classmethod
    def destination_name(cls: type[Self]) -> str:
        """Return the slug of the api endpoint for this model."""
        return "groups"

    projects = HasMany(
        gitlab_rest_project_reference.GitlabRestProjectReference,
        foreign_column_name="group_id",
    )
    access_tokens = HasMany(
        gitlab_rest_group_access_token.GitlabRestGroupAccessToken,
        foreign_column_name="group_id",
    )
    variables = HasMany(
        gitlab_rest_group_variable.GitlabRestGroupVariable,
        foreign_column_name="group_id",
    )
    subgroups = HasMany(
        gitlab_rest_group_subgroup_reference.GitlabRestGroupSubgroupReference,
        foreign_column_name="group_id",
    )
    parent_id = BelongsToSelf()
    parent = BelongsToModel("parent_id")
    ### Search params
    skip_groups = Json()
    all_available = Boolean()
    search = String()
    order_by = String()
    sort = String()
    visibility = Select(allowed_values=["public", "internal", "private"])
    with_custom_attributes = Boolean()
    owned = Boolean()
    min_access_level = Integer()
    top_level_only = Boolean()
    repository_storage = String()
    marked_for_deletion_on = Datetime(date_format="%Y-%m-%d")

    @property
    def query_configuration(self: Self) -> dict[str, Any]:
        """Set query configuration parameters."""
        query_configuration: dict[str, Any] = super().query_configuration
        pagination = query_configuration.get("pagination", {})
        query_configuration["pagination"] = {**pagination, **{"type": "keyset"}}
        return query_configuration

    @query_configuration.setter
    def query_configuration(self: Self, configuration: dict[str, Any]) -> None:
        self.query_wheres = configuration["wheres"]
        self.query_sorts = configuration["sorts"]
        self.query_group_by_column = configuration["group_by_column"]
        self.query_joins = configuration["joins"]
        self.query_limit = configuration["limit"]
        self.query_pagination = {**configuration["pagination"], **{"type": "keyset"}}
        self.query_selects = configuration["selects"]
        self.query_select_all = configuration["select_all"]
        self._model_columns = configuration["model_columns"]
