\# Environment Configuration Drift Detection and Correction



A modular system to detect, assess, and correct configuration drift across development (`dev`), staging (`staging`), and production (`prod`) environments — ensuring consistency, stability, and compliance in CI/CD pipelines.



---



\## Problem Statement



Configuration drift occurs when configuration settings in different environments (dev, staging, prod) become inconsistent over time. This can lead to bugs, security vulnerabilities, or unexpected behavior in production.



This project detects such drifts, assesses their impact, and suggests automated corrections using AI/ML-inspired logic and rule-based pattern analysis.



---



\## Features



\- Drift Detection: Identifies mismatches between environment configurations.

\- Pattern Analysis: Simulates AI-based environment behavior pattern learning.

\- Impact Assessment: Classifies drifts into HIGH, MEDIUM, or LOW impact.

\- Correction Suggestions: Recommends exact changes to fix discrepancies.

\- Flask Web App: User-friendly interface to run the full drift pipeline visually.

\- Modular Architecture: Code split into detector, analyzer, corrector, and utils.



---



\## Skills Demonstrated



| Skill                 | Description |

|----------------------|-------------|

| AI/ML Concepts        | Simulated pattern recognition to detect environment anomalies. |

| Critical Thinking     | Prioritizing configuration changes based on impact. |

| Problem Solving       | Handling drift in diverse environments with rollback logic. |

| Software Design       | Modular, readable, scalable Python application. |

| Flask Web Development | Lightweight web UI to trigger and visualize drift analysis. |

-----------------------------------------------------------------------------------------



\### Prerequisites



\- Python 3.8+

\- pip



\### Install dependencies



```bash

pip install flask





