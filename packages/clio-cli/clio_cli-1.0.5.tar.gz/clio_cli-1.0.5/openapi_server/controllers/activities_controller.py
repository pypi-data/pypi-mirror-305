from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_create_request import ActivityCreateRequest
from openapi_server.models.activity_list import ActivityList
from openapi_server.models.activity_show import ActivityShow
from openapi_server.models.activity_update_request import ActivityUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def activity_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Activity

    Outlines the parameters and data fields used when creating a new Activity

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activities
    :type body: dict | bytes

    """
    body = ActivityCreateRequest.from_dict(body)
    return web.Response(status=200)


async def activity_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Activity

    Outlines the parameters, optional and required, used when deleting the record for a single Activity

    :param id: The unique identifier for the Activity.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def activity_index(request: web.Request, x_api_version=None, activity_description_id=None, calendar_entry_id=None, communication_id=None, contact_note_id=None, created_since=None, end_date=None, expense_category_id=None, fields=None, flat_rate=None, grant_id=None, ids=None, limit=None, matter_id=None, matter_note_id=None, only_unaccounted_for=None, order=None, page_token=None, query=None, start_date=None, status=None, task_id=None, type=None, updated_since=None, user_id=None) -> web.Response:
    """Return the data for all Activities

    Outlines the parameters, optional and required, used when requesting the data for all Activities

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param activity_description_id: The unique identifier for a single ActivityDescription. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type activity_description_id: int
    :param calendar_entry_id: The unique identifier for a single CalendarEntry. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type calendar_entry_id: int
    :param communication_id: The unique identifier for a single Communication. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type communication_id: int
    :param contact_note_id: The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type contact_note_id: int
    :param created_since: Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param end_date: Filter Activity records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).
    :type end_date: str
    :param expense_category_id: The unique identifier for a single ExpenseCategory. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type expense_category_id: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param flat_rate: Filter Activity TimeEntry records to those that have a flat rate, or not.
    :type flat_rate: bool
    :param grant_id: The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type grant_id: int
    :param ids: Filter Activity records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type matter_id: int
    :param matter_note_id: The unique identifier for a single Note. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type matter_note_id: int
    :param only_unaccounted_for: Only unaccounted for activities.
    :type only_unaccounted_for: bool
    :param order: Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;note&#x60; matching a given string.
    :type query: str
    :param start_date: Filter Activity records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).
    :type start_date: str
    :param status: Filter Activity records to those that are draft, billed, unbilled or non-billable.
    :type status: str
    :param task_id: The unique identifier for a single Task. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type task_id: int
    :param type: Filter Activity records to those of a specific type.
    :type type: str
    :param updated_since: Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param user_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.
    :type user_id: int

    """
    created_since = util.deserialize_datetime(created_since)
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def activity_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Activity

    Outlines the parameters, optional and required, used when requesting the data for a single Activity

    :param id: The unique identifier for the Activity.
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


async def activity_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Activity

    Outlines the parameters and data fields used when updating a single Activity

    :param id: The unique identifier for the Activity.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Activities
    :type body: dict | bytes

    """
    body = ActivityUpdateRequest.from_dict(body)
    return web.Response(status=200)
