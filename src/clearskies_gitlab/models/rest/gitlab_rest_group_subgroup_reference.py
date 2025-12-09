from clearskies_gitlab.models.rest import gitlab_rest_group_subgroup


class GitlabRestGroupSubgroupReference:
    """Reference to GitlabRestGroupSubgroup model."""

    def get_model_class(self) -> type:
        """Return the model class this reference points to."""
        return gitlab_rest_group_subgroup.GitlabRestGroupSubgroup
