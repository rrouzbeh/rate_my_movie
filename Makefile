PYTHON := python3
PIP := $(PYTHON) -m pip
PYTEST := $(PYTHON) -m pytest

init:
	$(PIP) install -r requirements.txt
install:
	$(PYTHON) setup.py install
clean:
	$(PYTHON) setup.py clean --all
test:
	$(PYTEST) tests
docker:
	docker build -t rate-my-movie .