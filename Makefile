VIRTUALENV=env
PYTHON_BIN=$(VIRTUALENV)/bin/python
PIP_BIN=$(VIRTUALENV)/bin/pip
MANAGE_BIN=$(PYTHON_BIN) manage.py


virtualenv:
	test -d "$(VIRTUALENV)" || virtualenv --distribute $(VIRTUALENV)

requirements: virtualenv
	$(PIP_BIN) install -r requirements.txt

privateserver: requirements
	$(MANAGE_BIN) runserver --settings=devisio.settings.development

server: requirements
	$(MANAGE_BIN) runserver 0.0.0.0:8000 --settings=devisio.settings.development

staticfiles: requirements
	$(MANAGE_BIN) collectstatic --noinput

mediafolders:
	mkdir -p deploy/media
	mkdir -p deploy/media/uploads

database: requirements
	$(MANAGE_BIN) syncdb --noinput --settings=devisio.settings.development
	$(MANAGE_BIN) migrate --all --settings=devisio.settings.development

shell: requirements
	$(MANAGE_BIN) shell --settings=devisio.settings.development
