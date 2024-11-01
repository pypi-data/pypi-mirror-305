from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_create_request import CustomFieldCreateRequest
from openapi_server.models.custom_field_list import CustomFieldList
from openapi_server.models.custom_field_show import CustomFieldShow
from openapi_server.models.custom_field_update_request import CustomFieldUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def custom_field_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new CustomField

    Outlines the parameters and data fields used when creating a new CustomField

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Custom Fields
    :type body: dict | bytes

    """
    body = CustomFieldCreateRequest.from_dict(body)
    return web.Response(status=200)


async def custom_field_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single CustomField

    Outlines the parameters, optional and required, used when deleting the record for a single CustomField

    :param id: The unique identifier for the CustomField.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def custom_field_index(request: web.Request, x_api_version=None, created_since=None, deleted=None, field_type=None, fields=None, ids=None, limit=None, order=None, page_token=None, parent_type=None, query=None, updated_since=None, visible_and_required=None) -> web.Response:
    """Return the data for all CustomFields

    Outlines the parameters, optional and required, used when requesting the data for all CustomFields

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter CustomField records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param deleted: Filter CustomField records to those that have been deleted for future use.
    :type deleted: bool
    :param field_type: Field type of this custom field
    :type field_type: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter CustomField records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of CustomField records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the CustomField records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param parent_type: Filter CustomField records to those that have the specified &#x60;parent_type&#x60;.
    :type parent_type: str
    :param query: Wildcard search for &#x60;name&#x60; matching a given string.
    :type query: str
    :param updated_since: Filter CustomField records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str
    :param visible_and_required: Filter CustomField records to those that are visible and required.
    :type visible_and_required: bool

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def custom_field_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single CustomField

    Outlines the parameters, optional and required, used when requesting the data for a single CustomField

    :param id: The unique identifier for the CustomField.
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


async def custom_field_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single CustomField

    Outlines the parameters and data fields used when updating a single CustomField

    :param id: The unique identifier for the CustomField.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Custom Fields
    :type body: dict | bytes

    """
    body = CustomFieldUpdateRequest.from_dict(body)
    return web.Response(status=200)
