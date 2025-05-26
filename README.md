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

## Configuration

Configuration is managed through a single yaml file, one which is contained in the repository Here
is a breakdown of the keys:

```yaml
http_servers:
  config:
    warn_threshold: 1 # How many servers down before issuing a WARN
    critical_threadhold: 2 # How many servers down before issuing a CRITICAL
    protcol: "http" # http or https
    timeout: 5 # timeout in seconds
  servers: # List of servers to monitor
    - "web1"
    - "web2"
```

### Example Nagios impimentation 

Add the following to the `commands.cfg`:

```
define command {
    command_name    check_http_cluster
    command_line    $USER1$/check_http_cluster -c $ARG1$
}
```

Create a "dummy" host in `templates.cfg` if we don't want to associate with an existing server:

```
define host {
    name                            no-host
    use                             generic-host
    max_check_attempts              1
    address                         127.0.0.1 
    check_command                   check-host-alive
    register                        0
}
```

Finally setup the service itself in whatever config you'd like:

```
define host {
    use       no-host
    host_name http-cluster
}

define service {
    use                   generic-service
    host_name             http-cluster 
    service_description   CLUSTER 
    check_command         check_http_cluster! path/to/config.yaml
}
```
