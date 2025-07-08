def assess_impact(key):
    high_impact_keys = ["database", "logging_level"]
    low_impact_keys = ["debug"]

    if key in high_impact_keys:
        return "HIGH"
    elif key in low_impact_keys:
        return "LOW"
    else:
        return "MEDIUM"
