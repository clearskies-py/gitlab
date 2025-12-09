from clearskies_gitlab.models.rest import gitlab_rest_project_variable


class GitlabRestProjectVariableReference:
    """Reference to GitlabRestProjectVariable model."""

    def get_model_class(self) -> type:
        """Return the model class this reference points to."""
        return gitlab_rest_project_variable.GitlabRestProjectVariable
