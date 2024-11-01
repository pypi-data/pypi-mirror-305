from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.related_contacts_list import RelatedContactsList
from openapi_server import util


async def related_contacts_index(request: web.Request, matter_id, x_api_version=None, fields=None, limit=None, order=None, page_token=None) -> web.Response:
    """Return the related contact data for a single matter

    Outlines the parameters, optional and required, used when requesting the data for all RelatedContacts

    :param matter_id: Filters RelatedContacts data by matter.
    :type matter_id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param limit: A limit on the number of RelatedContacts records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the RelatedContacts records by the given field. Note that &#x60;id&#x60; is ordered by the &#x60;id&#x60; of the nested Relationship record. Default: &#x60;id(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str

    """
    return web.Response(status=200)
