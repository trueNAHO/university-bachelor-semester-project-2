MAIN_FILE := main.py
PIP_DEPENDENCIES := pygame

.PHONY: all install run clean

# Default target that triggers other targets: `install` and `run`.
all: install run

# Install the dependencies.
install:
	pip install $(PIP_DEPENDENCIES)

# Run the application.
run:
	python $(MAIN_FILE)
