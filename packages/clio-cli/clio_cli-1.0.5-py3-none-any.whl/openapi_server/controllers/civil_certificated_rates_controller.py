from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList
from openapi_server import util


async def lauk_civil_certificated_rate_index(request: web.Request, x_api_version=None, activity=None, activity_sub_category=None, attended_several_hearings_for_multiple_clients=None, category_of_law=None, change_of_solicitor=None, court=None, eligible_for_sqm=None, fee_scheme=None, fields=None, first_conducting_solicitor=None, key=None, limit=None, number_of_clients=None, page_token=None, party=None, post_transfer_clients_represented=None, rate_type=None, region=None, session_type=None, user_type=None) -> web.Response:
    """List Civil Certificated Rates

    Outlines the parameters, optional and required, used when requesting the data for all LaukCivilCertificatedRates

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param activity: Filter by activity.
    :type activity: str
    :param activity_sub_category: Filter by activity sub-category.
    :type activity_sub_category: str
    :param attended_several_hearings_for_multiple_clients: Filter by whether multiple hearings were attended for multiple clients.
    :type attended_several_hearings_for_multiple_clients: bool
    :param category_of_law: Filter by category of law.
    :type category_of_law: str
    :param change_of_solicitor: Filter by change of solicitor status.
    :type change_of_solicitor: bool
    :param court: Filter by court.
    :type court: str
    :param eligible_for_sqm: Filter by SQM eligibility.
    :type eligible_for_sqm: bool
    :param fee_scheme: Fee scheme
    :type fee_scheme: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param first_conducting_solicitor: Filter by first conducting solicitor status.
    :type first_conducting_solicitor: bool
    :param key: Filter by key.
    :type key: str
    :param limit: A limit on the number of LaukCivilCertificatedRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param number_of_clients: Filter by number of clients.
    :type number_of_clients: str
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param party: Filter by party.
    :type party: str
    :param post_transfer_clients_represented: Filter by post-transfer clients represented.
    :type post_transfer_clients_represented: str
    :param rate_type: Filter by rate type.
    :type rate_type: str
    :param region: Filter by region.
    :type region: str
    :param session_type: Filter by session type.
    :type session_type: str
    :param user_type: Filter by user type.
    :type user_type: str

    """
    return web.Response(status=200)
