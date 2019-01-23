SHELL = /bin/bash

##
# Definitions.

.SUFFIXES:

PACKAGE_NAME = {{ cookiecutter.package_name }}
PACKAGE_VERSION = $(shell cat VERSION)

srcdir = $(CURDIR)/src/$(PACKAGE_NAME)


## Tools
tools =

ifeq ($(shell uname -s),Darwin)
	SED = gsed
else
	SED = sed
endif

ifeq ($(shell which ${SED}),)
	tools += $(SED)
endif

DOCKER = docker
ifeq ($(shell which ${DOCKER}),)
    tools += $(DOCKER)
endif

VENV_DIR = $(CURDIR)/.venv

PYTHON = python3
ifeq ($(shell which ${PYTHON}),)
    tools += $(PYTHON)
endif


## -------------------------------
# All.

all: help
ifdef tools
	$(error "Can't find tools:${tools}")
endif


## -------------------------------
# Virtual environment.

.PHONY: venv
# target: venv – Create the virtual environment
venv: $(VENV_DIR)

$(VENV_DIR):
	@$(PYTHON) -m venv "$(VENV_DIR)"
	@"$(VENV_DIR)/bin/pip3" install --upgrade pip wheel setuptools
	@echo "To activate the virtual environment, execute 'source $(VENV_DIR)/bin/activate'"

.PHONY: venv
# Create the virtual environment into venv folder
venv: $(VENV_DIR)
.venv: $(VENV_DIR)


## -------------------------------
# Auxiliary targets.

.PHONY: help
# target: help – Display all callable targets
help:
	@echo "$(PACKAGE_NAME):$(PACKAGE_VERSION)"
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| $(SED) -r "s/^\s*#\s*target\s*:\s*//g"
	@echo


## -------------------------------
# Cleaners.

.PHONY: clean
# target: clean – Clean the project's directrory
clean:
	@find "$(CURDIR)" \
		-name "*.py[cod]" -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	@rm -rfv \
		"$(CURDIR)/.cache" \
		"$(CURDIR)/.mypy_cache" \
		"$(CURDIR)/.pytest_cache"

