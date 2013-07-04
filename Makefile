TARGET?=development
VIRTUALENV=env
PYTHON_BIN=$(VIRTUALENV)/bin/python
PIP_BIN=$(VIRTUALENV)/bin/pip
MANAGE_BIN=$(PYTHON_BIN) manage.py
SETTINGS_PARAM=devisio.settings.$(TARGET)


all: server

virtualenv:
	test -d "$(VIRTUALENV)" || virtualenv --distribute $(VIRTUALENV)

requirements: virtualenv
	$(PIP_BIN) install -r requirements/base.txt
	$(PIP_BIN) install -r requirements/$(TARGET).txt

privateserver: requirements
	$(MANAGE_BIN) runserver --settings=$(SETTINGS_PARAM)

server: requirements
	$(MANAGE_BIN) runserver 0.0.0.0:8000 --settings=$(SETTINGS_PARAM)

staticfiles: requirements
	$(MANAGE_BIN) collectstatic --noinput

mediafolders:
	mkdir -p deploy/media
	mkdir -p deploy/media/uploads

database: requirements
	$(MANAGE_BIN) syncdb --noinput --settings=$(SETTINGS_PARAM)
	$(MANAGE_BIN) migrate --all --settings=$(SETTINGS_PARAM)

shell: requirements
	$(MANAGE_BIN) shell --settings=$(SETTINGS_PARAM)
