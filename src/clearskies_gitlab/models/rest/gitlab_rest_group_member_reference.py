from clearskies_gitlab.models.rest import gitlab_rest_group_member


class GitlabRestGroupMemberReference:
    """Reference to GitlabRestGroupMember model."""

    def get_model_class(self) -> type:
        """Return the model class this reference points to."""
        return gitlab_rest_group_member.GitlabRestGroupMember
