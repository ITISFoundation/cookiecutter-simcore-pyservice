#/bin/bash
# TODO: unify scripts
exec {{ cookiecutter.simcore_install_root }}/scripts/openapi/openapi_codegen.sh \
    -i {{ cookiecutter.simcore_install_root }}/services/{{ cookiecutter.project_slug }}/src/{{ cookiecutter.package_name }}/oas3/{{cookiecutter.openapi_specs_version}}/openapi.yaml \
    -o . \
    -g python \
    -c ./codegen_config.json
