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

PYTHON = python3
ifeq ($(shell which ${PYTHON}),)
	tools += $(PYTHON)
endif

VENV_DIR = $(CURDIR)/.venv
PIP=$(VENV_DIR)/bin/pip3


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
	@. "$(VENV_DIR)/bin/activate" && pip install --upgrade pip wheel setuptools
	@echo "To activate the virtual environment, execute 'source $(VENV_DIR)/bin/activate'"

.PHONY: venv
# Create the virtual environment into venv folder
venv: $(VENV_DIR)
.venv: $(VENV_DIR)


##
# Building and packaging.

.PHONY: requirements
# target: requirements – Compiles PiP requirements (.in->.txt)
requirements:
	pushd requirements && $(MAKE) -f Makefile all && popd


.PHONY: install
# target: install – Install project sources in "development mode"
install: requirements/base.txt requirements/ci.txt
	#pip install -r requirements/base.txt
	#pip install -r requirements/ci.txt
	#@$(PYTHON) setup.py develop
	pip-sync requirements/base.txt requirements/ci.txt
	pip install -e .


.PHONY: uninstall
# target: uninstall – Uninstall project sources
uninstall:
	@$(PYTHON) setup.py develop --uninstall


##
# Testing.

.PHONY: test
# target: test – Runs unit tests [w/ fail fast]
test:
	#@$(PYTHON) setup.py pytest --addopts tests/unit
	#"$(VENV_DIR)/bin/pytest" -x --log-level=warning tests/unit
	"pytest" -x --log-level=warning tests/unit


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
# target: clean – Clean the project's directory
clean:
	@find "$(CURDIR)" \
		-name "*.py[cod]" -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	@rm -rfv \
		"$(CURDIR)/.cache" \
		"$(CURDIR)/.mypy_cache" \
		"$(CURDIR)/.pytest_cache"
