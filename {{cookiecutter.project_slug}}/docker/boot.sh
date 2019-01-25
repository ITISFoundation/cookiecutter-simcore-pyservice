#!/bin/sh
echo "Activating python virtual env..."
source $HOME/.venv/bin/activate

if [[ ${DEBUG} == "1" ]]
then
  echo "Booting in development mode ..."
  echo "DEBUG: User    :`id $(whoami)`"
  echo "DEBUG: Workdir :`pwd`"

  cd $HOME/services/{{ cookiecutter.project_slug }}
  pip install -r requirements/base.txt
  pip install -r requirements/tests.txt
  pip install -e .
  pip list

  cd $HOME/
  {{ cookiecutter.command_line_interface_bin_name }} --config config-host-dev.yaml

elif [[ ${DEBUG} == "2" ]]
then
  echo "Booting with debugger attached: https://docs.python.org/3.6/library/pdb.html#debugger-commands  ..."
  python -c "import pdb, {{ cookiecutter.package_name }}.cli; pdb.run('{{ cookiecutter.package_name }}.cli.main([\'-c\',\'config-container-prod.yaml\'])')"

else
  echo "Booting in production mode ..."
  {{ cookiecutter.command_line_interface_bin_name }} --config config-container-prod.yaml
fi
