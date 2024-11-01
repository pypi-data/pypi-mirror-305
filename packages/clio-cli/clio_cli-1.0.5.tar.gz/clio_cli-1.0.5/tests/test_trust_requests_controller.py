# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.trust_request_create_request import TrustRequestCreateRequest
from openapi_server.models.trust_request_show import TrustRequestShow


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_trust_request_create(client):
    """Test case for trust_request_create

    Create a new TrustRequest
    """
    body = openapi_server.TrustRequestCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/trust_requests.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

