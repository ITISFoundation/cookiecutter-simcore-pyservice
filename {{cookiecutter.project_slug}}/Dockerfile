# TODO: this is still not finished!!
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
ENV PIP  /home/scu/.venv/bin/pip3

EXPOSE 8080

# -------------------------- Build stage -------------------
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
    $PIP install --no-cache-dir --upgrade \
      pip \
      wheel \
      setuptools

WORKDIR /home/scu

# install base 3rd party packages to accelerate runtime installs
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/requirements/base.txt requirements-base.txt
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/docker docker
RUN chmod +x docker/boot.sh &&\
    chmod +x docker/entrypoint.sh
RUN $PIP install --no-cache-dir -r requirements-base.txt

# --------------------------Development stage -------------------
FROM build as development

ARG HOST_GID_ARG=1000

# install test 3rd party packages to accelerate runtime installs
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }}/requirements/ci.txt requirements-ci.txt
RUN $PIP install --no-cache-dir -r requirements-ci.txt

# in dev mode we give access to `scu` to host's mapped volumes
RUN addgroup -g $HOST_GID_ARG hgrp &&\
    addgroup scu hgrp && \
    chown -R scu:scu $HOME/.venv

VOLUME /home/scu/packages
VOLUME /home/scu/services/{{ cookiecutter.project_slug }}/

ENV BOOT_MODE development
ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD docker/boot.sh


# --------------------------Production multi-stage -------------------
#FROM build as build-production
FROM build as production

ENV SIMCORE_WEB_CONFIG production

# 2nd party packages
COPY --chown=scu:scu packages $HOME/packages
# server
COPY --chown=scu:scu services/{{ cookiecutter.project_slug }} $HOME/services/{{ cookiecutter.project_slug }}

WORKDIR /home/scu/services/{{ cookiecutter.project_slug }}
RUN $PIP install --no-cache-dir -r requirements/base.txt &&\
    $PIP install --no-cache-dir . &&\
    $PIP list

#-------------------
#FROM base as production
# TODO: PC some basic package missing

#COPY --from=build-production --chown=scu:scu $HOME/services/server/boot.sh $HOME
#COPY --from=build-production --chown=scu:scu $HOME/.venv $HOME/.venv
#RUN . $HOME/.venv/bin/activate; pip list

# FIXME: temporary solution until found missing packages
WORKDIR /home/scu

RUN . $HOME/.venv/bin/activate; pip list &&\
    rm -rf $HOME/packages &&\
    rm -rf $HOME/services/{{ cookiecutter.project_slug }}

ENV BOOT_MODE production
ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD docker/boot.sh
