# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar_entry_create_request import CalendarEntryCreateRequest
from openapi_server.models.calendar_entry_list import CalendarEntryList
from openapi_server.models.calendar_entry_show import CalendarEntryShow
from openapi_server.models.calendar_entry_update_request import CalendarEntryUpdateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_calendar_entry_create(client):
    """Test case for calendar_entry_create

    Create a new CalendarEntry
    """
    body = openapi_server.CalendarEntryCreateRequest()
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/calendar_entries.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_entry_destroy(client):
    """Test case for calendar_entry_destroy

    Delete a single CalendarEntry
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/calendar_entries/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_entry_index(client):
    """Test case for calendar_entry_index

    Return the data for all CalendarEntries
    """
    params = [('calendar_id', 56),
                    ('created_since', '2013-10-20T19:20:30+01:00'),
                    ('expanded', True),
                    ('external_property_name', 'external_property_name_example'),
                    ('external_property_value', 'external_property_value_example'),
                    ('fields', 'fields_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('has_court_rule', True),
                    ('ids[]', 56),
                    ('is_all_day', True),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('owner_entries_across_all_users', True),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('source', 'source_example'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('updated_since', '2013-10-20T19:20:30+01:00'),
                    ('visible', True)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/calendar_entries.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_entry_show(client):
    """Test case for calendar_entry_show

    Return the data for a single CalendarEntry
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
        path='/api/v4/calendar_entries/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_calendar_entry_update(client):
    """Test case for calendar_entry_update

    Update a single CalendarEntry
    """
    body = openapi_server.CalendarEntryUpdateRequest()
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
        path='/api/v4/calendar_entries/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

