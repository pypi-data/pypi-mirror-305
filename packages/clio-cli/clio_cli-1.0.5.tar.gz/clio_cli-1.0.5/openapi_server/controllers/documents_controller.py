from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_copy_request import DocumentCopyRequest
from openapi_server.models.document_create_request import DocumentCreateRequest
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_show import DocumentShow
from openapi_server.models.document_update_request import DocumentUpdateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def document_copy(request: web.Request, id, fields=None, body=None) -> web.Response:
    """Copy a Document

    Copies the latest document version of a Document into a new Document. The parameters &#x60;filename&#x60; and &#x60;name&#x60; will be copied from the source Document if none are provided. 

    :param id: The unique identifier for the Document.
    :type id: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Documents
    :type body: dict | bytes

    """
    body = DocumentCopyRequest.from_dict(body)
    return web.Response(status=200)


async def document_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Document

    Create a Document, or Create Document Version to an existing Document. 

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Documents
    :type body: dict | bytes

    """
    body = DocumentCreateRequest.from_dict(body)
    return web.Response(status=200)


async def document_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Document

    Deleting a Document using this method will move it to the trash instead of permanently deleting it. Trashed Documents are permanently deleted after 30 days. The following errors may be returned:  - &#x60;409 Conflict&#x60;: The Document (or one of its ancestor folders) is currently being modified by another request, and cannot be trashed. 

    :param id: The unique identifier for the Document.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def document_download(request: web.Request, id, document_version_id=None) -> web.Response:
    """Download the Document

    Download the Document

    :param id: The unique identifier for the Document.
    :type id: int
    :param document_version_id: The unique identifier for a DocumentVersion to be downloaded. Defaults to the latest.
    :type document_version_id: int

    """
    return web.Response(status=200)


async def document_index(request: web.Request, x_api_version=None, contact_id=None, created_since=None, document_category_id=None, external_property_name=None, external_property_value=None, fields=None, ids=None, include_deleted=None, limit=None, matter_id=None, order=None, page_token=None, parent_id=None, query=None, scope=None, show_uncompleted=None, updated_since=None) -> web.Response:
    """Return the data for all Documents

    Outlines the parameters, optional and required, used when requesting the data for all Documents

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.
    :type contact_id: int
    :param created_since: Filter Document records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param document_category_id: The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.
    :type document_category_id: int
    :param external_property_name: Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; 
    :type external_property_name: str
    :param external_property_value: Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; 
    :type external_property_value: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Document records to those having the specified unique identifiers.
    :type ids: int
    :param include_deleted: Allow trashed Document record to be included.
    :type include_deleted: bool
    :param limit: A limit on the number of Document records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.
    :type matter_id: int
    :param order: Orders the Document records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param parent_id: The unique identifier for a single Folder. Use the keyword &#x60;null&#x60; to match those without a Document. The list will be filtered to include only the Document records with the matching property.
    :type parent_id: int
    :param query: Wildcard search for &#x60;name&#x60; matching the given string.
    :type query: str
    :param scope: Filters Document record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.
    :type scope: str
    :param show_uncompleted: Allow Document record being uploaded to be included.
    :type show_uncompleted: bool
    :param updated_since: Filter Document records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def document_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Document

    Outlines the parameters, optional and required, used when requesting the data for a single Document

    :param id: The unique identifier for the Document.
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


async def document_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Document

    Update Document, move Document to another Folder, and/or restore a trashed Document. 

    :param id: The unique identifier for the Document.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Documents
    :type body: dict | bytes

    """
    body = DocumentUpdateRequest.from_dict(body)
    return web.Response(status=200)
