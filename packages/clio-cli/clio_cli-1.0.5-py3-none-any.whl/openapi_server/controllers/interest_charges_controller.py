from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.interest_charge_list import InterestChargeList
from openapi_server import util


async def interest_charge_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Delete a single InterestCharge

    Outlines the parameters, optional and required, used when deleting the record for a single InterestCharge

    :param id: The unique identifier for the InterestCharge.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def interest_charge_index(request: web.Request, x_api_version=None, bill_id=None, created_since=None, exclude_ids=None, fields=None, ids=None, limit=None, page_token=None, updated_since=None) -> web.Response:
    """Return the data for all InterestCharges

    Outlines the parameters, optional and required, used when requesting the data for all InterestCharges

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param bill_id: The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property.
    :type bill_id: int
    :param created_since: Filter InterestCharge records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param exclude_ids: Array containing *InterestCharge* identifiers that should be excluded from the query.
    :type exclude_ids: int
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter InterestCharge records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param updated_since: Filter InterestCharge records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)
