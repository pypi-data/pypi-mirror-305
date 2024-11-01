from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList
from openapi_server import util


async def lauk_civil_controlled_rate_index(request: web.Request, x_api_version=None, activity=None, category_of_law=None, fields=None, key=None, limit=None, page_token=None, rate_type=None, region=None) -> web.Response:
    """List Civil Controlled Rates

    Outlines the parameters, optional and required, used when requesting the data for all LaukCivilControlledRates

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param activity: Filter by activity.
    :type activity: str
    :param category_of_law: Filter by category of law.
    :type category_of_law: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param key: Filter by key.
    :type key: str
    :param limit: A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param rate_type: Filter by rate type.
    :type rate_type: str
    :param region: Filter by region.
    :type region: str

    """
    return web.Response(status=200)
