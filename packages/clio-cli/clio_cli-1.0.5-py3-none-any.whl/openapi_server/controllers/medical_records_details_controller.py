from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest
from openapi_server.models.medical_records_request_list import MedicalRecordsRequestList
from openapi_server.models.medical_records_request_show import MedicalRecordsRequestShow
from openapi_server.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest
from openapi_server import util


async def medical_records_request_create(request: web.Request, x_api_version=None, fields=None, body=None) -> web.Response:
    """Creating a Medical Records Detail, Medical Records and Medical Bills

    This endpoint allows a creation of a Medical Records Detail, multiple Medical Records and Medical Bills. Medical Liens can also be created as a property under Medical Bills.  Reference the payload to see how the records are being passed in. 

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Medical Records Details
    :type body: dict | bytes

    """
    body = MedicalRecordsRequestCreateRequest.from_dict(body)
    return web.Response(status=200)


async def medical_records_request_destroy(request: web.Request, id, x_api_version=None) -> web.Response:
    """Destroying a Medical Records Detail

    When a Medical Records Detail is destroyed, the child records, such as Medical Records, Medical Bills and Liens will also be destroyed in the same transaction. 

    :param id: The unique identifier for the Medical Records Detail.
    :type id: int
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str

    """
    return web.Response(status=200)


async def medical_records_request_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, page_token=None, treatment_end_date=None, treatment_start_date=None, updated_since=None) -> web.Response:
    """Return the data for all Medical Records Details

    Outlines the parameters, optional and required, used when requesting the data for all Medical Records Details 

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter MedicalRecordsRequest records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter MedicalRecordsRequest records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of Medical Records Detail records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param treatment_end_date: Filters Medical Records data by treatment end date.
    :type treatment_end_date: str
    :param treatment_start_date: Filters Medical Records data by treatment start date.
    :type treatment_start_date: str
    :param updated_since: Filter MedicalRecordsRequest records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    treatment_end_date = util.deserialize_datetime(treatment_end_date)
    treatment_start_date = util.deserialize_datetime(treatment_start_date)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def medical_records_request_show(request: web.Request, id, if_modified_since=None, if_none_match=None, x_api_version=None, fields=None) -> web.Response:
    """Return the data for a single Medical Records Detail

    Outlines the parameters, optional and required, used when requesting the data for a single Medical Records Details 

    :param id: The unique identifier for the Medical Records Detail.
    :type id: int
    :param if_modified_since: The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).
    :type if_modified_since: str
    :param if_none_match: The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed.
    :type if_none_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    if_modified_since = util.deserialize_date(if_modified_since)
    return web.Response(status=200)


async def medical_records_request_update(request: web.Request, id, if_match=None, x_api_version=None, fields=None, body=None) -> web.Response:
    """Updating a Medical Records Detail

    If there are records being passed into the Medical Records or Medical Bills parameter they will be treated as new records and new Medical Records / Medical Bills will be created. 

    :param id: The unique identifier for the Medical Records Detail.
    :type id: int
    :param if_match: The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags).
    :type if_match: str
    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param body: Request Body for Medical Records Details
    :type body: dict | bytes

    """
    body = MedicalRecordsRequestUpdateRequest.from_dict(body)
    return web.Response(status=200)
