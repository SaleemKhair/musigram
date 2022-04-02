.PHONY: prepare_venv build
APP_NAME=tone-clock-diagram
VENV_NAME ?= .venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip

TOX := $(shell command -v tox 2> /dev/null)

prepare_venv: $(VENV_NAME)/bin/activate 

$(VENV_NAME)/bin/activate: requirements.txt
	[ -d $(VENV_NAME) ] || virtualenv -p python3 $(VENV_NAME)
	${PIP} install -U pip
	${PIP} install -r requirements.txt

run: install
	${PYTHON} src/server/__main__.py

test: requirements.txt
	$(TOX) -e py38

build: prepare_venv
	${PYTHON} setup.py build

install: prepare_venv
	${PYTHON} setup.py install

uninstall: prepare_venv
	${PIP} uninstall ${APP_NAME}

clean:
	rm -rf **/__pycache__ build dist *.egg-info **/*.pyc .tox

