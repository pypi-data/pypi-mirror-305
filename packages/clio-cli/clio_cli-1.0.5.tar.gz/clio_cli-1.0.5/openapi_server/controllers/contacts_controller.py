from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_create_request import ContactCreateRequest
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_show import ContactShow
from openapi_server.models.contact_update_request import ContactUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def contact_create(request: web.Request, x_api_version=None, custom_field_ids=None, fields=None, body=None) -> web.Response:
    """Create a new Contact

    Outlines the parameters and data fields used when creating a new Contact

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Contacts
    :type body: dict | bytes

    """
    body = ContactCreateRequest.from_dict(body)
    return web.Response(status=200)


async def contact_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Contact

    Outlines the parameters, optional and required, used when deleting the record for a single Contact

    :param id: The unique identifier for the Contact.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def contact_index(request: web.Request, x_api_version=None, client_only=None, clio_connect_only=None, created_since=None, custom_field_ids=None, custom_field_values=None, email_only=None, exclude_ids=None, fields=None, ids=None, initial=None, limit=None, order=None, page_token=None, query=None, shared_resource_id=None, type=None, updated_since=None) -> web.Response:
    """Return the data for all Contacts

    Outlines the parameters, optional and required, used when requesting the data for all Contacts

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param client_only: Filter Contact records to those that are clients.
    :type client_only: bool
    :param clio_connect_only: Filter Contact records to those that are Clio Connect users.
    :type clio_connect_only: bool
    :param created_since: Filter Contact records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param custom_field_ids: Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param custom_field_values: Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; 
    :type custom_field_values: str
    :param email_only: Filter Contact records to those that have email addresses.
    :type email_only: bool
    :param exclude_ids: Filter Contact records to those who are not included in the given list of unique identifiers.
    :type exclude_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Contact records to those having the specified unique identifiers.
    :type ids: int
    :param initial: Filter Contact records to those where the last name or company name start with the given initial.
    :type initial: str
    :param limit: A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the Contact records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param query: Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string. 
    :type query: str
    :param shared_resource_id: Filter Contact records to those that currently have access to a given shared resource.
    :type shared_resource_id: int
    :param type: Filter Contact records to those that match the given type.
    :type type: str
    :param updated_since: Filter Contact records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def contact_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, custom_field_ids=None, fields=None) -> web.Response:
    """Return the data for a single Contact

    Outlines the parameters, optional and required, used when requesting the data for a single Contact

    :param id: The unique identifier for the Contact.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def contact_update(request: web.Request, id, if_match=None, x_api_version=None, custom_field_ids=None, fields=None, body=None) -> web.Response:
    """Update a single Contact

    Outlines the parameters and data fields used when updating a single Contact

    :param id: The unique identifier for the Contact.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Contacts
    :type body: dict | bytes

    """
    body = ContactUpdateRequest.from_dict(body)
    return web.Response(status=200)
