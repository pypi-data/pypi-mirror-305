from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_create_request import MatterCreateRequest
from openapi_server.models.matter_list import MatterList
from openapi_server.models.matter_show import MatterShow
from openapi_server.models.matter_update_request import MatterUpdateRequest
from openapi_server import util


async def matter_create(request: web.Request, x_api_version=None, custom_field_ids=None, fields=None, body=None) -> web.Response:
    """Create a new Matter

    Outlines the parameters and data fields used when creating a new Matter

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Matters
    :type body: dict | bytes

    """
    body = MatterCreateRequest.from_dict(body)
    return web.Response(status=200)


async def matter_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Matter

    Outlines the parameters, optional and required, used when deleting the record for a single Matter

    :param id: The unique identifier for the Matter.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def matter_index(request: web.Request, x_api_version=None, billable=None, client_id=None, close_date=None, created_since=None, custom_field_ids=None, custom_field_values=None, fields=None, grant_id=None, group_id=None, ids=None, limit=None, notification_event_subscriber_user_id=None, open_date=None, order=None, originating_attorney_id=None, page_token=None, pending_date=None, practice_area_id=None, query=None, responsible_attorney_id=None, status=None, subscriber_user_id=None, updated_since=None) -> web.Response:
    """Return the data for all Matters

    Outlines the parameters, optional and required, used when requesting the data for all Matters

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param billable: Filter Matter records to those which are billable.
    :type billable: bool
    :param client_id: The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.
    :type client_id: int
    :param close_date: Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?close_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?close_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?close_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;close_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. 
    :type close_date: str
    :param created_since: Filter Matter records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param custom_field_ids: Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param custom_field_values: Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; 
    :type custom_field_values: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param grant_id: The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.
    :type grant_id: int
    :param group_id: The unique identifier for a single Group. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.
    :type group_id: int
    :param ids: Filter Matter records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Matter records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param notification_event_subscriber_user_id: The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.
    :type notification_event_subscriber_user_id: int
    :param open_date: Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?open_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?open_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?open_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;open_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. 
    :type open_date: str
    :param order: Orders the Matter records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param originating_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.
    :type originating_attorney_id: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param pending_date: Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?pending_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?pending_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?pending_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;pending_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. 
    :type pending_date: str
    :param practice_area_id: The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.
    :type practice_area_id: int
    :param query: Wildcard search for &#x60;display_number&#x60;, &#x60;number&#x60; or &#x60;description&#x60; matching a given string, as well as the &#x60;first_name&#x60;, &#x60;last_name&#x60; or &#x60;name&#x60; of the associated client.
    :type query: str
    :param responsible_attorney_id: The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.
    :type responsible_attorney_id: int
    :param status: Filter Matter records to those with a given status. It accepts comma-separated statuses, e.g. &#x60;open,pending&#x60;.
    :type status: str
    :param subscriber_user_id: The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.
    :type subscriber_user_id: int
    :param updated_since: Filter Matter records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def matter_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, custom_field_ids=None, fields=None) -> web.Response:
    """Return the data for a single Matter

    Outlines the parameters, optional and required, used when requesting the data for a single Matter

    :param id: The unique identifier for the Matter.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def matter_update(request: web.Request, id, if_match=None, x_api_version=None, custom_field_ids=None, fields=None, body=None) -> web.Response:
    """Update a single Matter

    Outlines the parameters and data fields used when updating a single Matter

    :param id: The unique identifier for the Matter.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Matter&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Matters
    :type body: dict | bytes

    """
    body = MatterUpdateRequest.from_dict(body)
    return web.Response(status=200)
