# Variable
VENV_NAME = venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
COVERAGE = $(VENV_NAME)/bin/coverage

.PHONY: setup install run test clean help

# Default target
all: clean setup install test

# Create virtual environment and install dependencies
setup:
	@echo "Setting up the virtual environment and installing dependencies."
	rm -rf $(VENV_NAME)
	python3 -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt

# Install dependencies
install: $(VENV_NAME)
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

# Run the application
run: install
	@echo "Running the application..."
	PYTHONPATH=$(PWD) $(PYTHON) app/main.py

# Run tests
test: install
	@echo "Running tests..."
	$(PYTHON) -m unittest discover -s tests

# Run tests with coverage
coverage: install
	@echo "Running tests with coverage..."
	coverage run -m unittest discover -s tests
	coverage report

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .coverage

# Build Docker image
docker:
	@echo "Building Docker image..."
	docker build -t subscription-api .

# Display help information
help:
	@echo "Usage: make [TARGET]"
	@echo ""
	@echo "Targets:"
	@echo "  setup           - Create virtual environment and install dependencies"
	@echo "  install         - Install dependencies"
	@echo "  run             - Run the application"
	@echo "  test            - Run tests"
	@echo "  coverage        - Run tests with coverage report"
	@echo "  coverage-html   - Run tests with coverage and generate HTML report"
	@echo "  clean           - Clean up"
	@echo "  docker          - Build Docker image"
	@echo "  help            - Show this help message"
