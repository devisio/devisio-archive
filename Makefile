VIRTUALENV=env
PYTHON_BIN=$(VIRTUALENV)/bin/python
MANAGE_BIN=$(PYTHON_BIN) manage.py


privateserver:
	$(MANAGE_BIN) runserver

publicserver:
	$(MANAGE_BIN) runserver 0.0.0.0:8000

staticfiles:
	$(MANAGE_BIN) collectstatic --noinput
