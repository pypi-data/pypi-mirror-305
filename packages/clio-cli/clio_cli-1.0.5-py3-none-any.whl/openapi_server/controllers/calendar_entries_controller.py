from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_entry_create_request import CalendarEntryCreateRequest
from openapi_server.models.calendar_entry_list import CalendarEntryList
from openapi_server.models.calendar_entry_show import CalendarEntryShow
from openapi_server.models.calendar_entry_update_request import CalendarEntryUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def calendar_entry_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new CalendarEntry

    Outlines the parameters and data fields used when creating a new CalendarEntry

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Calendar Entries
    :type body: dict | bytes

    """
    body = CalendarEntryCreateRequest.from_dict(body)
    return web.Response(status=200)


async def calendar_entry_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single CalendarEntry

    Outlines the parameters, optional and required, used when deleting the record for a single CalendarEntry

    :param id: The unique identifier for the CalendarEntry.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def calendar_entry_index(request: web.Request, x_api_version=None, calendar_id=None, created_since=None, expanded=None, external_property_name=None, external_property_value=None, fields=None, _from=None, has_court_rule=None, ids=None, is_all_day=None, limit=None, matter_id=None, owner_entries_across_all_users=None, page_token=None, query=None, source=None, to=None, updated_since=None, visible=None) -> web.Response:
    """Return the data for all CalendarEntries

    Outlines the parameters, optional and required, used when requesting the data for all CalendarEntries

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param calendar_id: The unique identifier for a single Calendar. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the CalendarEntry records with the matching property.
    :type calendar_id: int
    :param created_since: Filter CalendarEntry records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param expanded: Returns a record for each occurrence of a recurring calendar event.  Non-recurring calendar events are unaffected and returned as separate records regardless of the expanded setting.
    :type expanded: bool
    :param external_property_name: Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; 
    :type external_property_name: str
    :param external_property_value: Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; 
    :type external_property_value: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param _from: Filter CalendarEntry records to those that end on or after the provided time (Expects an ISO-8601 timestamp).
    :type _from: str
    :param has_court_rule: Allows matching court rule on calendar entry.
    :type has_court_rule: bool
    :param ids: Filter CalendarEntry records to those having the specified unique identifiers.
    :type ids: int
    :param is_all_day: Filter CalendarEntry records to those that are marked as all day events.
    :type is_all_day: bool
    :param limit: A limit on the number of CalendarEntry records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a CalendarEntry. The list will be filtered to include only the CalendarEntry records with the matching property.
    :type matter_id: int
    :param owner_entries_across_all_users: Returns CalendarEntry records for all users related to a matter. Requires matter id.
    :type owner_entries_across_all_users: bool
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Allows matching search on calendar entry.
    :type query: str
    :param source: Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web).
    :type source: str
    :param to: Filter CalendarEntry records to those that begin on or before the provided time (Expects an ISO-8601 timestamp).
    :type to: str
    :param updated_since: Filter CalendarEntry records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param visible: Filter CalendarEntry records to those that are visible.
    :type visible: bool

    """
    created_since = util.deserialize_datetime(created_since)
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def calendar_entry_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single CalendarEntry

    Outlines the parameters, optional and required, used when requesting the data for a single CalendarEntry

    :param id: The unique identifier for the CalendarEntry.
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


async def calendar_entry_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single CalendarEntry

    Outlines the parameters and data fields used when updating a single CalendarEntry

    :param id: The unique identifier for the CalendarEntry.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Calendar Entries
    :type body: dict | bytes

    """
    body = CalendarEntryUpdateRequest.from_dict(body)
    return web.Response(status=200)
