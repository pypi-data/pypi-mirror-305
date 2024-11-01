# tinyagi/config.py

import json
import os

DEFAULT_CONFIG_FILE = 'config.json'

class ConfigManager:
    def __init__(self, config_file=None):
        self.config_file = config_file or DEFAULT_CONFIG_FILE
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found at {self.config_file}")
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def reload_config(self, config_file=None):
        self.config_file = config_file or self.config_file
        self.config = self.load_config()
        return self.config

    def get_config(self):
        return self.config
