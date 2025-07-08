from drift_detection.detector import load_config, detect_drift
from drift_detection.impact_analyzer import assess_impact
from drift_detection.corrector import suggest_corrections
from drift_detection.pattern_analyzer import analyze_patterns  # ✅ NEW

def main():
    print("Running Configuration Drift Detection...\n")

    dev_config = load_config("config/dev_config.json")
    prod_config = load_config("config/prod_config.json")
    
    # Step 1: Pattern Analysis
    print("Analyzing configuration patterns across environments...\n")
    anomalies = analyze_patterns(dev_config, dev_config, prod_config)  # Replace 2nd dev_config with staging_config later if needed
    if anomalies:
        print("Anomalies detected based on learned patterns:")
        for env, key, actual, expected in anomalies:
            print(f"- {env.upper()} → {key}: actual = {actual} | expected = {expected}")
    else:
        print("No anomalies found in environment configurations.")

    # Step 2: Drift Detection
    print("\n📡 Detecting drift between dev and prod...\n")
    drift = detect_drift(dev_config, prod_config)

    if not drift:
        print("No configuration drift detected. All environments are consistent.")
    else:
        print("Drift detected with impact levels:")
        for key, values in drift.items():
            impact = assess_impact(key)
            print(f"- {key}: dev = {values['dev']} | prod = {values['prod']} | Impact = {impact}")

        # ✅ Step 3: Suggest Corrections
        corrections = suggest_corrections(drift)
        if corrections:
            print("\nSuggested corrections:")
            for key, suggestion in corrections.items():
                print(f"- {key}: change prod from '{suggestion['from']}' to '{suggestion['to']}'")

if __name__ == "__main__":
    main()
