from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_version_list import DocumentVersionList
from openapi_server.models.error import Error
from openapi_server import util


async def document_version_index(request: web.Request, id, id2, x_api_version=None, fields=None, fully_uploaded=None, limit=None, page_token=None) -> web.Response:
    """Return the data for all DocumentVersions

    Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions

    :param id: The unique identifier for the DocumentVersion.
    :type id: int
    :param id2: ID of the Document
    :type id2: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param fully_uploaded: Filter DocumentVersion records to those with the given &#x60;fully_uploaded&#x60; status.
    :type fully_uploaded: bool
    :param limit: A limit on the number of DocumentVersion records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str

    """
    return web.Response(status=200)
