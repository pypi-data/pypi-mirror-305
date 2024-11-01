from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_metrics_show import EventMetricsShow
from openapi_server import util


async def event_metrics_index(request: web.Request, x_api_version=None, fields=None) -> web.Response:
    """Unread in-app notification events

    Outlines the parameters, optional and required, used when requesting Event Metrics

    :param x_api_version: The [API minor version](#section/Minor-Versions). Default: latest version.
    :type x_api_version: str
    :param fields: The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).
    :type fields: str

    """
    return web.Response(status=200)
