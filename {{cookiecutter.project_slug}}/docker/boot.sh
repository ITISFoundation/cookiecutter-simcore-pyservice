#!/bin/sh
echo "Activating python virtual env..."
source $HOME/.venv/bin/activate

if [[ ${DEBUG} == "1" ]]
then
  echo "Booting in development mode ..."
  echo "DEBUG: User    :`id $(whoami)`"
  echo "DEBUG: Workdir :`pwd`"

  cd $HOME/services/{{ cookiecutter.project_slug }}
  pip install -r requirements/dev.txt
  pip list

  cd $HOME/  
  {{ cookiecutter.command_line_interface_bin_name }} --config config-dev.yaml
else
  echo "Booting in production mode ..."
  {{ cookiecutter.command_line_interface_bin_name }} --config config-prod.yaml
fi
