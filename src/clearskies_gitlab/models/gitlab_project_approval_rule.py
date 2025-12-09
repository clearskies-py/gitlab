from __future__ import annotations

from clearskies import Model
from clearskies.columns import Boolean, Integer, Select, String


class GitlabProjectApprovalRule(Model):
    """Base model for namespaces."""

    id_column_name = "id"

    name = String()
    id = Integer()
    type = Select(allowed_values=["regular", "code_owner", "report_approver"])
    approvals_required = Integer()
    applies_to_all_protected_branches = Boolean()
