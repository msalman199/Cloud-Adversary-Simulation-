# 🚀 Build Passive Asset Map Using GitHub & Censys

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- Perform passive reconnaissance using GitHub search techniques
- Utilize Censys API to discover public cloud infrastructure
- Automate asset discovery using Python scripts
- Aggregate and analyze reconnaissance data from multiple sources
- Generate comprehensive security assessment reports

---

# 📌 Prerequisites

Before starting this lab, students should have:

- Basic understanding of cloud computing (AWS, Azure, GCP)
- Familiarity with Linux command line
- Basic Python programming knowledge
- Understanding of network protocols and cybersecurity principles
- GitHub account (free tier)
- Censys account with API credentials

---

# 🖥️ Lab Environment

Al Nafi provides pre-configured Linux cloud machines.

You will have:

- Python 3.x with pip
- Git client
- Text editors (nano, vim)
- Network utilities
- Web browser

---

# 🧠 Task 1 — GitHub Reconnaissance for Exposed Assets

---

# 🔹 Step 1 — Setup Working Environment

```bash
mkdir -p ~/passive-recon-lab/{github-recon,censys-recon,reports}
cd ~/passive-recon-lab/github-recon

pip3 install requests
🔹 Step 2 — Manual GitHub Search (OSINT)

Search on GitHub:

🔑 AWS Credentials Exposure
"aws_access_key_id" OR "aws_secret_access_key"
🗄️ Database Strings
"mongodb://" OR "mysql://" password
🔐 API Keys
"api_key" OR "apikey" filename:config
☁️ Cloud Config Files
filename:.env OR filename:terraform.tfvars
📊 Document Findings

Record:

Repository name
File path
Exposure type
Risk level
🔹 Step 3 — GitHub Scanner Script

Create file:

github_scanner.py
🐍 Python Script (Template)
#!/usr/bin/env python3

import requests
import json
import time
from datetime import datetime


class GitHubScanner:
    def __init__(self):
        self.base_url = "https://api.github.com/search/code"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "PassiveRecon-Lab"
        }
        self.results = []

    def search_github(self, query, max_results=10):
        """
        Search GitHub Code API
        """
        # TODO: Implement API request
        # TODO: Handle rate limiting (403)
        # TODO: Parse JSON response
        # TODO: Return results
        pass

    def analyze_results(self, items, search_type):
        """
        Analyze exposure results
        """
        # TODO: Extract repo, file path, URL
        # TODO: Add timestamp
        # TODO: Assign risk score
        pass

    def run_comprehensive_scan(self):
        """
        Multi-query scanning
        """
        queries = {
            "aws": "aws_access_key_id OR aws_secret_access_key",
            "db": "mongodb:// OR mysql://",
            "api": "api_key OR apikey filename:config",
            "cloud": "filename:.env OR filename:terraform.tfvars"
        }

        # TODO: Loop through queries
        # TODO: Apply delay between requests
        # TODO: Aggregate results
        pass

    def save_results(self, findings, filename="github_scan_results.json"):
        """
        Save JSON output
        """
        pass


def main():
    # TODO: Run scanner
    pass


if __name__ == "__main__":
    main()
▶️ Run Script
chmod +x github_scanner.py
python3 github_scanner.py
☁️ Task 2 — Censys Cloud Asset Discovery
🔹 Step 1 — Configure Censys API
cd ~/passive-recon-lab/censys-recon
pip3 install censys
🔐 Credentials Setup
mkdir -p ~/.censys
nano ~/.censys/credentials
📄 Add Credentials
[DEFAULT]
api_id = your-api-id
api_secret = your-api-secret
🔹 Step 2 — Censys Scanner

Create:

censys_scanner.py
🐍 Python Template
from censys.search import CensysHosts


class CensysScanner:
    def __init__(self):
        # TODO: Initialize API client
        pass

    def search_cloud_assets(self, query, max_results=50):
        # TODO: Execute query
        # TODO: Extract IP, ASN, services
        pass

    def search_aws_assets(self):
        queries = [
            'services.service_name: HTTP AND autonomous_system.name: AMAZON',
            'services.port: 443 AND autonomous_system.name: AMAZON-02'
        ]
        # TODO: Execute AWS queries
        pass

    def search_azure_assets(self):
        # TODO: Azure queries
        pass

    def search_gcp_assets(self):
        # TODO: GCP queries
        pass

    def search_exposed_services(self):
        # TODO: Databases, SSH, RDP, HTTP
        pass


def main():
    # TODO: Run scans
    pass
▶️ Run Scanner
python3 censys_scanner.py
📊 Task 3 — Data Aggregation & Reporting
🔹 Step 1 — Asset Aggregator

Create:

asset_aggregator.py
🐍 Python Template
import json
import os
from collections import Counter
from datetime import datetime


class AssetAggregator:
    def __init__(self):
        self.github_data = []
        self.censys_data = {}

    def load_github_data(self):
        # TODO: Load JSON
        pass

    def load_censys_data(self):
        # TODO: Load Censys results
        pass

    def analyze_exposures(self):
        # TODO: Risk scoring
        pass

    def analyze_cloud_distribution(self):
        # TODO: AWS / Azure / GCP breakdown
        pass

    def perform_risk_assessment(self):
        # TODO: HIGH / MEDIUM / LOW risks
        pass

    def generate_csv_reports(self):
        # TODO: Export CSV files
        pass

    def generate_summary_report(self):
        # TODO: Final report output
        pass


def main():
    # TODO: Run full aggregation
    pass
🔹 Step 2 — Automation Script

Create:

run_complete_scan.sh
🧾 Script
#!/bin/bash

echo "🚀 Starting Passive Recon Scan"

cd ~/passive-recon-lab

echo "[1] GitHub Recon"
cd github-recon
python3 github_scanner.py
cd ..

echo "[2] Censys Recon"
cd censys-recon
python3 censys_scanner.py
cd ..

echo "[3] Aggregation"
python3 asset_aggregator.py

echo "✅ Scan Complete"
▶️ Run
chmod +x run_complete_scan.sh
./run_complete_scan.sh
📁 Expected Outputs

You will generate:

github_scan_results.json
censys_results.json
github_findings.csv
censys_assets.csv
risk_assessment.csv
summary_report.txt
⚠️ Troubleshooting
GitHub Rate Limit
curl https://api.github.com/rate_limit

Fix:

Add delay (2–3 sec)
Use token
Censys API Error
Check credentials
Verify API quota
Empty Results
Adjust queries
Test manually on GitHub/Censys UI
Permission Issues
chmod +x *.py *.sh
📊 Key Outcomes

You achieved:

🔎 GitHub exposed credential discovery
☁️ Cloud infrastructure mapping via Censys
🤖 Automated OSINT pipeline
📊 Multi-source asset correlation
📄 Security reporting system
🚀 Final Conclusion

This lab demonstrated:

Passive reconnaissance without detection
Multi-source intelligence aggregation
Real-world OSINT automation workflows
Cloud attack surface discovery techniques
🧠 Key Takeaways

✔ GitHub leaks are real attack vectors
✔ Censys exposes cloud infrastructure publicly
✔ Automation increases OSINT efficiency
✔ Correlation = stronger security insights

⚠️ Security Reminder

Only use these techniques on:

✔ Authorized systems
✔ Your own infrastructure
✔ Approved penetration testing scope
