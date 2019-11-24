# Makefile config
.DEFAULT_GOAL := help
SHELL = /bin/bash

# Custom variables
VENV_DIR = $(CURDIR)/.venv
OUTPUT_DIR = $(CURDIR)/output
TEMPLATE = $(CURDIR)



$(VENV_DIR):
	# intalling virtual env
	@python3 -m venv $@
	# updating to latest pip
	@$@/bin/pip3 install --upgrade pip wheel setuptools
	@echo "To activate the virtual environment, execute 'source $(notdir $@)/bin/activate'"


requirements.txt: requirements.in ## Pip compile requirements.in
	# compiling requirements
	@pip-compile -v --output-file requirements.txt $<


.PHONY: devenv
devenv: requirements.txt $(VENV_DIR) ## installs all tooling to run and test current cookie-cutter
	# installing development environment
	@$(VENV_DIR)/bin/pip install -r $<


$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)/packages
	@mkdir -p $(OUTPUT_DIR)/services
	$(VENV_DIR)/bin/cookiecutter --output-dir "$(OUTPUT_DIR)/services" "$(TEMPLATE)"


play: $(OUTPUT_DIR) ## runs cookiecutter into output folder
	@touch play


.PHONY: replay
replay: play ## replays cookiecutter in output directory
	@$(VENV_DIR)/bin/cookiecutter \
			--no-input -f \
			--config-file="$(shell find $(OUTPUT_DIR) -name ".cookiecutterrc" | tail -n 1)"  \
			--output-dir="$(OUTPUT_DIR)/services" "$(TEMPLATE)"


.PHONY: test
test: ## tests backed cookie
	@$(VENV_DIR)/bin/pytest -s -c $(CURDIR)/pytest.ini


.PHONY: help
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## this colorful help
	@echo "Targets order display the common workflow:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)



.PHONY: clean clean-all
clean: ## cleans projects directory (except venv)
	# Cleaning outputs
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	@echo -n "$(shell whoami), are you REALLY sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	# cleaning caches and compiled files
	@find "$(CURDIR)" \
		-name "*.py[cod]" -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	@rm -rfv \
		"$(CURDIR)/.cache" \
		"$(CURDIR)/.mypy_cache" \
		"$(CURDIR)/.pytest_cache"
	# cleaning $(OUTPUT_DIR)
	@rm -rf "$(OUTPUT_DIR)"
	@rm play

clean-all: clean ## cleas both projects and devenv
	@rm -rf "$(VENV_DIR)"
