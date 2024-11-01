from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.group_create_request import GroupCreateRequest
from openapi_server.models.group_list import GroupList
from openapi_server.models.group_show import GroupShow
from openapi_server import util


async def group_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Group

    Outlines the parameters and data fields used when creating a new Group

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Groups
    :type body: dict | bytes

    """
    body = GroupCreateRequest.from_dict(body)
    return web.Response(status=200)


async def group_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Group

    Outlines the parameters, optional and required, used when deleting the record for a single Group

    :param id: The unique identifier for the Group.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def group_index(request: web.Request, x_api_version=None, archived=None, created_since=None, fields=None, ids=None, limit=None, name=None, order=None, page_token=None, query=None, type=None, updated_since=None, user_id=None) -> web.Response:
    """Return the data for all Groups

    Outlines the parameters, optional and required, used when requesting the data for all Groups

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param archived: Filter archived Group records.
    :type archived: bool
    :param created_since: Filter Group records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Group records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Group records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param name: Filter Group records to those that match the given name.
    :type name: str
    :param order: Orders the Group records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;name&#x60; matching a given string.
    :type query: str
    :param type: Filter Group records to those that match the given type.
    :type type: str
    :param updated_since: Filter Group records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param user_id: The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Group records with the matching property.
    :type user_id: int

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def group_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Group

    Outlines the parameters, optional and required, used when requesting the data for a single Group

    :param id: The unique identifier for the Group.
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


async def group_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Group

    Outlines the parameters and data fields used when updating a single Group

    :param id: The unique identifier for the Group.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Groups
    :type body: dict | bytes

    """
    body = GroupCreateRequest.from_dict(body)
    return web.Response(status=200)
