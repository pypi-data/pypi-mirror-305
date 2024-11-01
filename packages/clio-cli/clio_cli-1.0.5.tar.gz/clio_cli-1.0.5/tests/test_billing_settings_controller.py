# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_setting_show import BillingSettingShow
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_billing_setting_show(client):
    """Test case for billing_setting_show

    Return the billing settings
    """
    params = [('duration', 'duration_example'),
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
        path='/api/v4/settings/billing.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

