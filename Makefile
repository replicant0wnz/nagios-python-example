SHELL := /bin/bash

# Global stuff
DOCKER=docker
SOURCE_PATH := $(shell pwd)
WORKING_PATH=/opt
CONFIG="makefile.json"
UID := $(shell id -u)

# Docker config
DOCKER_RUN=$(DOCKER) run -u $(UID) -v $(SOURCE_PATH):$(WORKING_PATH) -w $(WORKING_PATH)

# Python config
PYTHON_CONTAINER=public.ecr.aws/replicant0wnz/build-python:latest
PYPI_USERNAME=__token__
PYPI_PASSWORD=$(token)

# Executable


.PHONY: list
list:
	# List options of nothing specified
	grep '^[^#[:space:]].*:' Makefile

.PHONY: black
black:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) black src/http_cluster/http_cluster.py

.PHONY: test
test:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) python -m pytest tests

.PHONY: list
install:
	cp

all: black test install
