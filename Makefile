TARGET?=development
PYTHON?=python
VIRTUALENV_BIN?=virtualenv
VIRTUALENV_DIR=env
MANAGE_PY=$(VIRTUALENV_DIR)/bin/python manage.py
PIP_BIN=$(VIRTUALENV_DIR)/bin/pip
SETTINGS_PARAM=devisio.settings.$(TARGET)


all: server

environment:
	test -d "$(VIRTUALENV_DIR)" || $(VIRTUALENV_BIN) --distribute --no-site-packages --python $(PYTHON) $(VIRTUALENV_DIR)

requirements: environment
	$(PIP_BIN) install -r requirements/base.txt
	$(PIP_BIN) install -r requirements/$(TARGET).txt

database: requirements
	$(MANAGE_PY) syncdb --noinput --settings=$(SETTINGS_PARAM)
	$(MANAGE_PY) migrate --all --settings=$(SETTINGS_PARAM)

privateserver: database
	$(MANAGE_PY) runserver --settings=$(SETTINGS_PARAM)

server: database
	$(MANAGE_PY) runserver 0.0.0.0:8000 --settings=$(SETTINGS_PARAM)

collectstatic: requirements deployfolders
	$(MANAGE_PY) collectstatic --noinput

deployfolders:
	mkdir -p deploy/media/uploads

shell: requirements
	$(MANAGE_PY) shell --settings=$(SETTINGS_PARAM)

.PHONY: privateserver server
