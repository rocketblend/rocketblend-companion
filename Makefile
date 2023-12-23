# Name of the virtual environment
VENV := venv

# Default target executed
all: help

## help: Show this help.
.PHONY: help
help: Makefile
	@sed -n 's/^##//p' $<

## activate: Activate the virtual environment.
.PHONY: activate
activate:
	@echo "Activating virtual environment..."
	@. $(VENV)/bin/activate

## deactivate: Deactivate the virtual environment.
.PHONY: deactivate
deactivate:
	@echo "Deactivating virtual environment..."
	@deactivate

## install: Install requirements.
.PHONY: install
install: $(VENV)/bin/activate
	$(VENV)/bin/pip install -r requirements.txt

$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(VENV)/bin/pip install -U pip