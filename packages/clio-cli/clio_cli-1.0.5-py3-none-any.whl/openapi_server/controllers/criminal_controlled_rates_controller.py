from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList
from openapi_server import util


async def lauk_criminal_controlled_rate_index(request: web.Request, x_api_version=None, activity=None, category_of_law=None, counsel=None, court=None, fields=None, key=None, limit=None, page_token=None, rate_type=None, region=None, solicitor_type=None) -> web.Response:
    """List Criminal Controlled Rates

    Outlines the parameters, optional and required, used when requesting the data for all LaukCriminalControlledRates

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param activity: Filter by activity.
    :type activity: str
    :param category_of_law: Filter by category of law.
    :type category_of_law: str
    :param counsel: Filter by counsel.
    :type counsel: str
    :param court: Filter by court.
    :type court: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param key: Filter by key.
    :type key: str
    :param limit: A limit on the number of LaukCriminalControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param rate_type: Filter by rate type.
    :type rate_type: str
    :param region: Filter by region.
    :type region: str
    :param solicitor_type: Filter by solicitor type.
    :type solicitor_type: str

    """
    return web.Response(status=200)
