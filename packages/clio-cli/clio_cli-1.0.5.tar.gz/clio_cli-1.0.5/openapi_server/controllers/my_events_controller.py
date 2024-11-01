from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.my_event_list import MyEventList
from openapi_server.models.my_event_show import MyEventShow
from openapi_server.models.my_event_update_request import MyEventUpdateRequest
from openapi_server import util


async def my_event_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Clear (delete) a single in-app notification event

    Outlines the parameters, optional and required, used when deleting the record for a single MyEvent

    :param id: The unique identifier for the MyEvent.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def my_event_index(request: web.Request, x_api_version=None, fields=None, limit=None, page_token=None) -> web.Response:
    """Return the data for all of my in-app notification events

    Outlines the parameters, optional and required, used when requesting the data for all MyEvents

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param limit: A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str

    """
    return web.Response(status=200)


async def my_event_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Mark a single in-app notification event as read/unread

    Outlines the parameters and data fields used when updating a single MyEvent

    :param id: The unique identifier for the MyEvent.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for My Events
    :type body: dict | bytes

    """
    body = MyEventUpdateRequest.from_dict(body)
    return web.Response(status=200)
