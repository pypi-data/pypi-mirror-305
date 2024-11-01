# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_description_create_request import ActivityDescriptionCreateRequest
from openapi_server.models.activity_description_list import ActivityDescriptionList
from openapi_server.models.activity_description_show import ActivityDescriptionShow
from openapi_server.models.activity_description_update_request import ActivityDescriptionUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_description_create(client):
    """Test case for activity_description_create

    Create a new ActivityDescription
    """
    body = openapi_server.ActivityDescriptionCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/activity_descriptions.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_description_destroy(client):
    """Test case for activity_description_destroy

    Delete a single ActivityDescription
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/activity_descriptions/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_description_index(client):
    """Test case for activity_description_index

    Return the data for all ActivityDescriptions
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('flat_rate', True),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('page_token', 'page_token_example'),
                    ('rate_for[matter_id]', 56),
                    ('rate_for[user_id]', 56),
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
        path='/api/v4/activity_descriptions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_description_show(client):
    """Test case for activity_description_show

    Return the data for a single ActivityDescription
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
        path='/api/v4/activity_descriptions/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_description_update(client):
    """Test case for activity_description_update

    Update a single ActivityDescription
    """
    body = openapi_server.ActivityDescriptionUpdateRequest()
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
        path='/api/v4/activity_descriptions/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

