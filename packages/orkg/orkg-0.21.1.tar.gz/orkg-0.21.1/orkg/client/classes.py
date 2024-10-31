from typing import Dict, Optional

from deprecated import deprecated

from orkg.out import OrkgResponse, OrkgUnpaginatedResponse
from orkg.utils import NamespacedClient, dict_to_url_params, query_params


class ClassesClient(NamespacedClient):
    def by_id(self, id: str) -> OrkgResponse:
        self.client.backend._append_slash = True
        response = self.client.backend.classes(id).GET()
        return self.client.wrap_response(response)

    @query_params("q", "exact")
    def get_all(self, params: Optional[Dict] = None) -> OrkgResponse:
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.classes.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.classes.GET()
        return self.client.wrap_response(response)

    @query_params("page", "size", "sort", "desc", "q", "exact")
    @deprecated(
        reason="This method is deprecated, use orkg.resources.get instead",
        version="0.21.0",
    )
    def get_resource_by_class(
        self, class_id: str, params: Optional[Dict] = None
    ) -> OrkgResponse:
        params.update({"include": class_id})
        return self.client.resources.get(params=params)

    @query_params("page", "size", "sort", "desc", "q", "exact")
    @deprecated(
        reason="This method is deprecated, use orkg.resources.get_unpaginated instead",
        version="0.21.0",
    )
    def get_resource_by_class_unpaginated(
        self,
        class_id: str,
        start_page: int = 0,
        end_page: int = -1,
        params: Optional[Dict] = None,
    ) -> OrkgUnpaginatedResponse:
        """
        Get a list of resources based on a class identifier without pagination, with support for query parameters.

        :param class_id: the class ID to filter on
        :param q: search term of the label of the resource (optional)
        :param exact: whether to check for the exact search term or not (optional) -> bool
        :param page: the page number (optional)
        :param size: number of items per page (optional)
        :param sort: key to sort on (optional)
        :param desc: true/false to sort desc (optional)
        :param start_page: page to start from. Defaults to 0 (optional)
        :param end_page: page to stop at. Defaults to -1 meaning non-stop (optional)
        :return: An OrkgUnpaginatedResponse object representing the unpaginated response.
        """

        return self._call_pageable(
            self.get_resource_by_class,
            args={"class_id": class_id},
            params=params,
            start_page=start_page,
            end_page=end_page,
        )

    @query_params("id", "label", "uri")
    def add(self, params: Optional[Dict] = None) -> OrkgResponse:
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.classes.POST(json=params, headers=self.auth)
        return self.client.wrap_response(response)

    @query_params("id", "label", "uri")
    def find_or_add(self, params: Optional[Dict] = None) -> OrkgResponse:
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            if "id" in params:
                # check if a class with this id is there
                found = self.by_id(params["id"])
                if found.succeeded:
                    return found
            # check if a class with this label is there
            found = self.get_all(q=params["label"], exact=True)
            if found.succeeded:
                if isinstance(found.content, list) and len(found.content) > 0:
                    found.content = found.content[0]
                    return found
            # None found! let's create a new one
            self.client.backend._append_slash = True
            response = self.client.backend.classes.POST(json=params, headers=self.auth)
        return self.client.wrap_response(response)

    @query_params("label", "uri")
    def update(self, id: str, params: Optional[Dict] = None) -> OrkgResponse:
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.classes(id).PUT(
                json=params, headers=self.auth
            )
        return self.client.wrap_response(response)

    def exists(self, id: str) -> bool:
        return self.by_id(id).succeeded
