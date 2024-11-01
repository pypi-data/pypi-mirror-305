from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_contacts_list import MatterContactsList
from openapi_server import util


async def matter_contacts_index(request: web.Request, matter_id, x_api_version=None, custom_field_ids=None, fields=None, limit=None, order=None, page_token=None) -> web.Response:
    """Return the related contact data for a single matter

    Outlines the parameters, optional and required, used when requesting the data for all MatterContacts

    :param matter_id: Filters contact data by matter.
    :type matter_id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param custom_field_ids: IDs of custom fields to include in results.
    :type custom_field_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param limit: A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param order: Orders the MatterContacts records by the given field. Note that &#x60;id&#x60; is ordered by the &#x60;id&#x60; of the nested Relationship record. Default: &#x60;is_client(asc)&#x60;.
    :type order: str
    :param page_token: A token specifying which page to return.
    :type page_token: str

    """
    return web.Response(status=200)
