# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_list import TaskList
from openapi_server.models.task_show import TaskShow
from openapi_server.models.task_update_request import TaskUpdateRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_task_create(client):
    """Test case for task_create

    Create a new Task
    """
    body = openapi_server.TaskCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/tasks.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_destroy(client):
    """Test case for task_destroy

    Delete a single Task
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/tasks/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_index(client):
    """Test case for task_index

    Return the data for all Tasks
    """
    params = [('assignee_id', 56),
                    ('assignee_type', 'assignee_type_example'),
                    ('assigner_id', 56),
                    ('cascading_source_id', 56),
                    ('client_id', 56),
                    ('complete', True),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('due_at_from', '2013-10-20'),
                    ('due_at_present', True),
                    ('due_at_to', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('permission', 'permission_example'),
                    ('priority', 'priority_example'),
                    ('query', 'query_example'),
                    ('responsible_attorney_id', 56),
                    ('status', 'status_example'),
                    ('statuses[]', 'statuses_example'),
                    ('statute_of_limitations', True),
                    ('task_type_id', 56),
                    ('time_entries_present', True),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/tasks.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_show(client):
    """Test case for task_show

    Return the data for a single Task
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
        path='/api/v4/tasks/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_task_update(client):
    """Test case for task_update

    Update a single Task
    """
    body = openapi_server.TaskUpdateRequest()
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
        path='/api/v4/tasks/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

