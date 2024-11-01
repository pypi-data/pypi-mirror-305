from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_stage_list import MatterStageList
from openapi_server import util


async def matter_stage_index(request: web.Request, x_api_version=None, created_since=None, fields=None, ids=None, limit=None, page_token=None, practice_area_id=None, updated_since=None) -> web.Response:
    """Return the data for all MatterStages

    Outlines the parameters, optional and required, used when requesting the data for all MatterStages

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param created_since: Filter MatterStage records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type created_since: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str
    :param ids: Filter MatterStage records to those having the specified unique identifiers.
    :type ids: int
    :param limit: A limit on the number of MatterStage records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.
    :type limit: int
    :param page_token: A token specifying which page to return.
    :type page_token: str
    :param practice_area_id: The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterStage records with the matching property.
    :type practice_area_id: int
    :param updated_since: Filter MatterStage records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).
    :type updated_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)
