from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.line_item_list import LineItemList
from openapi_server.models.line_item_show import LineItemShow
from openapi_server.models.line_item_update_request import LineItemUpdateRequest
from openapi_server import util


async def line_item_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single LineItem

    A LineItem can not be deleted if it&#39;s Bill is not editable

    :param id: The unique identifier for the LineItem.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def line_item_index(request: web.Request, x_api_version=None, activity_id=None, bill_id=None, created_since=None, display=None, exclude_ids=None, fields=None, group_ordering=None, ids=None, kind=None, limit=None, matter_id=None, page_token=None, query=None, updated_since=None) -> web.Response:
    """Return the data for all LineItems

    Outlines the parameters, optional and required, used when requesting the data for all LineItems

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param activity_id: The unique identifier for a single Activity. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.
    :type activity_id: int
    :param bill_id: The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the LineItem records with the matching property.
    :type bill_id: int
    :param created_since: Filter LineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param display: Set this flag to true to return only LineItems displayed on the bill.
    :type display: bool
    :param exclude_ids: Array containing LineItem identifiers that should be excluded from the query.
    :type exclude_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param group_ordering: Filters LineItem records to match given group ordering.
    :type group_ordering: int
    :param ids: Filter LineItem records to those having the specified unique identifiers.
    :type ids: int
    :param kind: The kind of LineItem.
    :type kind: str
    :param limit: A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.
    :type matter_id: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;description&#x60; or &#x60;note&#x60; matching a given string.
    :type query: str
    :param updated_since: Filter LineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def line_item_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single LineItem

    Outlines the parameters and data fields used when updating a single LineItem

    :param id: The unique identifier for the LineItem.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Line Items
    :type body: dict | bytes

    """
    body = LineItemUpdateRequest.from_dict(body)
    return web.Response(status=200)
