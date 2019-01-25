# Cookiecutter simcore-pyservice
[![Build Status](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice.svg?branch=master)](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice)

Cookiecutter template for [osparc-simcore]'s python-based services

This template was built upon ideas/snippets borrowed from already existing great [cookiecutter]s such as [gh:ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary), [gh:alexkey/cookiecutter-lux-python](https://github.com/alexkey/cookiecutter-lux-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) or [gh:mdklatt/cookiecutter-python-app](https://github.com/mdklatt/cookiecutter-python-app).

## Requirements
Install `cookiecutter` command line: `pip install cookiecutter`


## Usage
Generate a new Cookiecutter template layout: `cookiecutter gh:itisfoundation/cookiecutter-simcore-pyservice`


## Development

- main ``makefile``
```console
make help

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

- template folder:
  - ``.vscode-template`` are recommended settings for vscode
  - ``{{cookiecutter.project_slug}}/extra`` contains code modules within a tree folder structure equivalent to [osparc-simcore] repo

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


## License
This project is licensed under the terms of the [MIT License](/LICENSE)

[cookiecutter]:https://github.com/audreyr/cookiecutter
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore
