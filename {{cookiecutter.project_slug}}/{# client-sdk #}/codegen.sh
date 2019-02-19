#/bin/bash
# FIXME: activate when ITIFoundation/openapi-tools:latest available
exec {{ cookiecutter.simcore_install_root }}../scripts/openapi/openapi_codegen.sh \
    -i ../src/{{ cookiecutter.package_name }}/oas3/{{cookiecutter.openapi_specs_version}}/openapi.yaml \
    -o . \
    -g python \
    -c ./codegen_config.json
