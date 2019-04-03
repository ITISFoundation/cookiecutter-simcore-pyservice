FROM python:3.6-alpine as base
#
#  USAGE:
#     cd sercices/{{ cookiecutter.project_slug }}
#     docker build -f Dockerfile -t {{ cookiecutter.project_slug }}:prod --target production ../../
#     docker run {{ cookiecutter.project_slug }}:prod
#
#  REQUIRED: context expected at ``osparc-simcore/`` folder because we need access to osparc-simcore/packages

LABEL maintainer={{ cookiecutter.github_username }}

# simcore-user uid=8004(scu) gid=8004(scu) groups=8004(scu)
RUN adduser -D -u 8004 -s /bin/sh -h /home/scu scu

RUN apk add --no-cache \
      su-exec

ENV PATH "/home/scu/.local/bin:$PATH"

# All SC_ variables are customized
ENV SC_PIP pip3 --no-cache-dir
ENV SC_BUILD_TARGET base

EXPOSE 8080


# -------------------------- Build stage -------------------
# Installs build/package management tools and third party dependencies
#
# + /build             WORKDIR
#
{# SEE https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management #}
{#  SEE https://pip.pypa.io/en/stable/reference/pip_install              #}
FROM base as build

ENV SC_BUILD_TARGET build

{# TODO: install and uninstall lists #}
RUN apk add --no-cache \
      # postgresql-dev \
      # libc-dev \
      # libffi-dev \
      gcc \
      git

RUN $SC_PIP install --upgrade \
      pip \
      wheel \
      setuptools

WORKDIR /build

# install base 3rd party dependencies
COPY  services/{{ cookiecutter.project_slug }}/requirements/*.txt \
      services/{{ cookiecutter.project_slug }}/requirements/

RUN $SC_PIP install \
      -r services/{{ cookiecutter.project_slug }}/requirements/base.txt


# --------------------------Cache stage -------------------
# CI in master buils & pushes this target to speed-up image build
#
#  + /build
#    + services/{{ cookiecutter.project_slug }} [scu:scu] WORKDIR
#
FROM build as cache

ENV SC_BUILD_TARGET cache

{# TODO: Consider .dockerignore filter to avoid #}
COPY --chown=scu:scu packages /build/packages
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }} /build/services/{{ cookiecutter.project_slug }}

WORKDIR /build/services/{{ cookiecutter.project_slug }}

{# NOTE: notice that tests are not installed within the docker. Currently pytest runs in the host #}
RUN $SC_PIP install . &&\
    $SC_PIP list -v


# --------------------------Production stage -------------------
# Final cleanup up to reduce image size and startup setup
# Runs as scu (non-root user)
#
#  + /home/scu     $HOME = WORKDIR
#    + services/{{ cookiecutter.project_slug }} [scu:scu]
#
FROM cache as production

ENV SC_BUILD_TARGET production
ENV SC_BOOT_MODE production

WORKDIR /home/scu

RUN mkdir -p services/{{ cookiecutter.project_slug }} &&\
    chown scu:scu services/{{ cookiecutter.project_slug }} &&\
    mv /build/services/{{ cookiecutter.project_slug }}/docker services/{{ cookiecutter.project_slug }}/docker &&\
    rm -rf /build

{# TODO: optimize size by uninstalling dev tools? https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Remove_a_Package   #}
RUN apk del --no-cache\
      gcc \
      git

{# Shall guarantee maximum startup time limit per service. See https://12factor.net/ #}
HEALTHCHECK --interval=30s \
            --timeout=20s \
            --start-period=30s \
            --retries=3 \
            CMD ["python3", "services/{{ cookiecutter.project_slug }}/docker/healthcheck.py", "http://localhost:8080/{{ cookiecutter.openapi_specs_version }}/"]

ENTRYPOINT [ "/bin/sh", "services/{{ cookiecutter.project_slug }}/docker/entrypoint.sh" ]
CMD ["/bin/sh", "services/{{ cookiecutter.project_slug }}/docker/boot.sh"]


# --------------------------Development stage -------------------
# Source code accessible in host but runs in container
# Runs as myu with same gid/uid as host
# Placed at the end to speed-up the build if images targeting production
#
#  + /devel         WORKDIR
#    + services  (mounted volume)
#
FROM build as development

ENV SC_BUILD_TARGET development
ENV SC_BOOT_MODE development

{# TODO: Now could be moved after build to speed up ... or keep it here to enforce developer to build at least once. Reuses build-stage data #}
{# TODO: consider installing tooling in a separate virtualenv? #}
{# TODO: really necesary??? #}
WORKDIR /build
{# RUN $SC_PIP install -r services/{{ cookiecutter.project_slug }}/requirements/ci.txt #}

WORKDIR /devel
VOLUME  /devel/packages
VOLUME  /devel/services/{{ cookiecutter.project_slug }}/

ENTRYPOINT ["/bin/sh", "services/{{ cookiecutter.project_slug }}/docker/entrypoint.sh"]
CMD ["/bin/sh", "services/{{ cookiecutter.project_slug }}/docker/boot.sh"]
