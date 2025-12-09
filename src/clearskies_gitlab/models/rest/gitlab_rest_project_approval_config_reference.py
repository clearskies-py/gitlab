from clearskies_gitlab.models.rest import gitlab_rest_project_approval_config


class GitlabRestProjectApprovalConfigReference:
    """Reference to GitlabRestProjectApprovalConfig model."""

    def get_model_class(self) -> type:
        """Return the model class this reference points to."""
        return gitlab_rest_project_approval_config.GitlabRestProjectApprovalConfig
