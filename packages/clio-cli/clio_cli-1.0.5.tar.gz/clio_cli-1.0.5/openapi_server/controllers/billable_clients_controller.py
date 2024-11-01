from typing import List, Dict
from aiohttp import web

from openapi_server.models.billable_client_list import BillableClientList
from openapi_server.models.error import Error
from openapi_server import util


async def billable_client_index(request: web.Request, x_api_version=None, client_id=None, custom_field_values=None, end_date=None, fields=None, limit=None, matter_id=None, originating_attorney_id=None, page_token=None, query=None, responsible_attorney_id=None, start_date=None) -> web.Response:
    """Return the data for all BillableClients

    Outlines the parameters, optional and required, used when requesting the data for all BillableClients

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param client_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property.
    :type client_id: int
    :param custom_field_values: Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; 
    :type custom_field_values: str
    :param end_date: Filter BillableClient records to those that have Matters with unbilled Activities on or before this date (Expects an ISO-8601 date).
    :type end_date: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param limit: A limit on the number of BillableClient records to be returned. Limit can range between 1 and 25. Default: &#x60;25&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableClient records with the matching property.
    :type matter_id: int
    :param originating_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.
    :type originating_attorney_id: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for &#x60;display_number&#x60; or &#x60;number&#x60; or &#x60;description&#x60; matching a given string.
    :type query: str
    :param responsible_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.
    :type responsible_attorney_id: int
    :param start_date: Filter BillableClient records to those that have Matters with unbilled Activities on or after this date (Expects an ISO-8601 date).
    :type start_date: str

    """
    end_date = util.deserialize_date(end_date)
    start_date = util.deserialize_date(start_date)
    return web.Response(status=200)
