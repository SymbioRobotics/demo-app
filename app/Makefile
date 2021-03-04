###############################################################################
# Compose shared targets from symbio-build-tools and application-specific
# commands to control the build.
###############################################################################

all: setup.py
	$(PYTHON) setup.py develop --user

# Set the directories/packages inspected by flake8 and mypy. Use this in conjunction
# with their configuration files to apply the desired level of strictness.

lint_python: export SBT_FLAKE8_ARGS=symbio_reference tests setup.py
lint_python: export SBT_MYPY_ARGS=-p $(firstword $(SBT_FLAKE8_ARGS))
lint: lint_python

# Configure the supported automated test flavors by adding/removing these targets.
# Preserve the structure of the "tests" subdirectory such that restoring simply
# requires a one-liner here and similarly trivial change to the Jenkinsfile.

unit: test_python
integration functional:
	$(MAKEFILE_DIRECTORY)/$@.sh
test: lint unit integration functional

# Clean artifacts produced by make and automation scripts.

clean: clean_python
distclean: clean distclean_python

# Construct a Docker image runnable by automation scripts and host tools.

bootstrap: bootstrap_docker

# Load common variables and targets.

include ../infrastructure/common.mk
