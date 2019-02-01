#!/bin/sh
#
echo "Activating python virtual env..."
source $HOME/.venv/bin/activate

echo "Booting {{ cookiecutter.project_slug }} in ${BOOT_MODE} mode ..."

if [[ ${BOOT_MODE} == "development" ]]
then
  echo "INFO: User    :`id $(whoami)`"
  echo "INFO: Workdir :`pwd`"

  cd $HOME/services/{{ cookiecutter.project_slug }}
  $PIP install -r requirements/ci.txt
  $PIP install -e .
  $PIP list

  cd $HOME/
  {{ cookiecutter.command_line_interface_bin_name }} --config config-host-dev.yaml

elif [[ ${BOOT_MODE} == "debug" ]]
then
  echo "INFO: Debugger attached: https://docs.python.org/3.6/library/pdb.html#debugger-commands  ..."
  python -c "import pdb, {{ cookiecutter.package_name }}.cli; pdb.run('{{ cookiecutter.package_name }}.cli.main([\'-c\',\'config-container-prod.yaml\'])')"

elif [[ ${BOOT_MODE} == "production" ]]
then
  {{ cookiecutter.command_line_interface_bin_name }} --config config-container-prod.yaml

else
  echo "ERROR: ${BOOT_MODE} is invalid booting mode. Expecting development, debug or production"
fi
