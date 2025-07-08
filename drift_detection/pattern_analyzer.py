import json

def extract_features(config):
    """Convert config dict to flat feature vector for pattern analysis."""
    return config   

def analyze_patterns(dev_config, staging_config, prod_config):
    """Simulate ML-driven pattern analysis to detect anomalies."""
    patterns = {
        "debug": {"dev": True, "staging": False, "prod": False},
        "logging_level": {"dev": "DEBUG", "staging": "INFO", "prod": "ERROR"},
        "database": {"dev": "localhost", "staging": "staging.db.server", "prod": "prod.db.server"}
    }

    anomalies = []
    all_configs = {"dev": dev_config, "staging": staging_config, "prod": prod_config}

    for key in patterns:
        for env in all_configs:
            expected = patterns[key].get(env)
            actual = all_configs[env].get(key)
            if expected != actual:
                anomalies.append((env, key, actual, expected))

    return anomalies
