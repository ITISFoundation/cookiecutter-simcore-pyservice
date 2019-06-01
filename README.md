# Cookiecutter simcore-pyservice
[![Build Status](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice.svg?branch=master)](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice)
[![Requirements Status](https://requires.io/github/ITISFoundation/cookiecutter-simcore-pyservice/requirements.svg?branch=master)](https://requires.io/github/ITISFoundation/cookiecutter-simcore-pyservice/requirements/?branch=master)
	
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


## Backed project

Infrastructure:
  - [osparc-simcore]-compatible project skeleton for python services
  - service-level makefile (type ``make help``)
  - [folder]({{cookiecutter.project_slug}}/extra_osparc-simcore) with stub code to integrate service in [osparc-simcore] framework
  - Multi-stage [Dockerfile]({{cookiecutter.project_slug}}/Dockerfile) with different boot modes and healt-check
  -
  - ...

Service Features:
  - [aiohttp] server
  - [OpenAPI](https://www.openapis.org/) compatible RESTful API
  - ...

Then, to work in the backed project, this is the standard wordflow
``` console
  $ cd my project
  $ make help

  # Create and activate virtual environment
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

---

## Acknoledgements
This template was built upon ideas/snippets borrowed from already existing great [cookiecutter]s such as [gh:ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary), [gh:alexkey/cookiecutter-lux-python](https://github.com/alexkey/cookiecutter-lux-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) or [gh:mdklatt/cookiecutter-python-app](https://github.com/mdklatt/cookiecutter-python-app).

## License
This project is licensed under the terms of the [MIT License](/LICENSE)


[aiohttp]:https://aiohttp.readthedocs.io/en/stable/
[cookiecutter]:https://cookiecutter.readthedocs.io
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore
