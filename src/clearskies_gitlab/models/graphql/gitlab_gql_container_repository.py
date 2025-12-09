from clearskies import Model
from clearskies.columns import BelongsToId, Datetime, HasMany, String

from clearskies_gitlab.models.graphql import gitlab_gql_container_repository_tag, gitlab_gql_project


class GitlabGqlContainerRepository(Model):
    """Model for gitlab container repositories via GQL."""

    gitlab_id_pattern: str = "gid://gitlab/ContainerRepository/[ID]"
    id_column_name: str = "id"
    root_list = False

    @classmethod
    def destination_name(cls) -> str:
        """Return the slug of the api endpoint for this model."""
        return "containerRepository"

    name = String()
    location = String()
    path = String()
    created_at = Datetime()
    project_id = BelongsToId(gitlab_gql_project.GitlabGqlProject)
    project = BelongsToId(gitlab_gql_project.GitlabGqlProject)
    tags = HasMany(
        gitlab_gql_container_repository_tag.GitlabGqlContainerRepositoryTag,
        foreign_column_name="containerRepositoryId",
    )
