clean:
	@rm -rf `find . -name __pycache__`
	@git clean -dXf

env:
	python3 -m venv env
	env/bin/pip3 install --upgrade pip wheel setuptools
	env/bin/pip3 install pylint
	@echo "To activate the virtual environment, execute 'source env/bin/activate'"

.PHONY: clean
