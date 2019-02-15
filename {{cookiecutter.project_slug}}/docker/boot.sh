#!/bin/sh
#

# BOOTING application ---------------------------------------------
echo "Booting in ${MY_BOOT_MODE} mode ..."

APP_CONFIG=config-host-dev.yaml

if [[ ${MY_BUILD_TARGET} == "development" ]]
  echo "  User    :`id $(whoami)`"
  echo "  Workdir :`pwd`"
  echo "  Environment :"
  printenv  | sed 's/=/: /' | sed 's/^/    /' | sort

  $MY_PIP install --user -e services/{{ cookiecutter.project_slug }}

  echo "  Python :"
  python --version | sed 's/^/    /'
  which python | sed 's/^/    /'
  echo "  PIP :"
  $MY_PIP list | sed 's/^/    /'

  APP_CONFIG=config-host-dev.yaml

elif [[ ${MY_BUILD_TARGET} == "production" ]]
  APP_CONFIG=config-host-dev.yaml

fi


# RUNNING application ----------------------------------------
if [[ ${BOOT_MODE} == "debug" ]]
then
  echo "Debugger attached: https://docs.python.org/3.6/library/pdb.html#debugger-commands  ..."
  echo "Running: import pdb, {{ cookiecutter.package_name }}.cli; pdb.run('{{ cookiecutter.package_name }}.cli.main([\'-c\',\'${APP_CONFIG}\'])')"
  python -c "import pdb, {{ cookiecutter.package_name }}.cli; \
             pdb.run('{{ cookiecutter.package_name }}.cli.main([\'-c\',\'${APP_CONFIG}\'])')"

else
  {{ cookiecutter.command_line_interface_bin_name }} --config $APP_CONFIG
fi
