# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList
from openapi_server.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow


pytestmark = pytest.mark.asyncio

async def test_jurisdictions_to_trigger_index(client):
    """Test case for jurisdictions_to_trigger_index

    Return the data for all triggers
    """
    params = [('created_since', '2013-10-20T19:20:30+01:00'),
                    ('fields', 'fields_example'),
                    ('ids[]', 56),
                    ('is_requirements_required', True),
                    ('is_served', True),
                    ('limit', 56),
                    ('order', 'order_example'),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('updated_since', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/court_rules/jurisdictions/{jurisdiction_id}/triggers.json'.format(jurisdiction_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jurisdictions_to_trigger_show(client):
    """Test case for jurisdictions_to_trigger_show

    Return the data for the trigger
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
        path='/api/v4/court_rules/jurisdictions/{jurisdiction_id}/triggers/{id_jso}'.format(id=56, jurisdiction_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

