# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_create_request import ActivityCreateRequest
from openapi_server.models.activity_list import ActivityList
from openapi_server.models.activity_show import ActivityShow
from openapi_server.models.activity_update_request import ActivityUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_create(client):
    """Test case for activity_create

    Create a new Activity
    """
    body = openapi_server.ActivityCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/activities.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_destroy(client):
    """Test case for activity_destroy

    Delete a single Activity
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/activities/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_index(client):
    """Test case for activity_index

    Return the data for all Activities
    """
    params = [('activity_description_id', 56),
                    ('calendar_entry_id', 56),
                    ('communication_id', 56),
                    ('contact_note_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('end_date', '2013-10-20T19:20:30+01:00'),
                    ('expense_category_id', 56),
                    ('fields', 'fields_example'),
                    ('flat_rate', True),
                    ('grant_id', 56),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('matter_note_id', 56),
                    ('only_unaccounted_for', True),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('start_date', '2013-10-20T19:20:30+01:00'),
                    ('status', 'status_example'),
                    ('task_id', 56),
                    ('type', 'type_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00'),
                    ('user_id', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/activities.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_show(client):
    """Test case for activity_show

    Return the data for a single Activity
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
        path='/api/v4/activities/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_update(client):
    """Test case for activity_update

    Update a single Activity
    """
    body = openapi_server.ActivityUpdateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v4/activities/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

