# pylint: disable=W0621
# TODO: W0611:Unused import ...
# pylint: disable=W0611
# W0612:Unused variable
# TODO: W0613:Unused argument ...
# pylint: disable=W0613
import pytest

from aiohttp import web

from {{ cookiecutter.package_name }}.settings import APP_CONFIG_KEY
from {{ cookiecutter.package_name }}.rest import setup_rest
from {{ cookiecutter.package_name }}.session import setup_session


@pytest.fixture
def client(loop, aiohttp_unused_port, aiohttp_client):
    app = web.Application()

    server_kwargs={'port': aiohttp_unused_port(), 'host': 'localhost'}
        
    app[APP_CONFIG_KEY] = { 'main': server_kwargs } # Fake config

    # loads only two submodules
    setup_session(app)
    setup_rest(app)

    cli = loop.run_until_complete( aiohttp_client(app, server_kwargs=server_kwargs) )
    return cli

async def test_health_check(client):
    resp = await client.get("/v0/")
    assert resp.status == 200

    envelope = await resp.json()
    data, error = [envelope[k] for k in ('data', 'error')]

    assert data
    assert not error

    assert data['name'] == '{{ cookiecutter.package_name }}'
    assert data['status'] == 'SERVICE_RUNNING'


async def test_action_check(client):
    QUERY = '{{ cookiecutter.github_username }}'
    ACTION = 'echo'
    FAKE = {
        'path_value': 'one',
        'query_value': 'two',
        'body_value': {
            'a': 33,
            'b': 45
        }
    }

    resp = await client.post("/v0/check/{}?data={}".format(ACTION, QUERY), json=FAKE)
    payload = await resp.json()

    data, error = tuple( payload.get(k) for k in ('data', 'error') )

    assert resp.status == 200, str(payload)
    assert data
    assert not error

    # TODO: validate response against specs

    assert data['path_value'] == ACTION
    assert data['query_value'] == QUERY
    #assert data['body_value'] == FAKE['body_value']
