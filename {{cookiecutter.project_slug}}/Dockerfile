FROM python:3.6-alpine as base

LABEL maintainer={{ cookiecutter.github_username }}

#  USAGE:
#     cd sercices/{{ cookiecutter.project_slug }}
#     docker build -f Dockerfile -t {{ cookiecutter.project_slug }}:prod --target production ../../
#     docker run {{ cookiecutter.project_slug }}:prod
#
#  REQUIRED: context expected at ``osparc-simcore/`` folder because we need access to osparc-simcore/packages

# non-root user 'scu'
RUN adduser -D -u 8004 scu

RUN apk add --no-cache \
      su-exec

ENV HOME /home/scu
# TODO: Workaround for https://github.com/pypa/pip/issues/6197:
#   - Added explicit --cache-dir that is removed at the end of the build
#   - NOTE: After every PIP call, add rm -rf /tmp/.pipcache
ENV PIP /home/scu/.venv/bin/pip3 --cache-dir=/tmp/.pipcache

EXPOSE 8080


# -------------------------- Build stage -------------------
# Common stage between production and development targets
#
# + /home/scu/              $HOME
#    + packages
#        ...
#    + services/{{ cookiecutter.project_slug }}
#       + src
#       + tests
#
#
# TODO: straight copying python packages bring unnecessary files (e.g. __pycache__) -> dockerignore!
#       could copy and then python setup.py install OR git clone into the container.
#       This applies for both
#
FROM base as build

RUN apk add --no-cache \
      postgresql-dev \
      gcc \
      libc-dev \
      libffi-dev

RUN python3 -m venv $HOME/.venv &&\
    $PIP install --upgrade \
      pip \
      wheel \
      setuptools

WORKDIR /home/scu

# install base 3rd party packages to accelerate runtime installs
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/requirements/base.txt requirements-base.txt
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/docker docker
RUN chmod +x docker/boot.sh &&\
    chmod +x docker/entrypoint.sh
RUN $PIP install -r requirements-base.txt &&\
    rm -rf /tmp/.pipcache


# --------------------------Cache stage -------------------
# CI in master buils & pushes this target to speed-up image build
#
FROM build as cache

COPY --chown=scu:scu packages $HOME/packages
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }} $HOME/services/{{ cookiecutter.project_slug }}

WORKDIR /home/scu/services/{{ cookiecutter.project_slug }}
RUN $PIP install -r requirements/base.txt &&\
    $PIP install . &&\
    $PIP list &&\
    rm -rf /tmp/.pipcache

WORKDIR /home/scu
ENV BOOT_MODE production


# --------------------------Production stage -------------------
# Final cleanup up to reduce image size and startup setup
# TODO: optimize size by uninstalling dev tools? https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Remove_a_Package
#
FROM cache as production


# TODO: do we need to activate???
RUN $PIP list &&\
    rm -rf $HOME/packages &&\
    rm -rf $HOME/services/{{ cookiecutter.project_slug }} &&\
    rm -rf /tmp/.pipcache

ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD ["/bin/sh", "docker/boot.sh"]


# --------------------------Development stage -------------------
# Source code accessible in host but runs in container
# Placed at the end to speed-up the build if images targeting production
#
FROM build as development

ARG HOST_GID_ARG=1000

# install test 3rd party packages to accelerate runtime installs
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/requirements/ci.txt requirements-ci.txt
RUN $PIP install -r requirements-ci.txt &&\
    rm -rf /tmp/.pipcache

# in dev mode we give access to `scu` to host's mapped volumes
RUN addgroup -g $HOST_GID_ARG hgrp &&\
    addgroup scu hgrp &&\
    chown -R scu:scu $HOME/.venv

VOLUME /home/scu/packages
VOLUME /home/scu/services/{{ cookiecutter.project_slug }}/

ENV BOOT_MODE development
ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD docker/boot.sh
