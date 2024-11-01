from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.timer_create_request import TimerCreateRequest
from openapi_server.models.timer_show import TimerShow
from openapi_server import util


async def timer_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Timer

    Outlines the parameters and data fields used when creating a new Timer

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Timers
    :type body: dict | bytes

    """
    body = TimerCreateRequest.from_dict(body)
    return web.Response(status=200)


async def timer_destroy(request: web.Request, x_api_version=None) -> web.Response:
    """Delete a single Timer

    Outlines the parameters, optional and required, used when deleting the record for a single Timer

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def timer_show(request: web.Request, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Timer

    Outlines the parameters, optional and required, used when requesting the data for a single Timer

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
