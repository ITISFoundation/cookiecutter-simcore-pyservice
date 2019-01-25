.PHONY: all check clean

objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

# target: all – pip-compiles all requirements/*.in -> requirements/*.txt
all: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

test.txt: base.txt

# target: check – Checks whether pip-compile is installed
check:
	@which pip-compile > /dev/null

# target: clean – Cleans all requirements/*.txt
clean: check
	- rm *.txt
