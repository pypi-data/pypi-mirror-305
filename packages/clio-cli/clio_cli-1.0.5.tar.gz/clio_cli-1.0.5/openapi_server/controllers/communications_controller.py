from typing import List, Dict
from aiohttp import web

from openapi_server.models.communication_create_request import CommunicationCreateRequest
from openapi_server.models.communication_list import CommunicationList
from openapi_server.models.communication_show import CommunicationShow
from openapi_server.models.communication_update_request import CommunicationUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def communication_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Communication

    Outlines the parameters and data fields used when creating a new Communication

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Communications
    :type body: dict | bytes

    """
    body = CommunicationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def communication_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Communication

    Outlines the parameters, optional and required, used when deleting the record for a single Communication

    :param id: The unique identifier for the Communication.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def communication_index(request: web.Request, x_api_version=None, contact_id=None, created_since=None, _date=None, external_property_name=None, external_property_value=None, fields=None, having_time_entries=None, ids=None, limit=None, matter_id=None, order=None, page_token=None, query=None, received_at=None, received_before=None, received_since=None, type=None, updated_since=None, user_id=None) -> web.Response:
    """Return the data for all Communications

    Outlines the parameters, optional and required, used when requesting the data for all Communications

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property.
    :type contact_id: int
    :param created_since: Filter Communication records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param _date: Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).
    :type _date: str
    :param external_property_name: Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; 
    :type external_property_name: str
    :param external_property_value: Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; 
    :type external_property_value: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param having_time_entries: Filter Communication records to those that do or do not have time entries.
    :type having_time_entries: bool
    :param ids: Filter Communication records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Communication. The list will be filtered to include only the Communication records with the matching property.
    :type matter_id: int
    :param order: Orders the Communication records by the given field. Default: &#x60;date(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;body&#x60; or &#x60;subject&#x60; matching a given string.
    :type query: str
    :param received_at: Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).
    :type received_at: str
    :param received_before: Filter Communication records to those whose &#x60;date&#x60; is on or before the date provided (Expects an ISO-8601 date).
    :type received_before: str
    :param received_since: Filter Communication records to those whose &#x60;date&#x60; is on or after the date provided (Expects an ISO-8601 date).
    :type received_since: str
    :param type: Filter Communication records to those of the specified type.
    :type type: str
    :param updated_since: Filter Communication records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param user_id: The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Communication records with the matching property.
    :type user_id: int

    """
    created_since = util.deserialize_datetime(created_since)
    _date = util.deserialize_date(_date)
    received_at = util.deserialize_datetime(received_at)
    received_before = util.deserialize_datetime(received_before)
    received_since = util.deserialize_datetime(received_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def communication_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Communication

    Outlines the parameters, optional and required, used when requesting the data for a single Communication

    :param id: The unique identifier for the Communication.
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


async def communication_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Communication

    Outlines the parameters and data fields used when updating a single Communication

    :param id: The unique identifier for the Communication.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Communications
    :type body: dict | bytes

    """
    body = CommunicationUpdateRequest.from_dict(body)
    return web.Response(status=200)
