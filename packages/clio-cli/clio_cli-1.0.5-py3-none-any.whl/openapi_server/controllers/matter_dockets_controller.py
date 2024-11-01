from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_docket_create_request import MatterDocketCreateRequest
from openapi_server.models.matter_docket_list import MatterDocketList
from openapi_server.models.matter_docket_show import MatterDocketShow
from openapi_server import util


async def matter_docket_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Creates a matter docket

    Outlines the parameters and data fields used when creating a new MatterDocket

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Matter Dockets
    :type body: dict | bytes

    """
    body = MatterDocketCreateRequest.from_dict(body)
    return web.Response(status=200)


async def matter_docket_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Deletes the requested matter docket

    Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket

    :param id: The unique identifier for the MatterDocket.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def matter_docket_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, matter_id=None, matter_status=None, order=None, page_token=None, query=None, service_type_id=None, status=None, updated_since=None) -> web.Response:
    """Return the data for all matter dockets

    Outlines the parameters, optional and required, used when requesting the data for all MatterDockets

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter MatterDocket records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter MatterDocket records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    :type matter_id: int
    :param matter_status: Filter MatterDocket records to those with Matters having a specific status.
    :type matter_status: str
    :param order: Orders the MatterDocket records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;name&#x60; matching a given string.
    :type query: str
    :param service_type_id: The unique identifier for a single ServiceType. Use the keyword &#x60;null&#x60; to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.
    :type service_type_id: int
    :param status: Filter MatterDocket records to those having a specific status.
    :type status: str
    :param updated_since: Filter MatterDocket records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def matter_docket_preview(request: web.Request, jurisdiction_id, service_type_id, start_date, start_time, trigger_id, event_prefix=None) -> web.Response:
    """Preview calendar dates for the docket

    Preview calendar dates for the docket

    :param jurisdiction_id: The unique identifier for a single Jurisdiction. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    :type jurisdiction_id: int
    :param service_type_id: The unique identifier for a single ServiceType. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    :type service_type_id: int
    :param start_date: The date the MatterDocket should start. (Expects an ISO-8601 date).
    :type start_date: str
    :param start_time: The time the MatterDocket should start. (Expects an ISO-8601 timestamp).
    :type start_time: str
    :param trigger_id: The unique identifier for a single JurisdictionsToTrigger. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.
    :type trigger_id: int
    :param event_prefix: The prefix that will be added to the beginning of all court rule event titles
    :type event_prefix: str

    """
    start_date = util.deserialize_datetime(start_date)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def matter_docket_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for the matter docket

    Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket

    :param id: The unique identifier for the MatterDocket.
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
