#!/usr/bin/env python3

import requests
import yaml



class HTTPCluster:
    """
    Simple class for Nagios to test a cluster of http servers.
    """

    def __init__(self, config_file="config.yaml"):
        """
        Keywords:
            config_file (str): Full path to config
        """

        self.config_file = config_file

    def _read_config(self):
        """
        Reads the yaml config file

        Returns:
            config (dict)
        """

        config = {}

        f = open(self.config_file)

        try:
            config_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            raise e

        config = config_yaml

        return config

    def check_server(self, server=None, protocol="http", timeout=5, min_return_code=200, max_return_code=203):
        """
        Performs http check 

        Return:
            True: Recieve 2xx or 3xx code
            False: Anything else
        """

        try:
            return_code = requests.get(f"{protocol}://{server}", timeout=timeout).status_code
            print(return_code)
        except:
            return_code = 0

        if return_code < max_return_code and return_code >= min_return_code:
            return True
        else:
            return False

