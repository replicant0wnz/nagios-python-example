#!/usr/bin/env python3

import requests
import yaml

class HTTPCluster:
    """
    Simple class to test a cluster of http servers.
    """

    def __init__(self, config_file="config.yaml"):
        """
        Keywords:
            config_file (str): Full path to config
        """

        self.config_file = config_file

    def _read_config(self):
        """
        Reads the yaml config

        Returns:
            config (dict)
        """

        f = open(self.config_file)

        try:
            config_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            raise e

        return config_yaml["http_servers"]

    def check_server(self, server=None, protocol=None, timeout=None):
        """
        Performs http check

        Return:
            True: Successful 200 connection
            False: Anything else
        """

        try:
            return_code = requests.get(
                f"{protocol}://{server}", timeout=timeout
            ).status_code
        except:
            return_code = 0

        if return_code == 200:
            return True
        else:
            return False

    def execute_checks(self):
        """
        Perform the http checks
        """

        cluster_config = self._read_config()
        config = cluster_config["config"]
        servers = cluster_config["servers"]

        threshold = 0
        down_servers = []

        for server in servers:
            x = self.check_server(
                server=server, protocol=config["protcol"], timeout=config["timeout"]
            )
            if x is False:
                threshold += 1
                down_servers.append(server)

        if threshold == config["warn_threshold"]:
            nagios_message = "WARN"
        elif threshold == config["critical_threadhold"]:
            nagios_message = "CRITICAL"
        else:
            nagios_message = "OK"

        return nagios_message, down_servers


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Path to config", required=True)
    args = parser.parse_args()

    exit_code = {"OK": 0, "WARN": 1, "CRITICAL": 2}

    x = HTTPCluster(config_file=args.config)
    status, down_servers = x.execute_checks()
    if not down_servers:
        print(f"CLUSTER {status}: All servers reporting")
    else:
        down_string = " ".join(down_servers)
        print(f"CLUSTER {status}: {down_string} ")

    sys.exit(exit_code[status])
