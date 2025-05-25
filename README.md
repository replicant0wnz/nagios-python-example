# nagios-python-example
![](https://github.com/replicant0wnz/nagios-python-example/actions/workflows/release.yml/badge.svg)
[![Releases](https://img.shields.io/github/v/release/replicant0wnz/nagios-python-example)](https://github.com/replicant0wnz/nagios-python-example/releases)
[![Latest commit](https://img.shields.io/github/last-commit/replicant0wnz/nagios-python-example)](https://github.com/replicant0wnz/nagios-python-example/commits/main)
[![LICENSE](https://img.shields.io/github/license/replicant0wnz/nagios-python-example)](https://github.com/replicant0wnz/nagios-python-example/blob/main/LICENSE)
[![main](https://github.com/replicant0wnz/nagios-python-example/actions/workflows/main.yml/badge.svg)](https://github.com/replicant0wnz/nagios-python-example/actions/workflows/main.yml)

Simple Nagios plugin example writtin in Python

## Description

`nagios-python-example` contains a simple Nagios plugin that performs a check
against a list of http(s) servers. Both the `WARN` and `CRITICAL` are configurable.

Each down server will be shown in the Nagios console.

## Requirements

While most modern installations contain these modules the following are required:

- `PyYAML`
- `requests`

## Installation

While you can clone this entire repository the simpliest way to install it is via a
single `wget` command on the Nagios server:

```bash
sudo wget \
https://raw.githubusercontent.com/replicant0wnz/nagios-python-example/refs/heads/main/src/http_cluster/http_cluster.py \
-O /usr/local/nagios/libexec/check_http_cluster
```

## Configuration example

```yaml
someitem:
  key1: value
  key2: value
  key3:
    - list1
    - list2
    - list3
```

## Usage

```bash
ls -l 
do some stuff
```
