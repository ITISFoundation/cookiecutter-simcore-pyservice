# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import pytest

from aiohttp import web

from {{ cookiecutter.package_name }}.rest import setup_rest
from {{ cookiecutter.package_name }}.application_config import APP_CONFIG_KEY
from {{ cookiecutter.package_name }} import __version__

major_version = __version__.split('.')[0]
API_VERSION = f"v{major_version}""


@pytest.fixture
def client(loop, aiohttp_unused_port, aiohttp_client, api_specs_dir):
    app = web.Application()

    main_config={
        'port': aiohttp_unused_port(),
        'host': 'localhost'
    }

    # fake config
    app[APP_CONFIG_KEY] = {
        "main": main_config,
        "rest": {
            "version": API_VERSION,
            "location": str(api_specs_dir / API_VERSION / "openapi.yaml")
        }
    }

    # activates only restAPI sub-modules
    setup_rest(app, devel=True)

    cli = loop.run_until_complete( aiohttp_client(app, server_kwargs=main_config) )
    return cli

# ------------------------------------------

async def test_check_health(client):
    resp = await client.get("/%s/" % API_VERSION)
    payload = await resp.json()

    assert resp.status == 200, str(payload)
    data, error = tuple(payload.get(k) for k in ('data', 'error'))

    assert data
    assert not error

    assert data['name'] == '{{ cookiecutter.package_name }}'
    assert data['status'] == 'SERVICE_RUNNING'


async def test_check_action(client):
    QUERY = 'value'
    ACTION = 'echo'
    FAKE = {
        'path_value': 'one',
        'query_value': 'two',
        'body_value': {
            'a': 'foo',
            'b': '45'
        }
    }
    url = "/{ver}/check/{action}?data={query}".format(
        ver=API_VERSION,
        action=ACTION,
        query=QUERY)
    resp = await client.post(url, json=FAKE)
    payload = await resp.json()
    data, error = tuple(payload.get(k) for k in ('data', 'error'))

    assert resp.status == 200, str(payload)
    assert data
    assert not error

    {# TODO: validate response against specs #}
    assert data['path_value'] == ACTION
    assert data['query_value'] == QUERY
    assert data['body_value'] == FAKE
