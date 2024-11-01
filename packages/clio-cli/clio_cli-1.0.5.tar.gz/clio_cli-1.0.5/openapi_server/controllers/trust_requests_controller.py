from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.trust_request_create_request import TrustRequestCreateRequest
from openapi_server.models.trust_request_show import TrustRequestShow
from openapi_server import util


async def trust_request_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Create a new TrustRequest

    Outlines the parameters and data fields used when creating a new TrustRequest

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Trust Requests
    :type body: dict | bytes

    """
    body = TrustRequestCreateRequest.from_dict(body)
    return web.Response(status=200)
