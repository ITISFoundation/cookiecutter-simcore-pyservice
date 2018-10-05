SHELL = /bin/bash

##
# Definitions.

.SUFFIXES:

# Python virtual environment
VENV_DIR = $(CURDIR)/env


.PHONY: clean
clean:
	@find "$(CURDIR)" \
		-name "*.py[cod]" -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	@rm -rfv \
		"$(CURDIR)/.cache" \
		"$(CURDIR)/.mypy_cache" \
		"$(CURDIR)/.pytest_cache"	


.PHONY: install
install:
	. "$(VENV_DIR)/bin/activate" && pip install -r requirements-dev.txt


.PHONE: test
test:
	pytest


$(VENV_DIR):
	@python3 -m venv "$(CURDIR)/env"
	@"$(CURDIR)/env/bin/pip3" install --upgrade pip wheel setuptools
	@"$(CURDIR)/env/bin/pip3" install pylint
	@echo "To activate the virtual environment, execute 'source env/bin/activate'"

.PHONY: env
# target: env – Create the virtual environment
venv: $(VENV_DIR)