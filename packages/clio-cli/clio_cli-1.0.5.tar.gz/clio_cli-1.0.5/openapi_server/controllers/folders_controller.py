from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.folder_create_request import FolderCreateRequest
from openapi_server.models.folder_list import FolderList
from openapi_server.models.folder_show import FolderShow
from openapi_server.models.folder_update_request import FolderUpdateRequest
from openapi_server.models.item_list import ItemList
from openapi_server import util


async def folder_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new Folder

    Create a Folder to an existing folder. 

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Folders
    :type body: dict | bytes

    """
    body = FolderCreateRequest.from_dict(body)
    return web.Response(status=200)


async def folder_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single Folder

    Deleting a Folder using this method will move it to the trash instead of permanently deleting it. Trashed Folders are permanently deleted after 30 days. The following errors may be returned:  - &#x60;400 Bad Request&#x60;: The Folder cannot be trashed. The &#x60;type&#x60; of the error will be &#x60;DeleteFailed&#x60; and the &#x60;message&#x60; of the error will be one of the following:   - &#x60;Delete failed: This folder contains more than 100,000 items and cannot be trashed. Please trash some of the items inside it before trying again.&#x60;   - &#x60;Delete failed: This item contains locked items and cannot be deleted.&#x60;   - &#x60;Delete failed: The root folder cannot be trashed&#x60; - &#x60;409 Conflict&#x60;: The Folder (or one of its descendants) is currently being modified by another request, and cannot be trashed. 

    :param id: The unique identifier for the Folder.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def folder_index(request: web.Request, x_api_version=None, contact_id=None, created_since=None, document_category_id=None, external_property_name=None, external_property_value=None, fields=None, ids=None, include_deleted=None, limit=None, matter_id=None, order=None, page_token=None, parent_id=None, query=None, scope=None, updated_since=None) -> web.Response:
    """Return the data for all Folders

    Outlines the parameters, optional and required, used when requesting the data for all Folders

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type contact_id: int
    :param created_since: Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param document_category_id: The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type document_category_id: int
    :param external_property_name: Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; 
    :type external_property_name: str
    :param external_property_value: Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; 
    :type external_property_value: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Folder records to those having the specified unique identifiers.
    :type ids: int
    :param include_deleted: Allow trashed Folder record to be included.
    :type include_deleted: bool
    :param limit: A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type matter_id: int
    :param order: Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param parent_id: The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. 
    :type parent_id: int
    :param query: Wildcard search for &#x60;name&#x60; matching the given string.
    :type query: str
    :param scope: Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.
    :type scope: str
    :param updated_since: Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def folder_list(request: web.Request, x_api_version=None, contact_id=None, created_since=None, document_category_id=None, external_property_name=None, external_property_value=None, fields=None, ids=None, include_deleted=None, limit=None, matter_id=None, order=None, page_token=None, parent_id=None, query=None, scope=None, show_uncompleted=None, updated_since=None) -> web.Response:
    """Return the data of the contents of a Folder

    Return the data of the contents of a Folder. 

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param contact_id: The unique identifier for a single Contact. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type contact_id: int
    :param created_since: Filter Folder records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param document_category_id: The unique identifier for a single DocumentCategory. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type document_category_id: int
    :param external_property_name: Filter records to only those with the given external property(s) name set.  e.g. &#x60;?external_property_name&#x3D;Name&#x60; 
    :type external_property_name: str
    :param external_property_value: Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. &#x60;?external_property_name&#x3D;Name&amp;external_property_value&#x3D;Value&#x60; 
    :type external_property_value: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter Folder records to those having the specified unique identifiers.
    :type ids: int
    :param include_deleted: Allow trashed Folder record to be included.
    :type include_deleted: bool
    :param limit: A limit on the number of Folder records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param matter_id: The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property.
    :type matter_id: int
    :param order: Orders the Folder records by the given field. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param parent_id: The unique identifier for a single Folder.  When returning the data of the contents of a Folder, the keyword &#x60;null&#x60; is not valid for this field. If no Folder is provided, it will default to the account&#39;s root Folder.  When returning the data for all Folders, use the keyword &#x60;null&#x60; to match those without a Folder. The list will be filtered to include only the Folder records with the matching property. 
    :type parent_id: int
    :param query: Wildcard search for &#x60;name&#x60; matching the given string.
    :type query: str
    :param scope: Filters Folder record to those being a child of the parent Folder, or a descendant of the parent Folder. Default is &#x60;children&#x60;.
    :type scope: str
    :param show_uncompleted: Allow Folder record being uploaded to be included.
    :type show_uncompleted: bool
    :param updated_since: Filter Folder records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def folder_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Folder

    Outlines the parameters, optional and required, used when requesting the data for a single Folder

    :param id: The unique identifier for the Folder.
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


async def folder_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Update a single Folder

    Update Folder, move Folder to another Folder, and/or restore a trashed Folder. 

    :param id: The unique identifier for the Folder.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Folders
    :type body: dict | bytes

    """
    body = FolderUpdateRequest.from_dict(body)
    return web.Response(status=200)
