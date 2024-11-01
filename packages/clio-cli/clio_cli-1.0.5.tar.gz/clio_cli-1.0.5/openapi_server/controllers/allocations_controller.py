from typing import List, Dict
from aiohttp import web

from openapi_server.models.allocation_list import AllocationList
from openapi_server.models.allocation_show import AllocationShow
from openapi_server.models.error import Error
from openapi_server import util


async def allocation_index(request: web.Request, x_api_version=None, bill_id=None, contact_id=None, created_since=None, fields=None, ids=None, limit=None, matter_id=None, order=None, page_token=None, parent_id=None, parent_type=None, status=None, updated_since=None) -> web.Response:
    """Return the data for all Allocations

    Outlines the parameters, optional and required, used when requesting the data for all Allocations

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param bill_id: The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.
    :type bill_id: int
    :param contact_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.
    :type contact_id: int
    :param created_since: Filter Allocation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Allocation records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Allocation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.
    :type matter_id: int
    :param order: Orders the Allocation records by the given field. Default: &#x60;date(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param parent_id: ID of parent (either a Payment or CreditMemo) this allocation belongs to
    :type parent_id: int
    :param parent_type: Filter Allocation records based on whether the parent is a CreditMemo or a Payment.
    :type parent_type: int
    :param status: Filter Allocation records to only those that are voided (&#x60;\&quot;invalid\&quot;&#x60;) or not voided (&#x60;\&quot;valid\&quot;&#x60;).
    :type status: str
    :param updated_since: Filter Allocation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def allocation_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Allocation

    Outlines the parameters, optional and required, used when requesting the data for a single Allocation

    :param id: The unique identifier for the Allocation.
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
