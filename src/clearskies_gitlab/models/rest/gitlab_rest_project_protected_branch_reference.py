from clearskies_gitlab.models.rest import gitlab_rest_project_protected_branch


class GitlabRestProjectProtectedBranchReference:
    """Reference to GitlabRestProjectProtectedBranch model."""

    def get_model_class(self) -> type:
        """Return the model class this reference points to."""
        return gitlab_rest_project_protected_branch.GitlabRestProjectProtectedBranch
