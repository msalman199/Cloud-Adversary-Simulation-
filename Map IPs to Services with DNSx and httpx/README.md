
# 🌐 Map IPs to Services with DNSx and HTTPX

<div align="center">

![Lab](https://img.shields.io/badge/Lab-DNS_Service_Mapping-blue?style=for-the-badge)

# 🔍 DNS Enumeration & HTTP Service Mapping

### Discover Domains • Resolve DNS Records • Map IP Addresses • Detect Web Technologies • Automate Reconnaissance

---

## 🛡️ Technology Stack

<p align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Go](https://img.shields.io/badge/Go-Programming-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DNSx](https://img.shields.io/badge/DNSx-ProjectDiscovery-blue?style=for-the-badge)
![HTTPX](https://img.shields.io/badge/HTTPX-Web_Service_Discovery-success?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-Enumeration-green?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-Service_Discovery-orange?style=for-the-badge)
![Cloud](https://img.shields.io/badge/Cloud-Asset_Discovery-blueviolet?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Reports-lightgrey?style=for-the-badge)
![CSV](https://img.shields.io/badge/CSV-Reporting-darkgreen?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-Dashboard-E34F26?style=for-the-badge&logo=html5&logoColor=white)

</p>

---

# 📖 Table of Contents

- Objectives
- Prerequisites
- Lab Environment
- Task 1 — DNS Enumeration with DNSx
- Task 2 — HTTP Service Discovery with HTTPX *(Part 2)*
- Task 3 — Python Automation *(Part 2)*
- Visualization Dashboard *(Part 3)*
- Verification *(Part 3)*
- Troubleshooting *(Part 4)*
- Advanced Extensions *(Part 4)*
- Conclusion *(Part 4)*

---

# 🎯 Objectives

By the end of this lab, you will be able to:

- ✅ Understand DNS enumeration using **DNSx**
- ✅ Resolve domains into IP addresses
- ✅ Enumerate DNS records
- ✅ Perform subdomain brute forcing
- ✅ Map IP addresses to HTTP services using **HTTPX**
- ✅ Detect web technologies
- ✅ Automate reconnaissance using Python
- ✅ Generate professional reports
- ✅ Visualize discovered services
- ✅ Perform cloud asset enumeration

---

# 📚 Prerequisites

Before beginning this lab, you should have:

- Basic understanding of DNS concepts
- Familiarity with Linux command-line operations
- Knowledge of HTTP and HTTPS
- Python scripting fundamentals
- Basic reconnaissance concepts

---

# 🖥️ Lab Environment

This lab is performed using an **Al Nafi pre-configured Linux cloud machine**.

All required tools are installed inside the environment.

No additional virtual machines are required.

---

# 🚩 Task 1 — DNS Enumeration using DNSx

---

# 🔹 Step 1.1 — Install DNSx

Update package repositories.

```bash
sudo apt update
```

Install Go.

```bash
sudo apt install golang-go -y
```

Install DNSx.

```bash
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

---

# 🔹 Step 1.2 — Configure PATH

```bash
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc

source ~/.bashrc
```

Verify installation.

```bash
dnsx -version
```

Example output

```text
dnsx version 1.x.x
```

---

# 🔹 Step 1.3 — Create Working Directory

```bash
mkdir ~/lab3-dns-mapping

cd ~/lab3-dns-mapping
```

---

# 🔹 Step 1.4 — Create Target Domain List

Create a sample domain list.

```bash
cat > domains.txt << EOF
google.com
github.com
stackoverflow.com
cloudflare.com
amazon.com
microsoft.com
EOF
```

Display contents.

```bash
cat domains.txt
```

Expected output

```text
google.com
github.com
stackoverflow.com
cloudflare.com
amazon.com
microsoft.com
```

---

# 🔹 Step 1.5 — Basic DNS Resolution

Resolve all domains.

```bash
dnsx -l domains.txt -a -resp
```

Save results.

```bash
dnsx -l domains.txt -a -resp -o dns_results.txt
```

View results.

```bash
cat dns_results.txt
```

Example

```text
google.com A 142.250.xx.xx

github.com A 140.82.xx.xx

amazon.com A 205.251.xx.xx
```

---

# 🔹 Step 1.6 — Comprehensive DNS Enumeration

Collect additional DNS records.

```bash
dnsx \
-l domains.txt \
-a \
-aaaa \
-cname \
-mx \
-ns \
-txt \
-resp \
-o comprehensive_dns.txt
```

View the results.

```bash
cat comprehensive_dns.txt
```

---

# 🔹 Step 1.7 — Extract IP Addresses

Extract only IPv4 addresses.

```bash
dnsx \
-l domains.txt \
-a \
-resp-only \
| grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' \
> ip_addresses.txt
```

Display discovered IPs.

```bash
echo "Discovered IP addresses:"
```

```bash
cat ip_addresses.txt
```

Example

```text
142.250.xxx.xxx

140.82.xxx.xxx

104.18.xxx.xxx

13.224.xxx.xxx
```

---

# 🔹 Step 1.8 — Create Subdomain Wordlist

```bash
cat > subdomains.txt << EOF
www
mail
ftp
admin
api
dev
test
staging
blog
shop
support
docs
EOF
```

Verify.

```bash
cat subdomains.txt
```

---

# 🔹 Step 1.9 — Perform DNS Bruteforcing

Enumerate common subdomains.

```bash
echo "google.com" \
| dnsx \
-w subdomains.txt \
-a \
-resp \
-o subdomain_results.txt
```

Display findings.

```bash
cat subdomain_results.txt
```

---

# 🔹 Step 1.10 — Build Unique IP List

Extract IP addresses.

```bash
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' \
subdomain_results.txt \
>> ip_addresses.txt
```

Remove duplicates.

```bash
sort ip_addresses.txt | uniq > unique_ips.txt
```

Display final IP list.

```bash
cat unique_ips.txt
```

---

# 📊 Task 1 Summary

You have successfully:

- ✅ Installed DNSx
- ✅ Configured Go environment
- ✅ Resolved domains
- ✅ Enumerated DNS records
- ✅ Collected A, AAAA, MX, NS, TXT, and CNAME records
- ✅ Performed DNS brute forcing
- ✅ Extracted discovered IP addresses
- ✅ Generated a clean IP inventory

---

# 📁 Files Generated

```text
lab3-dns-mapping/

├── domains.txt

├── dns_results.txt

├── comprehensive_dns.txt

├── subdomains.txt

├── subdomain_results.txt

├── ip_addresses.txt

└── unique_ips.txt
```

---

# 🏁 End of Part 1

The next section (**Part 2**) includes:

- 🌐 HTTP Service Discovery using HTTPX
- 🔍 Technology Detection
- 📊 Service Categorization
- 🐍 Complete `dns_service_mapper.py`
- 📄 CSV & Summary Report Generation
````
````markdown id="dns-httpx-part2"
# 🌐 Task 2 — Map Discovered IPs to Services using HTTPX

After identifying IP addresses with **DNSx**, the next step is to determine which web services are running on those hosts. In this task, you will use **HTTPX** to probe common HTTP/HTTPS ports, detect technologies, and categorize discovered services.

---

# 🔹 Step 2.1 — Install HTTPX

Install the latest version of HTTPX.

```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

Verify the installation.

```bash
httpx -version
```

Example output

```text
httpx version 1.x.x
```

---

# 🔹 Step 2.2 — Basic HTTP Service Discovery

Probe the discovered IP addresses.

```bash
httpx \
-l unique_ips.txt \
-ports 80,443,8080,8443 \
-o http_services.txt
```

View the results.

```bash
cat http_services.txt
```

Example

```text
http://142.250.xxx.xxx

https://140.82.xxx.xxx

https://104.18.xxx.xxx
```

---

# 🔹 Step 2.3 — Collect Detailed Service Information

Gather additional information such as:

- HTTP Status Code
- Page Title
- Technology Stack

```bash
httpx \
-l unique_ips.txt \
-ports 80,443,8080,8443,3000,5000,9000 \
-title \
-tech-detect \
-status-code \
-o detailed_services.txt
```

Display the results.

```bash
cat detailed_services.txt
```

Example

```text
https://github.com [200] GitHub • GitHub Pages

https://cloudflare.com [301] Cloudflare • nginx

https://google.com [200] Google
```

---

# 🔹 Step 2.4 — Comprehensive Service Enumeration

Collect advanced HTTP metadata.

```bash
httpx \
-l unique_ips.txt \
-ports 80,443,8080,8443,3000,5000,9000 \
-title \
-tech-detect \
-status-code \
-content-length \
-server \
-method \
-websocket \
-pipeline \
-http2 \
-o comprehensive_services.txt
```

Display results.

```bash
cat comprehensive_services.txt
```

---

# 🔹 Step 2.5 — Capture Screenshots *(Optional)*

Capture screenshots of discovered web applications.

```bash
httpx \
-l unique_ips.txt \
-screenshot \
-o screenshot_results.txt
```

---

# 🔹 Step 2.6 — Identify Common Web Servers

Search for common web servers.

```bash
grep -Ei "nginx|apache|iis" \
comprehensive_services.txt
```

Example

```text
Apache

nginx

Microsoft-IIS
```

---

# 🔹 Step 2.7 — Categorize Services

Create a categorized report.

```bash
echo "=== Web Servers ===" \
> service_categories.txt
```

Append web servers.

```bash
grep -Ei "nginx|apache|iis" \
comprehensive_services.txt \
>> service_categories.txt
```

Append cloud services.

```bash
echo -e "\n=== Cloud Services ===" \
>> service_categories.txt

grep -Ei "cloudflare|aws|azure|gcp" \
comprehensive_services.txt \
>> service_categories.txt
```

Append development services.

```bash
echo -e "\n=== Development/API Services ===" \
>> service_categories.txt

grep -E ":3000|:5000|:8080|:9000" \
comprehensive_services.txt \
>> service_categories.txt
```

Append HTTPS services.

```bash
echo -e "\n=== Secure Services (HTTPS) ===" \
>> service_categories.txt

grep "https://" \
comprehensive_services.txt \
>> service_categories.txt
```

Display categorized results.

```bash
cat service_categories.txt
```

---

# 📊 Task 2 Summary

You successfully:

- Installed HTTPX
- Probed discovered IP addresses
- Identified active web services
- Detected technologies
- Collected HTTP metadata
- Categorized discovered services
- Generated organized service inventories

---

# 🤖 Task 3 — Automate DNS & HTTP Enumeration with Python

---

# 🔹 Step 3.1 — Create `dns_service_mapper.py`

Create the file:

```text
dns_service_mapper.py
```

Add the following code.

```python
#!/usr/bin/env python3

import subprocess
import json
import csv
import os
from datetime import datetime


class DNSServiceMapper:

    def __init__(self, output_dir="lab3_results"):
        self.output_dir = output_dir
        self.create_output_directory()

    def create_output_directory(self):
        """
        Create output directory.

        TODO:
        - Create directory if missing
        """

        pass

    def run_dnsx_enumeration(self, domains_file):
        """
        Execute DNSx enumeration.

        TODO:
        - Execute DNSx
        - Save JSON output
        - Extract IP addresses
        """

        pass

    def run_httpx_enumeration(self, ips_file):
        """
        Execute HTTPX enumeration.

        TODO:
        - Probe web services
        - Save JSON results
        """

        pass

    def parse_results(self):
        """
        Parse DNS and HTTP output.

        TODO:
        - Read DNS JSON
        - Read HTTP JSON
        - Combine results
        """

        pass

    def generate_csv_report(self, results):
        """
        Generate CSV report.

        TODO:
        - Export mapping results
        """

        pass

    def generate_summary_report(self, results):
        """
        Generate statistics report.

        TODO:
        - Count status codes
        - Count technologies
        - Count server types
        - Save summary
        """

        pass


def main():
    """
    Main entry point.

    TODO:
    - Initialize mapper
    - Execute enumeration
    - Parse results
    - Generate reports
    """

    pass


if __name__ == "__main__":
    main()
```

---

# 📄 Save the Script

```bash
cat > dns_service_mapper.py << 'EOF'

# Paste the Python script here

EOF
```

Make the script executable.

```bash
chmod +x dns_service_mapper.py
```

---

# ▶️ Step 3.2 — Execute the Automation Script

Install the required Python package.

```bash
pip3 install requests
```

Run the automation.

```bash
python3 dns_service_mapper.py
```

View the generated files.

```bash
ls -la lab3_results/
```

Example output

```text
dns_results.json

http_services.json

service_mapping_report.csv

summary_report.txt

extracted_ips.txt
```

---

# 📁 Expected Project Structure

```text
lab3-dns-mapping/

│

├── domains.txt

├── unique_ips.txt

├── dns_service_mapper.py

│

├── lab3_results/

│   ├── dns_results.json

│   ├── http_services.json

│   ├── extracted_ips.txt

│   ├── service_mapping_report.csv

│   └── summary_report.txt
```

---

# 🔄 Automation Workflow

```text
             Target Domains
                    │
                    ▼
              DNSx Enumeration
                    │
                    ▼
             Extract IP Addresses
                    │
                    ▼
            HTTPX Enumeration
                    │
                    ▼
        Technology Detection
                    │
                    ▼
          Parse JSON Results
                    │
                    ▼
          CSV Report Generation
                    │
                    ▼
         Summary Statistics Report
```

---

# ✅ Progress Checklist

At this stage you have completed:

- ✅ DNS Enumeration
- ✅ HTTP Service Discovery
- ✅ Technology Detection
- ✅ Service Categorization
- ✅ Created `dns_service_mapper.py`
- ✅ Automated DNS & HTTP enumeration
- ✅ Generated CSV reports
- ✅ Generated summary reports

---

# 🏁 End of Part 2

The next section (**Part 3**) includes:

- 📊 `service_visualizer.py`
- 🌐 Interactive HTML Dashboard
- 📈 Charts and Graphs
- ✅ Verification & Testing
- 📂 Dashboard Generation
````
````markdown
# 📊 Task 3 — Visualize Service Mapping Results

After completing DNS and HTTP enumeration, it's useful to visualize the collected information. In this task, you'll build charts and an interactive dashboard to better understand discovered services, technologies, and HTTP responses.

---

# 🔹 Step 3.3 — Create `service_visualizer.py`

Create the following file:

```text
service_visualizer.py
```

Add the following code:

```python
#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


class ServiceVisualizer:
    def __init__(self, results_dir="lab3_results"):
        self.results_dir = results_dir

    def load_data(self):
        """
        Load CSV report.

        TODO:
        - Read CSV report
        - Return DataFrame
        """

        pass

    def create_status_code_chart(self, df):
        """
        Create HTTP status code chart.

        TODO:
        - Build bar chart
        - Save PNG
        """

        pass

    def create_technology_chart(self, df):
        """
        Create technology distribution chart.

        TODO:
        - Count technologies
        - Generate chart
        """

        pass

    def create_server_chart(self, df):
        """
        Create web server distribution chart.

        TODO:
        - Count server types
        - Save visualization
        """

        pass

    def generate_all_visualizations(self):
        """
        Generate every visualization.

        TODO:
        - Load CSV
        - Call chart functions
        """

        pass


def main():
    visualizer = ServiceVisualizer()
    visualizer.generate_all_visualizations()


if __name__ == "__main__":
    main()
```

---

# 🔹 Install Required Python Packages

```bash
pip3 install matplotlib pandas seaborn
```

---

# 🔹 Make the Script Executable

```bash
chmod +x service_visualizer.py
```

---

# 🔹 Run the Visualization Script

```bash
python3 service_visualizer.py
```

Generated files will include:

```text
status_code_distribution.png

technology_distribution.png

server_distribution.png
```

---

# 📈 Expected Charts

The script should generate:

- 📊 HTTP Status Code Distribution
- 🖥️ Server Distribution
- ⚙️ Technology Distribution
- 📈 Top Technologies
- 🌐 Web Server Statistics

---

# 🌐 Step 3.4 — Create Interactive Dashboard

Create:

```text
dashboard_generator.py
```

Insert the following code.

```python
#!/usr/bin/env python3

import pandas as pd
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time
import webbrowser


class DashboardGenerator:

    def __init__(self, results_dir="lab3_results"):
        self.results_dir = results_dir

    def generate_html_dashboard(self):
        """
        Generate HTML dashboard.

        TODO:
        - Read CSV report
        - Build HTML page
        - Create statistics cards
        - Create service table
        """

        pass

    def serve_dashboard(self):
        """
        Start local HTTP server.

        TODO:
        - Serve dashboard
        - Launch browser
        """

        pass


def main():
    dashboard = DashboardGenerator()

    dashboard.generate_html_dashboard()

    dashboard.serve_dashboard()


if __name__ == "__main__":
    main()
```

---

# 🔹 Save the Dashboard Script

```bash
cat > dashboard_generator.py << 'EOF'

# Paste the dashboard script here

EOF
```

---

# 🔹 Make Executable

```bash
chmod +x dashboard_generator.py
```

---

# 🔹 Launch Dashboard

```bash
python3 dashboard_generator.py
```

Open:

```text
http://localhost:8000/dashboard.html
```

---

# 🖥️ Dashboard Features

The HTML dashboard should display:

- 📊 Summary Statistics
- 🌍 Total Services
- 🌐 HTTP Status Codes
- ⚙️ Technologies
- 🖥️ Web Servers
- 📋 Service Inventory
- 🔗 Clickable URLs
- 📈 Interactive Layout

---

# 📂 Expected Directory Structure

```text
lab3-dns-mapping/

│

├── dns_service_mapper.py

├── service_visualizer.py

├── dashboard_generator.py

│

├── lab3_results/

│   ├── dns_results.json

│   ├── http_services.json

│   ├── extracted_ips.txt

│   ├── service_mapping_report.csv

│   ├── summary_report.txt

│   ├── status_code_distribution.png

│   ├── technology_distribution.png

│   ├── server_distribution.png

│   └── dashboard.html
```

---

# ✅ Verification & Testing

Verify generated files.

```bash
echo "=== Generated Files ==="

ls -la lab3_results/
```

---

## Check DNS Results

```bash
head -5 lab3_results/dns_results.json
```

---

## Check HTTP Results

```bash
head -5 lab3_results/http_services.json
```

---

## Check CSV Report

```bash
head -5 lab3_results/service_mapping_report.csv
```

---

## Display Summary Report

```bash
cat lab3_results/summary_report.txt
```

---

# 📋 Expected Output

```text
==================================================

DNS & HTTP Service Mapping Summary

==================================================

Total Services: 42

HTTP 200 : 31

HTTP 301 : 4

HTTP 302 : 3

HTTP 403 : 2

HTTP 404 : 2

--------------------------------------------------

Top Technologies

Cloudflare

Nginx

Apache

React

Bootstrap

--------------------------------------------------

Top Servers

nginx

Apache

Microsoft IIS

CloudFront

--------------------------------------------------
```

---

# 📊 Visualization Workflow

```text
           DNS Results
                │
                ▼
        HTTP Enumeration
                │
                ▼
         JSON Processing
                │
                ▼
         CSV Report Export
                │
                ▼
      Visualization Engine
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
 PNG Charts       HTML Dashboard
        │                │
        └───────┬────────┘
                ▼
      Security Assessment
```

---

# ✅ Progress Checklist

At this point you have successfully:

- ✅ Created `dns_service_mapper.py`
- ✅ Created `service_visualizer.py`
- ✅ Created `dashboard_generator.py`
- ✅ Generated CSV reports
- ✅ Generated summary reports
- ✅ Created PNG visualizations
- ✅ Built an interactive HTML dashboard
- ✅ Verified generated outputs

---

# 🏁 End of Part 3

The final section (**Part 4**) includes:

- 🛠️ Troubleshooting Common Issues
- 🚀 Advanced Extensions
- 📡 Port Scanning Integration
- ⏱️ Continuous Monitoring
- 🎯 Conclusion
- 💡 Key Takeaways
- 🏆 Professional GitHub README Ending
````
````markdown id="dns-httpx-part4"
# 🛠️ Troubleshooting Common Issues

This section covers the most common problems you may encounter while completing this lab and their recommended solutions.

---

# ❌ Issue 1 — `dnsx` or `httpx` Command Not Found

## Cause

The Go binary directory is not included in your `PATH`, or the tools were not installed successfully.

## ✅ Solution

Export the Go binary directory.

```bash
export PATH=$PATH:~/go/bin
```

Reload your shell configuration.

```bash
source ~/.bashrc
```

Reinstall the tools if necessary.

```bash
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest

go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

Verify installations.

```bash
dnsx -version

httpx -version
```

---

# ❌ Issue 2 — Python Modules Not Found

## Cause

Required Python libraries have not been installed.

## ✅ Solution

Install the required packages.

```bash
pip3 install pandas matplotlib seaborn requests
```

If `pip3` is unavailable:

```bash
sudo apt install python3-pip -y
```

Verify installation.

```bash
python3 -m pip list
```

---

# ❌ Issue 3 — No DNS Results

## Cause

The target domain may not resolve or DNS enumeration failed.

## ✅ Solution

Verify DNS resolution.

```bash
nslookup google.com
```

Test DNSx manually.

```bash
echo "google.com" | dnsx -a -resp
```

Check Internet connectivity.

```bash
ping -c 4 google.com
```

---

# ❌ Issue 4 — HTTPX Returns No Services

## Cause

The discovered hosts may not expose HTTP services on the scanned ports.

## ✅ Solution

Test HTTPX manually.

```bash
echo "https://google.com" | httpx -title
```

Expand the scanned ports.

```bash
httpx \
-l unique_ips.txt \
-ports 80,443,8080,8443,3000,5000,8000,9000
```

---

# ❌ Issue 5 — Permission Denied

## Cause

Python scripts are not executable.

## ✅ Solution

Grant execute permissions.

```bash
chmod +x *.py
```

Verify permissions.

```bash
ls -la
```

---

# ❌ Issue 6 — Dashboard Does Not Open

## Cause

The dashboard web server failed to start or the browser did not launch automatically.

## ✅ Solution

Run the dashboard manually.

```bash
python3 dashboard_generator.py
```

Open your browser.

```text
http://localhost:8000/dashboard.html
```

---

# 🚀 Advanced Extensions

Expand the lab with additional reconnaissance capabilities.

---

# 🔹 Extension 1 — Custom DNS Wordlists

Create a custom subdomain wordlist.

```bash
cat > custom_subdomains.txt << EOF
api
admin
dev
test
staging
prod
www
mail
ftp
ssh
vpn
portal
dashboard
EOF
```

Run DNS brute forcing.

```bash
echo "target-domain.com" \
| dnsx \
-w custom_subdomains.txt \
-a \
-resp
```

---

# 🔹 Extension 2 — Port Scanning Integration

Install Nmap.

```bash
sudo apt install nmap -y
```

Create:

```text
port_scanner.py
```

```python
import subprocess


def scan_ports(ip_file):
    """
    Scan discovered IP addresses.

    TODO:
    - Read IP list
    - Execute Nmap
    - Display results
    """

    pass


if __name__ == "__main__":
    scan_ports("lab3_results/extracted_ips.txt")
```

Run the scanner.

```bash
python3 port_scanner.py
```

---

# 🔹 Extension 3 — Continuous Monitoring

Create:

```text
monitor_services.py
```

```python
import subprocess
import time
from datetime import datetime


def monitor_services():
    """
    Monitor HTTP services.

    TODO:
    - Execute HTTPX
    - Save results
    - Repeat every 5 minutes
    """

    pass


if __name__ == "__main__":
    monitor_services()
```

Run the monitor.

```bash
python3 monitor_services.py
```

---

# 📊 Complete Lab Workflow

```text
                   Target Domains
                          │
                          ▼
                  DNS Enumeration
                          │
                          ▼
                 DNS Record Collection
                          │
                          ▼
                Subdomain Enumeration
                          │
                          ▼
                 Extract IP Addresses
                          │
                          ▼
                HTTP Service Discovery
                          │
                          ▼
             Technology Detection
                          │
                          ▼
               JSON Data Processing
                          │
                          ▼
                  CSV Report Export
                          │
                          ▼
             Summary Report Generation
                          │
                          ▼
              Visualization Engine
                 ┌────────┴────────┐
                 ▼                 ▼
           PNG Charts       HTML Dashboard
                 │                 │
                 └────────┬────────┘
                          ▼
            Continuous Asset Monitoring
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have:

- ✅ Enumerated DNS records using DNSx
- ✅ Resolved domains into IP addresses
- ✅ Performed subdomain brute forcing
- ✅ Mapped IP addresses to HTTP services
- ✅ Identified active web applications
- ✅ Detected web technologies
- ✅ Collected HTTP metadata
- ✅ Automated reconnaissance with Python
- ✅ Generated JSON, CSV, and text reports
- ✅ Built visualization charts
- ✅ Created an interactive HTML dashboard
- ✅ Implemented continuous monitoring concepts

---

# 🧠 Skills Acquired

Throughout this lab, you practiced:

- 🌐 DNS Enumeration
- 🔍 Passive Reconnaissance
- 📡 Service Discovery
- ☁️ Cloud Asset Enumeration
- ⚙️ HTTP Technology Detection
- 🐍 Python Automation
- 📊 Data Analysis
- 📈 Data Visualization
- 🖥️ Dashboard Development
- 📋 Security Reporting

---

# 🔐 Security Best Practices

Always follow responsible security practices:

- ✔️ Perform reconnaissance only on systems you own or are authorized to assess.
- ✔️ Respect bug bounty program scopes and disclosure policies.
- ✔️ Protect generated reports containing potentially sensitive information.
- ✔️ Secure API keys and credentials using environment variables or secrets management.
- ✔️ Validate findings before reporting them.
- ✔️ Keep reconnaissance activities documented for future reference.

---

# 📚 Conclusion

In this lab, you learned how to perform comprehensive **DNS enumeration** with **DNSx** and map discovered IP addresses to running web services using **HTTPX**. You practiced resolving domains, collecting DNS records, performing subdomain brute forcing, probing HTTP services, identifying technologies, and generating structured reports.

You also built Python automation to streamline reconnaissance workflows, produced CSV and summary reports, created visualization charts, and developed an interactive HTML dashboard to analyze discovered assets more effectively.

These techniques are fundamental for cloud security assessments, penetration testing, attack surface management, adversary simulation, and continuous infrastructure monitoring. The automation and reporting workflows developed in this lab provide a strong foundation for real-world reconnaissance and cloud asset discovery.

---

# 💡 Key Takeaways

- DNS enumeration reveals valuable infrastructure information.
- IP-to-service mapping provides visibility into exposed web applications.
- HTTPX simplifies technology fingerprinting and service discovery.
- Automation improves consistency and efficiency during reconnaissance.
- Visual reports and dashboards make findings easier to analyze and communicate.
- Continuous monitoring helps identify newly exposed services and infrastructure changes.
- Proper documentation is essential for professional security assessments.

---

# 📖 Additional Practice

Continue improving your reconnaissance skills by:

- Building larger custom subdomain wordlists.
- Integrating Certificate Transparency log searches.
- Adding WHOIS lookups and ASN mapping.
- Collecting screenshots of discovered web applications.
- Exporting reports to PDF.
- Integrating Slack or Discord notifications.
- Scheduling recurring scans with Cron or GitHub Actions.
- Expanding dashboards with interactive charts and filtering.

---

# 🏆 Congratulations!

You have successfully completed the **Map IPs to Services with DNSx and HTTPX** lab.

You now have practical experience with:

- 🌐 DNS Enumeration
- 📡 Service Discovery
- ☁️ Cloud Asset Mapping
- ⚙️ Technology Fingerprinting
- 🐍 Python Automation
- 📊 Data Visualization
- 🖥️ Interactive Dashboards
- 📋 Professional Security Reporting

These skills are directly applicable to **Cloud Security**, **Attack Surface Management**, **Penetration Testing**, **Red Team Operations**, **Bug Bounty Hunting**, and the **CCASE (Certified Cloud Adversary Simulation Expert)** learning path.

---

<div align="center">

## ⭐ If this repository helped you learn something new, consider giving it a star!

### 🚀 Happy Reconnaissance & Secure Hunting!

**Made with ❤️ for Cloud Security Learners**

</div>
````


