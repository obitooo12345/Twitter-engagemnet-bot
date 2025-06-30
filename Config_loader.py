import yaml
import os

def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def validate_config(config):
    required = ['accounts', 'settings']
    return all(key in config for key in required)
