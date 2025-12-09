from __future__ import annotations

from clearskies import Model
from clearskies.columns import Boolean, Integer, Json, String


class GitlabBranchProtection(Model):
    """Model for GitLab branch protections."""

    id_column_name = "id"

    id = Integer()
    name = String()
    allow_force_push = Boolean()
    code_owner_approval_required = Boolean()
    merge_access_levels = Json()
    push_access_levels = Json()
    unprotect_access_levels = Json()
