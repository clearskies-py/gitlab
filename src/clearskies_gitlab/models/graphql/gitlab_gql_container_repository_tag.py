from clearskies import Model
from clearskies.columns import BelongsToId, Datetime, String

from clearskies_gitlab.models.graphql import gitlab_gql_container_repository


class GitlabGqlContainerRepositoryTag(Model):
    """Model for gitlab container repositories via GQL."""

    id_column_name: str = "name"
    root_list = False

    @classmethod
    def destination_name(cls) -> str:
        """Return the slug of the api endpoint for this model."""
        return "tag"

    name = String()
    digest = String()
    location = String()
    path = String()
    created_at = Datetime()
    published_at = Datetime()
    container_repository_id = BelongsToId(gitlab_gql_container_repository.GitlabGqlContainerRepository)
    container_repository = BelongsToId(gitlab_gql_container_repository.GitlabGqlContainerRepository)
