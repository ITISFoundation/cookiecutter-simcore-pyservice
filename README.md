# Cookiecutter simcore-pyservice
[![Build Status](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice.svg?branch=master)](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice)

Cookiecutter template for [osparc-simcore]'s python-based services


## Requirements

  - [python](https://www.python.org/) >=3.6
    - Install `cookiecutter` command line: `pip install cookiecutter`
  - [docker](https://www.docker.com/) [optional]
  - [the internet](https://youtu.be/iDbyYGrswtg?t=3)

## Usage
To generate a new cookiecutter template layout just type

```console
 $ cookiecutter gh:itisfoundation/cookiecutter-simcore-pyservice
```
and answer the questions.

Then, to work in the backed project, this is the standard wordflow
``` console
  $ cd my project
  $ make help

  # Create and activate virtual envi
  $ make venv
  $ source .venv/bin/activate

  # freeze dependencies
  $ make requirements

  $ make
```

---

## Development

```console
$ make help

install – installs all tooling to run and test current cookie-cutter
run – runs cookiecutter into output folder
replay – replays cookiecutter using customized .cookiecutterrc-ignore
test – tests backed cookie
venv – Create the virtual environment into venv folder
requirements – Pip compile requirements.in
help – Display all callable targets
clean – cleans projects directory
clean-force – cleans & removes also venv folder
```

#### Features of the backed project
  - [aiohttp] server
  - [OpenAPI](https://www.openapis.org/) compatible RESTful API
  -
  - Predefined project skeleton
  - ``.vscode-template`` are recommended settings for vscode
  - ``{{cookiecutter.project_slug}}/extra`` contains code modules within a tree folder structure equivalent to [osparc-simcore] repo
  - makefile
  ```console
  $ make help
  simcore_service_dummy_service:0.1.0

  venv – Create the virtual environment
  install – Install project sources in "development mode"
  uninstall – Uninstall project sources
  test – Runs unit tests [w/ fail fast]
  help – Display all callable targets
  clean – Clean the project's directory
  ```

---

## Acknoledgements
This template was built upon ideas/snippets borrowed from already existing great [cookiecutter]s such as [gh:ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary), [gh:alexkey/cookiecutter-lux-python](https://github.com/alexkey/cookiecutter-lux-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) or [gh:mdklatt/cookiecutter-python-app](https://github.com/mdklatt/cookiecutter-python-app).

## License
This project is licensed under the terms of the [MIT License](/LICENSE)


[aiohptt]:https://aiohttp.readthedocs.io/en/stable/
[cookiecutter]:https://cookiecutter.readthedocs.io
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore
