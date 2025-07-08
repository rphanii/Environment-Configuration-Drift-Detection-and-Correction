import json

def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)

def detect_drift(dev_config, prod_config):
    drift = {}
    for key in dev_config:
        if key in prod_config and dev_config[key] != prod_config[key]:
            drift[key] = {
                "dev": dev_config[key],
                "prod": prod_config[key]
            }
    return drift
