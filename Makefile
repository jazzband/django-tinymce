VIRTUALENV = virtualenv
VENV := $(shell echo $${VIRTUAL_ENV-.venv})
PYTHON = $(VENV)/bin/python
DEV_STAMP = $(VENV)/.dev_env_installed.stamp
INSTALL_STAMP = $(VENV)/.install.stamp

.IGNORE: clean distclean maintainer-clean
.PHONY: all install virtualenv tests

OBJECTS = .venv .coverage

all: install
install: $(INSTALL_STAMP)
$(INSTALL_STAMP): $(PYTHON) setup.py
	$(VENV)/bin/pip install -U pip django flake8 pyenchant coverage
	$(VENV)/bin/pip install -Ue .
	touch $(INSTALL_STAMP)

install-dev: $(INSTALL_STAMP) $(DEV_STAMP) setup.py
$(DEV_STAMP): $(PYTHON)
	$(VENV)/bin/pip install django flake8 pyenchant coverage tox
	touch $(DEV_STAMP)

virtualenv: $(PYTHON)
$(PYTHON):
	$(VIRTUALENV) $(VENV)

tests-once: install-dev
	$(VENV)/bin/coverage run --source=tinymce setup.py test
	$(VENV)/bin/coverage report

tests: install-dev tox.ini
	$(VENV)/bin/tox

flake8: install-dev
	$(VENV)/bin/flake8 tinymce --ignore=E501,E402

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr

distclean: clean
	rm -fr *.egg *.egg-info/

maintainer-clean: distclean
	rm -fr .venv/ .tox/ dist/ build/

serve:
	./testtinymce/manage.py migrate
	./testtinymce/manage.py createsuperuser --username admin --email "test@tinymce.com" --no-input 2>/dev/null || exit 0
	./testtinymce/manage.py runserver
