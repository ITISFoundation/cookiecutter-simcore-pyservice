""" Example of how to use the client-sdk of {{ cookiecutter.distribution_name }}

    pip install -v  git+https://github.com/itisfoundation/osparc-simcore.git@master#subdirectory=services/{{ cookiecutter.project_slug }}/client-sdk/python
"""
import asyncio
from contextlib import contextmanager

import {{ cookiecutter.sdk_package_name }}
from {{ cookiecutter.sdk_package_name }}.models import HealthInfo
from {{ cookiecutter.sdk_package_name }}.rest import ApiException


@contextmanager
def api_client(cfg):
    client = {{ cookiecutter.sdk_package_name }}.ApiClient(cfg)
    try:
        yield client
    except ApiException as err:
        print("%s\n" % err)
    finally:
        #NOTE: enforces to closing client session and connector.
        # this is a defect of the sdk
        del client.rest_client


async def run_test():
    cfg = {{ cookiecutter.sdk_package_name }}.Configuration()
    cfg.host = cfg.host.format(
        host="localhost",
        port=8080,
        version="{{ cookiecutter.openapi_specs_version }}"
    )

    with api_client(cfg) as client:
        session = client.rest_client.pool_manager
        print("LEN", len(session.cookie_jar))
        for cookie in session.cookie_jar:
            print(cookie.key)
        api = {{ cookiecutter.sdk_package_name }}.DefaultApi(client)
        res = await api.health_check()

        assert isinstance(res, HealthInfo)
        assert res.last_access == -1

        last_access = 0
        for _ in range(5):
            check = await api.health_check()
            print(check.last_access)
            assert last_access < check.last_access
            last_access = check.last_access


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_test())

if __name__ == "__main__":
    main()
