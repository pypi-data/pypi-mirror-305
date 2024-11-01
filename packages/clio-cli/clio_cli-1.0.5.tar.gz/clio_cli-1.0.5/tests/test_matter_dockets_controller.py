# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_docket_create_request import MatterDocketCreateRequest
from openapi_server.models.matter_docket_list import MatterDocketList
from openapi_server.models.matter_docket_show import MatterDocketShow


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_matter_docket_create(client):
    """Test case for matter_docket_create

    Creates a matter docket
    """
    body = openapi_server.MatterDocketCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/court_rules/matter_dockets.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_docket_destroy(client):
    """Test case for matter_docket_destroy

    Deletes the requested matter docket
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/court_rules/matter_dockets/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_docket_index(client):
    """Test case for matter_docket_index

    Return the data for all matter dockets
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('matter_status', 'matter_status_example'),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('service_type_id', 56),
                    ('status', 'status_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/court_rules/matter_dockets.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_docket_preview(client):
    """Test case for matter_docket_preview

    Preview calendar dates for the docket
    """
    params = [('event_prefix', 'event_prefix_example'),
                    ('jurisdiction[id]', 56),
                    ('service_type[id]', 56),
                    ('start_date', '2013-10-20T19:20:30+01:00'),
                    ('start_time', '2013-10-20T19:20:30+01:00'),
                    ('trigger[id]', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/court_rules/matter_dockets/preview.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_docket_show(client):
    """Test case for matter_docket_show

    Return the data for the matter docket
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'if_modified_since': '2013-10-20',
        'if_none_match': 'if_none_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/court_rules/matter_dockets/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

