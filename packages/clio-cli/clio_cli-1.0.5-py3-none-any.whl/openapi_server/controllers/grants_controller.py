from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.grant_create_request import GrantCreateRequest
from openapi_server.models.grant_list import GrantList
from openapi_server.models.grant_show import GrantShow
from openapi_server import util


async def grant_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new grant

    Outlines the parameters and data fields used when creating a new Grant

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Grants
    :type body: dict | bytes

    """
    body = GrantCreateRequest.from_dict(body)
    return web.Response(status=200)


async def grant_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Deletes a single grant

    Outlines the parameters, optional and required, used when deleting the record for a single Grant

    :param id: The unique identifier for the Grant.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def grant_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, name=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all grants

    Outlines the parameters, optional and required, used when requesting the data for all Grants

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter Grant records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Grant records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Grant records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param name: Filter Grant records to those that match the given name.
    :type name: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter Grant records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def grant_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single grant

    Outlines the parameters, optional and required, used when requesting the data for a single Grant

    :param id: The unique identifier for the Grant.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def grant_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single grant

    Outlines the parameters and data fields used when updating a single Grant

    :param id: The unique identifier for the Grant.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Grants
    :type body: dict | bytes

    """
    body = GrantCreateRequest.from_dict(body)
    return web.Response(status=200)
