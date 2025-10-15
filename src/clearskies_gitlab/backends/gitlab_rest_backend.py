from __future__ import annotations

import logging
import urllib
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, cast

import requests
from clearskies import Model, configs
from clearskies.backends import ApiBackend
from clearskies.decorators import parameters_to_properties
from clearskies.di import inject
from clearskies.query import Query
from requests.structures import CaseInsensitiveDict

from clearskies_gitlab.exceptions import gitlab_error

if TYPE_CHECKING:
    from clearskies import model
    from clearskies.authentication import Authentication
    from clearskies.query import Query


class GitlabRestBackend(ApiBackend):
    """Backend for Gitlab.com."""

    base_url = inject.ByName("gitlab_url", cache=True)
    authentication = inject.ByName("gitlab_auth", cache=False)
    requests = inject.Requests()
    _auth_headers: dict[str, str] = {}

    @parameters_to_properties
    def __init__(
        self,
        base_url: str = "",
        authentication: Authentication | None = None,
        model_casing: str = "snake_case",
        api_casing: str = "snake_case",
        api_to_model_map: dict[str, str] = {},
        pagination_parameter_name: str = "page",
        pagination_parameter_type: str = "int",
        limit_parameter_name: str = "per_page",
    ) -> None:
        """Setups the class."""
        self.finalize_and_validate_configuration()
        self.logger = logging.getLogger(__name__)

    def count_method(self, query: Query) -> str:
        """Return the request method to use when making a request for a record count."""
        return "HEAD"

    def count(self, query: Query) -> int:
        """Return the count of records matching the query."""
        self.check_query(query)
        (url, method, body, headers) = self.build_records_request(query)
        response = self.execute_request(url, self.count_method(query), json=body, headers=headers)
        return self._map_count_response(response.headers)

    def _map_count_response(self, headers: CaseInsensitiveDict[str]) -> int:
        return int(headers.get("x-total", 0))

    def set_next_page_data_from_response(
        self,
        next_page_data: dict[str, Any],
        query: Query,
        response: requests.Response,  # type: ignore
    ) -> None:
        """
        Update the next_page_data dictionary with the appropriate data needed to fetch the next page of records.

        This method has a very important job, which is to inform clearskies about how to make another API call to fetch the next
        page of records.  The way this happens is by updating the `next_page_data` dictionary in place with whatever pagination
        information is necessary.  Note that this relies on next_page_data being passed by reference, hence the need to update
        it in place.  That means that you can do this:

        ```python
        next_page_data["some_key"] = "some_value"
        ```

        but if you do this:

        ```python
        next_page_data = {"some_key": "some_value"}
        ```

        Then things simply won't work.
        """
        # Different APIs generally have completely different ways of communicating pagination data, but one somewhat common
        # approach is to use a link header, so let's support that in the base class.
        if "link" not in response.headers:
            return
        next_link = [rel for rel in response.headers["link"].split(",") if 'rel="next"' in rel]
        if not next_link:
            return
        parsed_next_link = urllib.parse.urlparse(next_link[0].split(";")[0].strip(" <>"))
        query_parameters = urllib.parse.parse_qs(parsed_next_link.query)
        if self.pagination_parameter_name not in query_parameters:
            raise ValueError(
                f"Configuration error with {self.__class__.__name__}!  I am configured to expect a pagination key of '{self.pagination_parameter_name}.  However, when I was parsing the next link from a response to get the next pagination details, I could not find the designated pagination key.  This likely means that backend.pagination_parameter_name is set to the wrong value.  The link in question was "
                + parsed_next_link.geturl()
            )
        next_page_data[self.pagination_parameter_name] = query_parameters[self.pagination_parameter_name][0]
