# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billable_matter_list import BillableMatterList
from openapi_server.models.billable_matter_show import BillableMatterShow
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_billable_matter_ids(client):
    """Test case for billable_matter_ids

    Returns the unique identifiers of all BillableMatter
    """
    params = [('client_id', 56),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('end_date', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('originating_attorney_id', 56),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('responsible_attorney_id', 56),
                    ('start_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/billable_matters/ids.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billable_matter_index(client):
    """Test case for billable_matter_index

    Return the data for all BillableMatters
    """
    params = [('client_id', 56),
                    ('custom_field_values', 'custom_field_values_example'),
                    ('end_date', '2013-10-20'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('matter_id', 56),
                    ('originating_attorney_id', 56),
                    ('page_token', 'page_token_example'),
                    ('query', 'query_example'),
                    ('responsible_attorney_id', 56),
                    ('start_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/billable_matters.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

