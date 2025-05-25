SHELL := /bin/bash

# Global stuff
DOCKER=docker
SOURCE_PATH := $(shell pwd)
WORKING_PATH=/opt
UID := $(shell id -u)

# Docker config
DOCKER_RUN=$(DOCKER) run -u $(UID) -v $(SOURCE_PATH):$(WORKING_PATH) -w $(WORKING_PATH)

# Python config
PYTHON_CONTAINER=public.ecr.aws/replicant0wnz/build-python:latest

HTTP_CLUSTER=src/http_cluster/http_cluster.py

.PHONY: list
list:
	# List options of nothing specified
	grep '^[^#[:space:]].*:' Makefile

.PHONY: black
black:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) black $(HTTP_CLUSTER)

.PHONY: test
test:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) python -m pytest tests
