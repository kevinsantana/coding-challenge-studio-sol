SHELL=/bin/bash
BASE_DIR:=.
PROJECT_BASE_DIR:=$(BASE_DIR)/valid_password/
PROJECT_NAME:=valid-password

BASE_DOCKER_FILE:=$(BASE_DIR)/Dockerfile

help:
	@echo 'Usage:'
	@echo '  make clean                  Remove python compiled files                                           '
	@echo '  make lint                   Run pylama linter                                                      '
	@echo '  make black           		 Install black and run                                                  '
	@echo '  make run-local           	 Run user-api application local                                         '
	@echo '  make docker-build           Build docker images with docker-compose                                '
	@echo '  make docker-start           Run appplication with docker images                                    '
	@echo '  make run                    Build and run application                                              '
	@echo ''

clean:
	@find . -iname *.pyc -delete;
	@find . -iname *.pyo -delete;
	@find . -iname __pycache__ -delete;
	@rm -fr build dist .venv-dist;
	@rm -fr .cache .pytest_cache;
	@rm -fr .tox .eggs;
	@find . -iname .coverage -delete;
	@find . -iname *.egg-info -exec rm -fr {} +
	@rm -fr htmlcov coverage.xml;

lint:
	pip install -U pylama;
	cd $(PROJECT_BASE_DIR); pylama -o pylama.ini;

black:
	pip install -U black;
	for d in $(PROJECT_BASE_DIR)*/ ; do cd $$d; python -m  black .; cd ..; done;

test: clean
	pytest -v

run-local:
	cd valid_password && gunicorn --workers=1 --worker-class=uvicorn.workers.UvicornWorker --timeout=174000 --reload --bind=0.0.0.0:8000 'app:start_application()'

docker-build:
	if [ -f $(BASE_DOCKER_FILE) ]; then docker build -t valid_password:1.0.0 .; fi

docker-start:
	if [ -f $(BASE_DOCKER_FILE) ]; then docker container run -p 7000:7000 --name valid-password --rm valid_password:1.0.0; fi

run:
	make docker-build;
	make docker-start;