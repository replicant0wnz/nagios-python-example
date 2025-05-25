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
        Reads the yaml config file and returns a list of servers

        Returns:
            config (dict)
        """

        config = {}

        f = open(self.config_file)

        try:
            config_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            raise e

        config = config_yaml['http_servers']

        self.protcol = config['config']['protcol']
        self.timeout = config['config']['timeout']
        self.warn_threshold = config['config']['warn_threshold']
        self.critical_threadhold = config['config']['critical_threadhold']
        

    def _check_server(self, server=None, protocol=None, timeout=None):
        """
        Performs http check 

        Return:
            True: Successful 200 connection
            False: Anything else
        """

        try:
            return_code = requests.get(f"{protocol}://{server}", timeout=timeout).status_code
        except:
            return_code = 0

        if return_code == 200:
            return True
        else:
            return False


    def execute(self):
        """
        Iterate through the config and perform the http checks
        """
       
        config = self._read_config()


