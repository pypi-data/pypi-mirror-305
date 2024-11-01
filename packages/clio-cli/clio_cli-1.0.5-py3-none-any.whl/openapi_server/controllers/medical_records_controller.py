from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.medical_record_show import MedicalRecordShow
from openapi_server.models.medical_record_update_request import MedicalRecordUpdateRequest
from openapi_server import util


async def medical_record_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Destroying a Medical Record

    Outlines the parameters, optional and required, used when deleting the record for a single MedicalRecord

    :param id: The unique identifier for the MedicalRecord.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def medical_record_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Updating a Medical Record

    Outlines the parameters and data fields used when updating a single MedicalRecord

    :param id: The unique identifier for the MedicalRecord.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Medical Records
    :type body: dict | bytes

    """
    body = MedicalRecordUpdateRequest.from_dict(body)
    return web.Response(status=200)
