from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.trust_line_item_list import TrustLineItemList
from openapi_server.models.trust_line_item_show import TrustLineItemShow
from openapi_server.models.trust_line_item_update_request import TrustLineItemUpdateRequest
from openapi_server import util


async def trust_line_item_index(request: web.Request, x_api_version=None, bill_id=None, created_since=None, fields=None, ids=None, limit=None, matter_id=None, order=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all TrustLineItems

    Outlines the parameters, optional and required, used when requesting the data for all TrustLineItems

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param bill_id: The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property.
    :type bill_id: int
    :param created_since: Filter TrustLineItem records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter TrustLineItem records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property.
    :type matter_id: int
    :param order: Orders the TrustLineItem records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter TrustLineItem records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def trust_line_item_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single TrustLineItem

    Outlines the parameters and data fields used when updating a single TrustLineItem

    :param id: The unique identifier for the TrustLineItem.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Trust Line Items
    :type body: dict | bytes

    """
    body = TrustLineItemUpdateRequest.from_dict(body)
    return web.Response(status=200)
