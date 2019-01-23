SHELL = /bin/bash

##
# Definitions.

.SUFFIXES:

PACKAGE_NAME = {{ cookiecutter.package_name }}
PACKAGE_VERSION = $(shell cat VERSION)

srcdir = $(CURDIR)/src/$(PACKAGE_NAME)



##
# Auxiliary targets.

.PHONY: help
# target: help – Display all callable targets
help:
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| $(SED) -r "s/^\s*#\s*target\s*:\s*//g"
	@echo

## Cleaners.

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

