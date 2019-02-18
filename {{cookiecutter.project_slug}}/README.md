# {{ cookiecutter.project_slug }}

[![](https://img.shields.io/microbadger/image-size/itisfoundation/{{ cookiecutter.project_slug }}./staging-latest.svg?label={{ cookiecutter.project_slug }}.&style=flat)](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }}. "More on itisfoundation/{{ cookiecutter.project_slug }}.:staging-latest image")

[![](https://images.microbadger.com/badges/image/itisfoundation/{{ cookiecutter.project_slug }}.svg)](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![](https://images.microbadger.com/badges/version/itisfoundation/{{ cookiecutter.project_slug }}.svg)](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![](https://images.microbadger.com/badges/commit/itisfoundation/{{ cookiecutter.project_slug }}.svg)](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")

{{ cookiecutter.project_short_description }}


## Development
```console
$ make help
```

Standard dev workflow is
``` console
$ make venv
$ source .venv/bin/activate

(.venv)$ make requirements
(.venv)$ make install

(.venv)$ make test
```
To start the service just check (some config files under ``{{cookiecutter.project_slug}}/src/{{cookiecutter.package_name}}/config`` )
```
$ {{ cookiecutter.command_line_interface_bin_name }} --help

$ {{ cookiecutter.command_line_interface_bin_name }} --config config-host-dev.yml
```
