from flask import Flask, render_template, request
from drift_detection.detector import load_config, detect_drift
from drift_detection.impact_analyzer import assess_impact
from drift_detection.corrector import suggest_corrections
from drift_detection.pattern_analyzer import analyze_patterns

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_analysis():
    dev = load_config("config/dev_config.json")
    staging = load_config("config/staging_config.json")
    prod = load_config("config/prod_config.json")

    result = "Running Configuration Drift Detection...\n\n"

    
    result += "Analyzing configuration patterns across environments...\n\n"
    anomalies = analyze_patterns(dev, staging, prod)
    if anomalies:
        result += "Anomalies detected based on learned patterns:\n"
        for env, key, actual, expected in anomalies:
            result += f"- {env.upper()} → {key}: actual = {actual} | expected = {expected}\n"
    else:
        result += "No anomalies in pattern analysis.\n"

    result += "\nDetecting drift between dev and prod...\n\n"

    # Drift Detection
    drift = detect_drift(dev, prod)
    if not drift:
        result += "No configuration drift detected.\n"
    else:
        result += "Drift detected with impact levels:\n"
        for key, values in drift.items():
            impact = assess_impact(key)
            result += f"- {key}: dev = {values['dev']} | prod = {values['prod']} | Impact = {impact}\n"

        # Corrections
        corrections = suggest_corrections(drift)
        if corrections:
            result += "\nSuggested corrections:\n"
            for key, suggestion in corrections.items():
                result += f"- {key}: change prod from '{suggestion['from']}' to '{suggestion['to']}'\n"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
