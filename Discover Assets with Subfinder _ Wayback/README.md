
# 🔎 Discover Assets with Subfinder + Wayback

<div align="center">

![Banner](https://img.shields.io/badge/Lab-Asset_Discovery-blue?style=for-the-badge)

# 🌐 Passive Reconnaissance & Historical Asset Discovery

### Learn how to discover subdomains, collect historical URLs, automate reconnaissance, and generate professional reports.

---

## 🛡️ Technology Stack

<p align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Go](https://img.shields.io/badge/Go-Programming-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Subfinder](https://img.shields.io/badge/Subfinder-Recon-blue?style=for-the-badge)
![ProjectDiscovery](https://img.shields.io/badge/ProjectDiscovery-Tools-orange?style=for-the-badge)
![HTTPX](https://img.shields.io/badge/HTTPX-Probing-green?style=for-the-badge)
![Wayback Machine](https://img.shields.io/badge/Wayback-Historical_Data-black?style=for-the-badge)
![WaybackURLs](https://img.shields.io/badge/WaybackURLs-TomNomNom-blueviolet?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-Recon-success?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-Web-orange?style=for-the-badge)
![Recon](https://img.shields.io/badge/Passive-Recon-red?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Reports-lightgrey?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-Reporting-E34F26?style=for-the-badge&logo=html5&logoColor=white)

</p>

---

# 📖 Table of Contents

- Objectives
- Prerequisites
- Lab Environment
- Task 1 — Install & Configure Subfinder
- Task 2 — Discover Historical Assets using Wayback Machine
- Task 3 — Python Automation *(Part 2)*
- Expected Outcomes *(Part 3)*
- Troubleshooting *(Part 3)*
- Conclusion *(Part 3)*

---

# 🎯 Objectives

By completing this lab, you will learn how to:

- ✅ Install and configure **Subfinder**
- ✅ Discover subdomains using passive reconnaissance
- ✅ Validate live hosts with **HTTPX**
- ✅ Retrieve historical URLs from the Wayback Machine
- ✅ Analyze historical assets
- ✅ Automate reconnaissance using Python
- ✅ Generate JSON and HTML reports
- ✅ Build reusable asset monitoring workflows

---

# 📚 Prerequisites

Before beginning this lab, you should have:

- Basic Linux command-line knowledge
- Understanding of DNS and subdomains
- Python programming fundamentals
- Familiarity with HTTP and web technologies

---

# 🖥️ Lab Environment

This lab uses an **Al Nafi** pre-configured Linux cloud machine.

All activities are performed on a single Linux host.

---

# 🚩 Task 1 — Install & Configure Subfinder

---

# 🔹 Step 1.1 — Update the System

```bash
sudo apt update && sudo apt upgrade -y
```

---

# 🔹 Step 1.2 — Install Go

```bash
sudo apt install golang-go -y
```

Verify installation.

```bash
go version
```

Expected output

```text
go version go1.xx linux/amd64
```

---

# 🔹 Step 1.3 — Install Subfinder

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

---

# 🔹 Step 1.4 — Configure PATH

```bash
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc
source ~/.bashrc
```

Verify installation.

```bash
subfinder -version
```

---

# 🔹 Step 1.5 — Configure Provider API Keys

Create configuration directory.

```bash
mkdir -p ~/.config/subfinder
```

Create provider configuration file.

```bash
cat > ~/.config/subfinder/provider-config.yaml << 'EOF'
# Add your API keys here (optional but recommended)

virustotal: []

shodan: []

github: []

censys: []

EOF
```

Protect the configuration file.

```bash
chmod 600 ~/.config/subfinder/provider-config.yaml
```

---

# 🔹 Step 1.6 — Create a Working Directory

```bash
mkdir ~/asset_discovery_lab

cd ~/asset_discovery_lab
```

---

# 🔹 Step 1.7 — Perform Passive Subdomain Enumeration

```bash
subfinder -d example.com -o subdomains.txt
```

Display discovered subdomains.

```bash
cat subdomains.txt
```

Count results.

```bash
echo "Total subdomains: $(wc -l < subdomains.txt)"
```

Example

```text
api.example.com

mail.example.com

dev.example.com

blog.example.com
```

---

# 🔹 Step 1.8 — Install HTTPX

HTTPX validates whether discovered hosts are alive.

```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

---

# 🔹 Step 1.9 — Probe Active Hosts

```bash
httpx \
-l subdomains.txt \
-o active_hosts.txt \
-status-code \
-title
```

Display results.

```bash
cat active_hosts.txt
```

Count active hosts.

```bash
echo "Active hosts: $(wc -l < active_hosts.txt)"
```

Example

```text
https://api.example.com [200] API Gateway

https://mail.example.com [302] Outlook

https://blog.example.com [200] Blog
```

---

# ✅ Task 1 Summary

You successfully:

- Installed Go
- Installed Subfinder
- Configured provider APIs
- Performed passive subdomain enumeration
- Installed HTTPX
- Verified live assets

---

# 🌍 Task 2 — Retrieve Historical Assets Using Wayback Machine

---

# 🔹 Step 2.1 — Install Required Packages

```bash
sudo apt install python3-pip -y
```

Install Python libraries.

```bash
pip3 install requests waybackpy
```

---

# 🔹 Step 2.2 — Install WaybackURLs

```bash
go install github.com/tomnomnom/waybackurls@latest
```

Verify installation.

```bash
waybackurls --help
```

---

# 🔹 Step 2.3 — Create Historical Data Directory

```bash
mkdir historical_data
```

---

# 🔹 Step 2.4 — Collect Historical URLs

Retrieve archived URLs.

```bash
waybackurls example.com > historical_data/wayback_urls.txt
```

Remove duplicate entries.

```bash
sort -u historical_data/wayback_urls.txt \
> historical_data/unique_urls.txt
```

Count collected URLs.

```bash
echo "Historical URLs found: $(wc -l < historical_data/unique_urls.txt)"
```

Example

```text
Historical URLs found: 1254
```

---

# 🔹 Step 2.5 — Extract Interesting Files

Search for potentially sensitive files.

```bash
grep -E '\.(js|json|xml|config|env|bak)$' \
historical_data/unique_urls.txt \
> historical_data/interesting_files.txt
```

---

# 🔹 Step 2.6 — Identify API Endpoints

```bash
grep -E '/(api|v1|v2|rest|graphql)/' \
historical_data/unique_urls.txt \
> historical_data/api_endpoints.txt
```

---

# 🔹 Step 2.7 — Discover Admin Panels

```bash
grep -E '/(admin|panel|dashboard)' \
historical_data/unique_urls.txt \
> historical_data/admin_panels.txt
```

---

# 🔹 Step 2.8 — Generate Summary Statistics

```bash
echo "Interesting files: $(wc -l < historical_data/interesting_files.txt)"

echo "API endpoints: $(wc -l < historical_data/api_endpoints.txt)"

echo "Admin panels: $(wc -l < historical_data/admin_panels.txt)"
```

Example

```text
Interesting files: 17

API endpoints: 41

Admin panels: 6
```

---

# 📊 Task 2 Summary

At this stage you have successfully:

- Retrieved archived URLs
- Removed duplicate URLs
- Identified API endpoints
- Located admin panels
- Identified backup/configuration files
- Generated reconnaissance statistics

---

# 🏁 End of Part 1

The next section (**Part 2**) includes:

- 🐍 Complete Python Automation
- 📄 `asset_discovery.py`
- 📄 `report_generator.py`
- 🚀 Professional reporting automation
````````markdown
# 🤖 Task 3 — Automate Asset Discovery with Python

In this section, you will automate the complete reconnaissance workflow using Python. The scripts are designed as templates with `TODO` sections for you to implement as part of the lab.

---

# 🐍 Step 3.1 — Create `asset_discovery.py`

Create a new file named:

```text
asset_discovery.py
```

Add the following code:

```python
#!/usr/bin/env python3

import subprocess
import json
import sys
from datetime import datetime


class AssetDiscovery:
    def __init__(self, target_domain):
        """
        Initialize asset discovery.

        Args:
            target_domain: Target domain name
        """

        self.target_domain = target_domain

        self.results = {
            "domain": target_domain,
            "timestamp": datetime.now().isoformat(),
            "subdomains": [],
            "active_hosts": [],
            "historical_urls": []
        }

    def run_subfinder(self):
        """
        Discover subdomains.

        TODO:
        - Execute Subfinder using subprocess
        - Capture stdout
        - Parse discovered subdomains
        - Handle command failures
        """

        pass

    def probe_hosts(self):
        """
        Probe hosts using HTTPX.

        TODO:
        - Save subdomains into temporary file
        - Execute HTTPX
        - Read active hosts
        - Remove temporary files
        """

        pass

    def collect_wayback_data(self):
        """
        Collect historical URLs.

        TODO:
        - Execute waybackurls
        - Store URLs
        - Filter invalid entries
        """

        pass

    def analyze_findings(self):
        """
        Analyze reconnaissance results.

        TODO:
        - Locate API endpoints
        - Identify admin panels
        - Search backup files
        - Search configuration files
        """

        pass

    def generate_json_report(self):
        """
        Generate JSON report.

        TODO:
        - Save self.results
        - Include statistics
        """

        pass

    def run_full_discovery(self):
        """
        Execute the full workflow.

        TODO:
        - Call all functions
        - Print progress
        - Handle exceptions
        """

        pass


def main():
    """
    Main entry point.

    TODO:
    - Parse command-line arguments
    - Validate input
    - Execute workflow
    """

    pass


if __name__ == "__main__":
    main()
```

---

# 📌 What This Script Will Automate

After implementation it should:

- Discover subdomains
- Probe live hosts
- Download historical URLs
- Analyze URLs
- Generate JSON reports

---

# ⚙️ Step 3.2 — Create `report_generator.py`

Create:

```text
report_generator.py
```

Insert the following code.

```python
#!/usr/bin/env python3

import json
import sys


class HTMLReportGenerator:

    def __init__(self, json_report_path):
        """
        Initialize report generator.

        Args:
            json_report_path: JSON report path
        """

        self.report_path = json_report_path
        self.data = None

    def load_data(self):
        """
        Load JSON report.

        TODO:
        - Open JSON file
        - Parse data
        - Handle missing files
        """

        pass

    def generate_html_header(self):
        """
        Generate HTML header.

        TODO:
        - Add CSS
        - Add title
        """

        pass

    def generate_summary_section(self):
        """
        Summary section.

        TODO:
        - Display statistics
        """

        pass

    def generate_subdomain_table(self):
        """
        Create subdomain table.

        TODO:
        - Display first 50 entries
        - Mark active hosts
        """

        pass

    def generate_findings_section(self):
        """
        Findings section.

        TODO:
        - Critical findings
        - Recommendations
        """

        pass

    def save_report(self, output_path):
        """
        Save HTML report.

        TODO:
        - Combine sections
        - Save file
        """

        pass


def main():
    """
    Main entry.

    TODO:
    - Parse arguments
    - Generate report
    """

    pass


if __name__ == "__main__":
    main()
```

---

# 📊 Expected HTML Report

After completing the TODO sections your report should resemble:

```text
------------------------------------------------

 Asset Discovery Report

------------------------------------------------

Target Domain

example.com

------------------------------------------------

Summary

Subdomains Found : 87

Active Hosts : 36

Historical URLs : 1,142

API Endpoints : 49

Admin Panels : 6

Interesting Files : 18

------------------------------------------------

Recommendations

✓ Review exposed admin panels

✓ Remove obsolete endpoints

✓ Secure backup files

✓ Audit public APIs

------------------------------------------------
```

---

# 📁 Recommended Project Structure

```text
asset_discovery_lab/

│

├── asset_discovery.py

├── report_generator.py

├── subdomains.txt

├── active_hosts.txt

│

├── historical_data/

│   ├── wayback_urls.txt

│   ├── unique_urls.txt

│   ├── api_endpoints.txt

│   ├── admin_panels.txt

│   └── interesting_files.txt

│

└── reports/

    ├── report.json

    └── report.html
```

---

# 💡 Automation Workflow

```text
          Target Domain
                 │
                 ▼
          Subfinder Scan
                 │
                 ▼
          Subdomains List
                 │
                 ▼
             HTTPX Probe
                 │
                 ▼
           Active Hosts
                 │
                 ▼
          Wayback Machine
                 │
                 ▼
          Historical URLs
                 │
                 ▼
        Security Analysis
                 │
                 ▼
          JSON Report
                 │
                 ▼
          HTML Report
```

---

# ✅ Task 3 Progress Checklist

After completing this part you should have:

- ✅ Created `asset_discovery.py`
- ✅ Created `report_generator.py`
- ✅ Designed an automated reconnaissance workflow
- ✅ Prepared HTML reporting
- ✅ Generated JSON output structure

---

# 🏁 End of Part 2

The final section (**Part 3**) includes:

- 📈 `asset_monitor.py`
- 🧪 Testing the scripts
- 🎯 Expected Outcomes
- 🛠️ Troubleshooting
- 📚 Conclusion
- 💡 Key Takeaways
- 🎓 Professional GitHub README finishing section
````
````markdown
# 📡 Step 3.3 — Create `asset_monitor.py`

Create a new file named:

```text
asset_monitor.py
```

Add the following code:

```python
#!/usr/bin/env python3

import json
import os
from datetime import datetime


class AssetMonitor:
    def __init__(self, domain):
        """
        Initialize asset monitoring.

        Args:
            domain: Target domain
        """
        self.domain = domain
        self.reports_dir = f"reports_{domain}"

    def save_report(self, report_data):
        """
        Save timestamped report.

        TODO:
        - Create reports directory
        - Generate timestamped filename
        - Save JSON report
        """
        pass

    def get_latest_reports(self, count=2):
        """
        Retrieve latest reports.

        TODO:
        - List available reports
        - Sort by modification time
        - Return latest files
        """
        pass

    def compare_reports(self, old_report, new_report):
        """
        Compare reports.

        TODO:
        - Load JSON files
        - Compare subdomains
        - Compare active hosts
        - Compare historical URLs
        - Identify added and removed assets
        """
        pass

    def generate_change_report(self, changes):
        """
        Generate readable change report.

        TODO:
        - Format changes
        - Highlight additions
        - Highlight removals
        - Save report
        """
        pass


def main():
    """
    Main entry point.

    TODO:
    - Parse command-line arguments
    - Create AssetMonitor instance
    - Compare latest reports
    """

    pass


if __name__ == "__main__":
    main()
```

---

# 🧪 Step 3.4 — Test Your Scripts

Make all scripts executable.

```bash
chmod +x asset_discovery.py report_generator.py asset_monitor.py
```

Run the asset discovery script *(after implementing the TODO sections)*.

```bash
python3 asset_discovery.py example.com
```

Generate an HTML report.

```bash
python3 report_generator.py asset_discovery_report_example.com.json
```

Run the monitoring script.

```bash
python3 asset_monitor.py example.com
```

---

# 📁 Example Output Structure

```text
asset_discovery_lab/
│
├── asset_discovery.py
├── report_generator.py
├── asset_monitor.py
│
├── subdomains.txt
├── active_hosts.txt
│
├── historical_data/
│   ├── wayback_urls.txt
│   ├── unique_urls.txt
│   ├── api_endpoints.txt
│   ├── admin_panels.txt
│   └── interesting_files.txt
│
├── reports/
│   ├── asset_discovery_report_example.com.json
│   ├── asset_discovery_report.html
│   └── change_report.txt
│
└── reports_example.com/
    ├── report_2026-06-01.json
    ├── report_2026-06-15.json
    └── report_2026-06-30.json
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have successfully achieved the following:

- ✅ Discovered subdomains for the target domain
- ✅ Validated active web hosts using HTTPX
- ✅ Retrieved historical URLs from the Wayback Machine
- ✅ Identified API endpoints and administrative interfaces
- ✅ Detected interesting files such as backups and configuration files
- ✅ Built reusable Python automation scripts
- ✅ Generated professional JSON reports
- ✅ Generated HTML reports for documentation
- ✅ Created a monitoring workflow to track changes over time

---

# 📊 Skills Gained

By completing this lab, you have practiced:

- 🌐 Passive reconnaissance
- 🔍 Subdomain enumeration
- 📡 Asset discovery
- 📜 Historical URL collection
- 🧠 Reconnaissance data analysis
- 🐍 Python automation
- 📄 Report generation
- 📈 Continuous asset monitoring

---

# 🛠️ Troubleshooting

## ❌ Issue: `subfinder: command not found`

### Solution

Ensure the Go binary directory is added to your PATH.

```bash
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc

source ~/.bashrc
```

Verify the installation.

```bash
subfinder -version
```

---

## ❌ Issue: No subdomains discovered

### Solution

Some domains expose very few public subdomains.

Try testing against another well-known target.

Examples:

```text
tesla.com

hackerone.com

github.com
```

---

## ❌ Issue: `waybackurls` returns no results

### Solution

The selected domain may not have archived snapshots.

Choose a domain with a long public history.

---

## ❌ Issue: Python import errors

### Solution

Install the required dependencies.

```bash
pip3 install requests waybackpy
```

---

## ❌ Issue: Permission denied

### Solution

Grant execute permissions to the scripts.

```bash
chmod +x asset_discovery.py report_generator.py asset_monitor.py
```

---

# 🔐 Security Best Practices

- ✔️ Perform only **authorized** reconnaissance activities.
- ✔️ Respect program scopes and rules during bug bounty engagements.
- ✔️ Store API keys securely and never commit them to version control.
- ✔️ Validate findings before reporting them.
- ✔️ Protect generated reports if they contain sensitive information.
- ✔️ Use passive reconnaissance techniques whenever possible to minimize impact.

---

# 📚 Conclusion

In this lab, you learned how to discover and analyze digital assets using **Subfinder** and the **Wayback Machine**. You explored passive reconnaissance techniques to identify subdomains, validated live hosts with **HTTPX**, retrieved historical URLs, and analyzed archived data to uncover valuable security insights.

You also created reusable Python scripts that automate asset discovery, generate JSON and HTML reports, and monitor changes across multiple reconnaissance runs. These skills form the foundation of modern attack surface management, bug bounty hunting, penetration testing, and defensive security assessments.

---

# 💡 Key Takeaways

- Passive reconnaissance enables asset discovery without directly interacting with the target.
- Historical archives often reveal forgotten endpoints, legacy systems, and sensitive files.
- Subdomain enumeration helps expand visibility into an organization's attack surface.
- HTTP probing distinguishes active assets from inactive ones.
- Automation improves consistency, scalability, and efficiency during reconnaissance.
- Structured reporting supports communication, documentation, and remediation efforts.
- Continuous monitoring helps detect newly exposed assets and changes over time.

---

# 🚀 Next Steps

Expand your automation by integrating additional reconnaissance tools, such as:

- DNS enumeration utilities
- Certificate Transparency log searches
- Screenshot capture tools
- Port scanning utilities
- Notification systems (Slack, Discord, Email)
- Databases for long-term asset tracking
- CI/CD pipelines for scheduled reconnaissance
- Attack surface management platforms

---

# 📖 Additional Practice Ideas

- Enumerate multiple target domains and compare their attack surfaces.
- Extend the Python scripts to export findings as CSV or PDF.
- Integrate APIs from passive intelligence providers.
- Add screenshot collection for discovered web applications.
- Build dashboards to visualize historical asset growth.
- Schedule automated scans using `cron` or GitHub Actions.

---

# 🏆 Lab Completed Successfully!

Congratulations! 🎉

You have completed the **Discover Assets with Subfinder + Wayback** lab and built a solid foundation in passive reconnaissance, historical asset discovery, automation, reporting, and continuous monitoring. These practical skills are directly applicable to penetration testing, bug bounty hunting, red teaming, and attack surface management.

---

<div align="center">

### ⭐ If you found this lab helpful, consider giving the repository a star!

**Happy Hunting! 🕵️‍♂️**

</div>
````

