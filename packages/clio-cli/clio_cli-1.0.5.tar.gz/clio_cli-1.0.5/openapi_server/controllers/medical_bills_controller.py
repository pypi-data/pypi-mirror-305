from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.medical_bill_show import MedicalBillShow
from openapi_server.models.medical_bill_update_request import MedicalBillUpdateRequest
from openapi_server import util


async def medical_bill_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Destroying a Medical Bill

    Outlines the parameters, optional and required, used when deleting the record for a single Medical Bill 

    :param id: The unique identifier for the Medical Bill.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def medical_bill_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Updating a Medical Bill

    Outlines the parameters and data fields used when updating a single Medical Bill 

    :param id: The unique identifier for the Medical Bill.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Medical Bills
    :type body: dict | bytes

    """
    body = MedicalBillUpdateRequest.from_dict(body)
    return web.Response(status=200)
