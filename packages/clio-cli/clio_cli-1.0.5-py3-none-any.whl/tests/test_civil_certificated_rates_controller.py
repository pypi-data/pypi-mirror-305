# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList


pytestmark = pytest.mark.asyncio

async def test_lauk_civil_certificated_rate_index(client):
    """Test case for lauk_civil_certificated_rate_index

    List Civil Certificated Rates
    """
    params = [('activity', 'activity_example'),
                    ('activity_sub_category', 'activity_sub_category_example'),
                    ('attended_several_hearings_for_multiple_clients', True),
                    ('category_of_law', 'category_of_law_example'),
                    ('change_of_solicitor', True),
                    ('court', 'court_example'),
                    ('eligible_for_sqm', True),
                    ('fee_scheme', 'fee_scheme_example'),
                    ('fields', 'fields_example'),
                    ('first_conducting_solicitor', True),
                    ('key', 'key_example'),
                    ('limit', 56),
                    ('number_of_clients', 'number_of_clients_example'),
                    ('page_token', 'page_token_example'),
                    ('party', 'party_example'),
                    ('post_transfer_clients_represented', 'post_transfer_clients_represented_example'),
                    ('rate_type', 'rate_type_example'),
                    ('region', 'region_example'),
                    ('session_type', 'session_type_example'),
                    ('user_type', 'user_type_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_api_version': 'x_api_version_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/lauk_civil_certificated_rates.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

