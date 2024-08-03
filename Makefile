# Makefile for plant_seedlings project

# Variables
PROJECT_NAME = Plant_Seedlings
PYTHON = python3
PIP = pip
POETRY = poetry

# Targets
.PHONY: all setup install run clean test

all: setup install

setup:
	@echo "Setting up virtual environment..."
	$(POETRY) env use $(PYTHON)

install:
	@echo "Installing dependencies..."
	$(POETRY) install

test:
	@echo "Running tests..."
	$(POETRY) run pytest -v tests/test.py

run:
	@echo "Running the application..."
	$(POETRY) run streamlit run app/app.py

# poetry cache clear --all .
clean:
	@echo "Cleaning up..."
	$(POETRY) env remove $(PYTHON) 

# Additional target for development purposes
dev-install:
	@echo "Installing development dependencies..."
	$(POETRY) install --with dev
