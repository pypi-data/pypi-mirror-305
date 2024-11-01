# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList


pytestmark = pytest.mark.asyncio

async def test_lauk_criminal_controlled_rate_index(client):
    """Test case for lauk_criminal_controlled_rate_index

    List Criminal Controlled Rates
    """
    params = [('activity', 'activity_example'),
                    ('category_of_law', 'category_of_law_example'),
                    ('counsel', 'counsel_example'),
                    ('court', 'court_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('limit', 56),
                    ('page_token', 'page_token_example'),
                    ('rate_type', 'rate_type_example'),
                    ('region', 'region_example'),
                    ('solicitor_type', 'solicitor_type_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/lauk_criminal_controlled_rates.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

