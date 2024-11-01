from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_create_request import CalendarCreateRequest
from openapi_server.models.calendar_list import CalendarList
from openapi_server.models.calendar_show import CalendarShow
from openapi_server.models.calendar_update_request import CalendarUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def calendar_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Calendar

    Outlines the parameters and data fields used when creating a new Calendar

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Calendars
    :type body: dict | bytes

    """
    body = CalendarCreateRequest.from_dict(body)
    return web.Response(status=200)


async def calendar_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Calendar

    Outlines the parameters, optional and required, used when deleting the record for a single Calendar

    :param id: The unique identifier for the Calendar.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def calendar_index(request: web.Request, x_api_version=None, created_since=None, fields=None, filter_inactive_users=None, ids=None, limit=None, order=None, owner=None, page_token=None, source=None, type=None, updated_since=None, visible=None, writeable=None) -> web.Response:
    """Return the data for all Calendars

    Outlines the parameters, optional and required, used when requesting the data for all Calendars

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter Calendar records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param filter_inactive_users: Filter any shared UserCalendar records whose owner is inactive.
    :type filter_inactive_users: bool
    :param ids: Filter Calendar records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the Calendar records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param owner: Filter Calendar records to those that the user owns.
    :type owner: bool
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param source: Filter Calendar records to those having a specific calendar visibility source (mobile, web).
    :type source: str
    :param type: Filter Calendar records to those of the specified type.
    :type type: str
    :param updated_since: Filter Calendar records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param visible: Filter Calendar records to those that are visible.
    :type visible: bool
    :param writeable: Filter Calendar records to those which the user can write to.
    :type writeable: bool

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def calendar_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Calendar

    Outlines the parameters, optional and required, used when requesting the data for a single Calendar

    :param id: The unique identifier for the Calendar.
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


async def calendar_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Calendar

    Outlines the parameters and data fields used when updating a single Calendar

    :param id: The unique identifier for the Calendar.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Calendars
    :type body: dict | bytes

    """
    body = CalendarUpdateRequest.from_dict(body)
    return web.Response(status=200)
