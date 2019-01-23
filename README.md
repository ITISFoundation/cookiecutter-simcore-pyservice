# Cookiecutter simcore-pyservice
[![Build Status](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice.svg?branch=master)](https://travis-ci.com/ITISFoundation/cookiecutter-simcore-pyservice)

Cookiecutter template for [osparc-simcore]'s python-based services

This template was built upon ideas/snippets borrowed from already existing great [cookiecutter]s such as [gh:ionelmc/cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary), [gh:alexkey/cookiecutter-lux-python](https://github.com/alexkey/cookiecutter-lux-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) or [gh:mdklatt/cookiecutter-python-app](https://github.com/mdklatt/cookiecutter-python-app).

## Requirements
Install `cookiecutter` command line: `pip install cookiecutter`


## Usage
Generate a new Cookiecutter template layout: `cookiecutter gh:itisfoundation/cookiecutter-simcore-pyservice`    


## Development

- ``.vscode-template`` are recommended settings for vscode

``` bash
# creates virtual-environment, and runs current cookie-cutter if 'output' does not exists
make run

```


## License
This project is licensed under the terms of the [MIT License](/LICENSE)

[cookiecutter]:https://github.com/audreyr/cookiecutter
[osparc-simcore]:https://github.com/ITISFoundation/osparc-simcore