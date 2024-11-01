from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user_list import UserList
from openapi_server.models.user_show import UserShow
from openapi_server import util


async def user_index(request: web.Request, x_api_version=None, created_since=None, enabled=None, fields=None, ids=None, include_co_counsel=None, limit=None, name=None, order=None, page_token=None, pending_setup=None, role=None, subscription_type=None, updated_since=None) -> web.Response:
    """Return the data for all Users

    Outlines the parameters, optional and required, used when requesting the data for all Users

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter User records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param enabled: Filter User records to those that are enabled or disabled.
    :type enabled: bool
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter User records to those having the specified unique identifiers.
    :type ids: int
    :param include_co_counsel: Filter User to include co-counsel users
    :type include_co_counsel: bool
    :param limit: A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: &#x60;2000&#x60;.
    :type limit: int
    :param name: Filter User records to those with the given name.
    :type name: str
    :param order: Orders the User records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param pending_setup: Filter User records based on whether or not they are still being setup.
    :type pending_setup: bool
    :param role: Filter User records to those with a specific role.
    :type role: str
    :param subscription_type: Filter User records to those with a specific subscription type.
    :type subscription_type: str
    :param updated_since: Filter User records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def user_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single User

    Outlines the parameters, optional and required, used when requesting the data for a single User

    :param id: The unique identifier for the User.
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


async def user_who_am_i(request: web.Request, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for the current User

    Outlines the parameters, optional and required, used when requesting the data for a single User

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
