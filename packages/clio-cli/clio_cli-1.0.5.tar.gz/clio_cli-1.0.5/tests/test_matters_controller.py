# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.matter_create_request import MatterCreateRequest
from openapi_server.models.matter_list import MatterList
from openapi_server.models.matter_show import MatterShow
from openapi_server.models.matter_update_request import MatterUpdateRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_matter_create(client):
    """Test case for matter_create

    Create a new Matter
    """
    body = openapi_server.MatterCreateRequest()
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/matters.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_destroy(client):
    """Test case for matter_destroy

    Delete a single Matter
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/matters/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_index(client):
    """Test case for matter_index

    Return the data for all Matters
    """
    params = [('billable', True),
                    ('client_id', 56),
                    ('close_date[]', 'close_date_example'),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('custom_field_ids[]', 56),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('fields', 'fields_example'),
                    ('grant_id', 56),
                    ('group_id', 56),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('notification_event_subscriber_user_id', 56),
                    ('open_date[]', 'open_date_example'),
                    ('order', 'order_example'),
                    ('originating_attorney_id', 56),
                    ('page_token', 'page_token_example'),
                    ('pending_date[]', 'pending_date_example'),
                    ('practice_area_id', 56),
                    ('query', 'query_example'),
                    ('responsible_attorney_id', 56),
                    ('status', 'status_example'),
                    ('subscriber_user_id', 56),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/matters.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matter_show(client):
    """Test case for matter_show

    Return the data for a single Matter
    """
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'if_modified_since': '2013-10-20',
        'if_none_match': 'if_none_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/matters/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_matter_update(client):
    """Test case for matter_update

    Update a single Matter
    """
    body = openapi_server.MatterUpdateRequest()
    params = [('custom_field_ids[]', 56),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v4/matters/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

