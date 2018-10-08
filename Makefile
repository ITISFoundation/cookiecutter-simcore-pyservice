SHELL = /bin/bash

##
# Definitions.

.SUFFIXES:

# Python virtual environment
VENV_DIR = $(CURDIR)/venv
OUTPUT_DIR = $(CURDIR)/output


.PHONY: clean
clean:
	@find "$(CURDIR)" \
		-name "*.py[cod]" -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	@rm -rfv \
		"$(CURDIR)/.cache" \
		"$(CURDIR)/.mypy_cache" \
		"$(CURDIR)/.pytest_cache"	
	@rm -rf "$(VENV_DIR)"

.PHONY: install
install:
	. "$(VENV_DIR)/bin/activate" && pip install -r requirements-dev.txt


$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)
	. "$(VENV_DIR)/bin/activate" && cookiecutter "$(CURDIR)" --output-dir "$(OUTPUT_DIR)"

.PHONY: run
# target: run - Runs cookiecutter into output folder
run: $(OUTPUT_DIR)



.PHONE: test
test:
	pytest



$(VENV_DIR):
	@python3 -m venv "$(VENV_DIR)"
	@"$(VENV_DIR)/bin/pip3" install --upgrade pip wheel setuptools
	@"$(VENV_DIR)/bin/pip3" install pylint
	@echo "To activate the virtual environment, execute 'source env/bin/activate'"

.PHONY: venv
# target: env – Create the virtual environment into venv folder
venv: $(VENV_DIR)