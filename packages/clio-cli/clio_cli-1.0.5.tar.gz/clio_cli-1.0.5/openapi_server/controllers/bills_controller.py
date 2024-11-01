from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_list import BillList
from openapi_server.models.bill_show import BillShow
from openapi_server.models.bill_update_request import BillUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def bill_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete or void a Bill

    This endpoint will transition a bill to either its deleted or voided state. A bill can only be deleted or voided if it has no payments recorded and its current state is one of the following: * Draft * Pending Approval * Unpaid  A bill will automatically be moved to a deleted or void state based on its current state. The mappings for this are: * Draft -&gt; Deleted * Pending Approval -&gt; Deleted * Unpaid -&gt; Void 

    :param id: The unique identifier for the Bill.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def bill_index(request: web.Request, x_api_version=None, client_id=None, created_since=None, custom_field_values=None, due_after=None, due_at=None, due_before=None, fields=None, ids=None, issued_after=None, issued_before=None, last_sent_end_date=None, last_sent_start_date=None, limit=None, matter_id=None, order=None, originating_attorney_id=None, overdue_only=None, page_token=None, query=None, responsible_attorney_id=None, state=None, status=None, type=None, updated_since=None) -> web.Response:
    """Return the data for all Bills

    Outlines the parameters, optional and required, used when requesting the data for all Bills

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param client_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Bill records with the matching property.
    :type client_id: int
    :param created_since: Filter Bill records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param custom_field_values: Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; 
    :type custom_field_values: str
    :param due_after: Filter Bill records to those that have a &#x60;due_date&#x60; after the one provided (Expects an ISO-8601 date).
    :type due_after: str
    :param due_at: Filter Bill records to those that have a specific &#x60;due_date&#x60; (Expects an ISO-8601 date).
    :type due_at: str
    :param due_before: Filter Bill records to those that have a &#x60;due_date&#x60; before the one provided (Expects an ISO-8601 date).
    :type due_before: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Bill records to those having the specified unique identifiers.
    :type ids: int
    :param issued_after: Filter Bill records to those that have an &#x60;issue_date&#x60; after the one provided (Expects an ISO-8601 date).
    :type issued_after: str
    :param issued_before: Filter Bill records to those that have an &#x60;issue_date&#x60; before the one provided (Expects an ISO-8601 date).
    :type issued_before: str
    :param last_sent_end_date: Filter Bill records for those whose bills have been sent before the specified date
    :type last_sent_end_date: str
    :param last_sent_start_date: Filter Bill records for those whose bills have been sent after the specified date
    :type last_sent_start_date: str
    :param limit: A limit on the number of Bill records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property.
    :type matter_id: int
    :param order: Orders the Bill records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param originating_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property.
    :type originating_attorney_id: int
    :param overdue_only: Filter Bill records to those that are overdue.
    :type overdue_only: bool
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Allows matching search on invoice number.
    :type query: int
    :param responsible_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Bill. The list will be filtered to include only the Bill records with the matching property.
    :type responsible_attorney_id: int
    :param state: Filter Bill records to those in a given state.
    :type state: str
    :param status: Filter Bill records to those with particular payment status.
    :type status: str
    :param type: Filter Bill records to those of a specific type.
    :type type: str
    :param updated_since: Filter Bill records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    due_after = util.deserialize_date(due_after)
    due_at = util.deserialize_date(due_at)
    due_before = util.deserialize_date(due_before)
    issued_after = util.deserialize_date(issued_after)
    issued_before = util.deserialize_date(issued_before)
    last_sent_end_date = util.deserialize_date(last_sent_end_date)
    last_sent_start_date = util.deserialize_date(last_sent_start_date)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def bill_preview(request: web.Request, id) -> web.Response:
    """Returns the pre-rendered html for the Bill

    This endpoint returns a pre-rendered HTML object that you can use to view a preview of your bills. The HTML provided contains all of the CSS rules it requires to show the bill correctly, as well as the DOCTYPE setting it requires. It&#39;s best to use an iframe, or similar object, to render the results of this endpoint. 

    :param id: The unique identifier for the Bill.
    :type id: int

    """
    return web.Response(status=200)


async def bill_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None, navigation_next=None, navigation_previous=None) -> web.Response:
    """Return the data for a single Bill

    Outlines the parameters, optional and required, used when requesting the data for a single Bill

    :param id: The unique identifier for the Bill.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param navigation_next: The id of the next *Bill* available for viewing
    :type navigation_next: int
    :param navigation_previous: The id of the previous *Bill* available for viewing
    :type navigation_previous: int

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def bill_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Bill

    Outlines the parameters and data fields used when updating a single Bill

    :param id: The unique identifier for the Bill.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Bills
    :type body: dict | bytes

    """
    body = BillUpdateRequest.from_dict(body)
    return web.Response(status=200)
