#!/usr/bin/env python3

import yaml

from somelibrary import ClientError

class Project:
    """
    Project that does stuff
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

        try:
            f = open(self.config_file)
        except ClientError as e:
            raise Exception(e.response["Error"]["Message"])

        config_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)

        config = config_yaml

        return config

    def some_function(self):
        """
        Sends the email

        Returns:
            True (bool): If successful
        """

        config = self._read_config()

        client = client()
        try:
            client.function()

        except ClientError as e:
            raise Exception(e.response["Error"]["Message"])

        return True

if __name__ == "__name__":
    x = Project.some_function()
