# 🔎 Automate Recon with Amass + Commonspeak2

> **Lab Category:** Cloud Reconnaissance & Asset Discovery  
> **Difficulty:** Intermediate  
> **Platform:** Linux (Ubuntu 20.04+)  
> **Estimated Time:** 2–3 Hours

---

# 📖 Overview

Reconnaissance is the first phase of every security assessment. In cloud environments, organizations often expose multiple services through subdomains, APIs, storage buckets, dashboards, and development environments.

In this lab you will learn how to automate reconnaissance using **OWASP Amass**, **Commonspeak2**, and **Python** to discover cloud assets and process reconnaissance results into useful reports.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- ✅ Install and configure **OWASP Amass**
- ✅ Perform automated subdomain enumeration
- ✅ Use Commonspeak2 wordlists
- ✅ Create Python automation scripts
- ✅ Process reconnaissance results automatically
- ✅ Generate structured reports
- ✅ Understand cloud reconnaissance methodology
- ✅ Apply reconnaissance techniques relevant to the **CCASE** certification

---

# 📚 Prerequisites

Students should have:

- Linux command line knowledge
- Basic DNS concepts
- Understanding of subdomains
- Basic Python programming
- Knowledge of AWS, Azure and GCP
- Basic cybersecurity reconnaissance concepts

> **Note**
>
> Al Nafi provides a ready-to-use Linux machine.
> Simply click **Start Lab** and begin.

---

# 🖥️ Lab Environment

This lab runs on **one Linux machine**.

No additional VMs or remote systems are required.

Installed tools include:

- Python 3
- Git
- wget
- curl
- unzip
- pip
- GCC
- Internet connectivity

---

# 🧩 Task 1 — Install and Configure Amass

---

## 🔹 Step 1.1 Install Amass

Update packages:

```bash
sudo apt update
```

Install dependencies:

```bash
sudo apt install -y wget curl git build-essential
```

Download Amass:

```bash
wget https://github.com/OWASP/Amass/releases/download/v3.23.3/amass_linux_amd64.zip
```

Extract archive:

```bash
unzip amass_linux_amd64.zip
```

Move binary:

```bash
sudo mv amass_linux_amd64/amass /usr/local/bin/
```

Verify installation:

```bash
amass version
```

Expected output:

```
amass version 3.23.3
```

---

## 🔹 Step 1.2 Configure Data Sources

Create configuration directory:

```bash
mkdir -p ~/.config/amass
```

Create configuration file:

```bash
cat > ~/.config/amass/config.ini << 'EOF'
[data_sources]
minimum_ttl = 1440

[data_sources.AlienVault]
[data_sources.Ask]
[data_sources.Baidu]
[data_sources.Bing]
[data_sources.CertSpotter]
[data_sources.CIRCL]
[data_sources.CommonCrawl]
[data_sources.Crtsh]
[data_sources.DNSdb]
[data_sources.DNSDumpster]
[data_sources.DNSrepo]
[data_sources.Dogpile]
[data_sources.Exalead]
[data_sources.FindSubDomains]
[data_sources.Google]
[data_sources.HackerTarget]
[data_sources.IPv4Info]
[data_sources.Netcraft]
[data_sources.PassiveTotal]
[data_sources.Riddler]
[data_sources.SecurityTrails]
[data_sources.Shodan]
[data_sources.ThreatCrowd]
[data_sources.VirusTotal]
[data_sources.Yahoo]
[data_sources.Yandex]
EOF
```

---

## 🔹 Step 1.3 Create Working Directory

```bash
mkdir ~/recon_lab
cd ~/recon_lab
```

---

## 🔹 Step 1.4 Basic Enumeration

Run:

```bash
amass enum -d example.com -o amass_basic_results.txt
```

View results:

```bash
cat amass_basic_results.txt
```

Example output:

```
www.example.com
mail.example.com
api.example.com
dev.example.com
```

---

## 🔹 Step 1.5 Passive Enumeration

```bash
amass enum \
-passive \
-d example.com \
-o amass_passive.txt
```

Passive mode avoids active probing and relies on public data sources.

---

## 🔹 Step 1.6 Comprehensive Enumeration

Run brute-force enumeration:

```bash
amass enum \
-d example.com \
-brute \
-w /usr/share/wordlists/amass/subdomains-top1mil-5000.txt \
-o amass_comprehensive.txt
```

This command uses a large wordlist to discover hidden subdomains.

---

## 🔹 Step 1.7 Generate Visualization

Generate graph data:

```bash
amass viz \
-d3 \
-d example.com
```

Amass creates visualization files showing relationships between:

- Domains
- Subdomains
- DNS Records
- IP Addresses
- Autonomous Systems

---

# ✅ Task 1 Complete

At this point you should have:

- Installed OWASP Amass
- Configured data sources
- Performed passive enumeration
- Performed brute-force enumeration
- Generated visualization data
- Saved reconnaissance results
## 🔹 Task 2: Implement Commonspeak2 for Cloud Asset Enumeration

### 🎯 Objective

In this task, you will:

- Install and configure Commonspeak2 wordlists
- Automate cloud asset discovery using Python
- Enumerate common cloud subdomains
- Save and analyze discovered assets

---

# 📌 Subtask 2.1 – Install Commonspeak2

Clone the Commonspeak2 repository.

```bash
git clone https://github.com/assetnote/commonspeak2-wordlists.git
cd commonspeak2-wordlists
```

View available wordlists.

```bash
ls -la
```

Return to the lab directory.

```bash
cd ~/recon_lab
```

---

# 📌 Subtask 2.2 – Create Cloud Enumeration Script

Create the automation script.

```bash
nano create_cloud_script.py
```

Paste the following code.

```python
#!/usr/bin/env python3

import os

def create_cloud_enum_script():

    script_content = '''#!/usr/bin/env python3

import requests
import threading
import sys
import os

from concurrent.futures import ThreadPoolExecutor

class CloudAssetEnumerator:

    def __init__(self, target_domain):

        self.target_domain = target_domain
        self.results = []
        self.lock = threading.Lock()

    def check_subdomain(self, subdomain):

        full_domain = f"{subdomain}.{self.target_domain}"

        try:
            response = requests.get(
                f"http://{full_domain}",
                timeout=5,
                allow_redirects=True
            )

            if response.status_code == 200:

                with self.lock:

                    self.results.append(
                        f"{full_domain} - HTTP - {response.status_code}"
                    )

                    print(f"[+] Found HTTP: {full_domain}")

                return True

        except:
            pass

        try:

            response = requests.get(
                f"https://{full_domain}",
                timeout=5,
                verify=False,
                allow_redirects=True
            )

            if response.status_code == 200:

                with self.lock:

                    self.results.append(
                        f"{full_domain} - HTTPS - {response.status_code}"
                    )

                    print(f"[+] Found HTTPS: {full_domain}")

                return True

        except:
            pass

        return False

    def enumerate(self):

        cloud_subdomains = [

            "api",
            "app",
            "admin",
            "dev",
            "test",
            "staging",
            "prod",
            "portal",
            "dashboard",
            "cdn",
            "assets",
            "media",
            "static",
            "files",
            "docs",
            "support",
            "status",
            "metrics",
            "monitor",
            "images",
            "blog",
            "mail",
            "ftp",
            "shop",
            "store"

        ]

        print("[*] Starting Cloud Enumeration...")

        with ThreadPoolExecutor(max_workers=10) as executor:

            executor.map(self.check_subdomain, cloud_subdomains)

    def save(self):

        filename = f"cloud_assets_{self.target_domain}.txt"

        with open(filename, "w") as f:

            for item in self.results:
                f.write(item + "\\n")

        print(f"[+] Saved results to {filename}")

def main():

    if len(sys.argv) != 2:

        print("Usage: python3 cloud_enum.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    enum = CloudAssetEnumerator(domain)

    enum.enumerate()

    enum.save()

    print(f"[+] Total Assets Found: {len(enum.results)}")

if __name__ == "__main__":
    main()
'''

    with open("cloud_enum.py", "w") as f:
        f.write(script_content)

    os.chmod("cloud_enum.py", 0o755)

    print("[+] cloud_enum.py created successfully")

create_cloud_enum_script()
```

---

# 📌 Generate the Enumeration Script

Execute:

```bash
python3 create_cloud_script.py
```

Verify the file.

```bash
ls -la cloud_enum.py
```

Expected output:

```
-rwxr-xr-x cloud_enum.py
```

---

# 📌 Install Python Dependency

```bash
pip3 install requests
```

---

# 📌 Run Cloud Enumeration

Enumerate a sample domain.

```bash
python3 cloud_enum.py example.com
```

---

# 📌 View Results

```bash
cat cloud_assets_example.com.txt
```

Example:

```
api.example.com - HTTPS - 200
cdn.example.com - HTTPS - 200
static.example.com - HTTP - 200
assets.example.com - HTTPS - 200
```

---

# 📌 Understanding the Script

The automation performs the following steps:

- Builds common cloud-related subdomains
- Checks HTTP connectivity
- Checks HTTPS connectivity
- Uses multithreading
- Saves discovered assets
- Produces reusable output

---

# 📌 Why Commonspeak2?

Commonspeak2 contains thousands of real-world cloud asset names such as:

```
admin
portal
cdn
storage
media
assets
dashboard
backup
api
gateway
files
static
```

These names greatly improve cloud reconnaissance coverage.

---

# 📌 Verification Checklist

Ensure the following:

- ✅ Commonspeak2 repository cloned
- ✅ cloud_enum.py created
- ✅ requests installed
- ✅ Enumeration completed successfully
- ✅ Results saved to file

---

# ✅ Task 2 Complete

You have successfully:

- Installed Commonspeak2
- Created an automated cloud asset discovery tool
- Enumerated cloud infrastructure
- Saved reconnaissance results for further analysis

The next task will process these results into CSV, JSON, Markdown reports, and build a complete automated reconnaissance workflow.

- ## 🔹 Task 3: Automate Results Processing and Visualization

### 🎯 Objective

In this task, you will:

- Process Amass and cloud enumeration results
- Generate useful reconnaissance statistics
- Export findings into CSV and JSON formats
- Create a professional Markdown summary report
- Build a fully automated reconnaissance workflow

---

# 📌 Subtask 3.1 – Create Results Processing Script

Create the Python script.

```bash
nano create_processor.py
```

Paste the following code.

```python
#!/usr/bin/env python3

import os

def create_results_processor():

    script_content = '''#!/usr/bin/env python3

import os
import csv
import json
from collections import Counter, defaultdict

class ReconResultsProcessor:

    def __init__(self):

        self.amass_results = []
        self.cloud_results = []

    def load_amass_results(self, filename):

        if not os.path.exists(filename):
            print("[-] Missing Amass results")
            return

        with open(filename) as f:
            self.amass_results = [
                line.strip()
                for line in f
                if line.strip()
            ]

        print(f"[+] Loaded {len(self.amass_results)} Amass results")

    def load_cloud_results(self, filename):

        if not os.path.exists(filename):
            print("[-] Missing Cloud results")
            return

        with open(filename) as f:
            self.cloud_results = [
                line.strip()
                for line in f
                if line.strip()
            ]

        print(f"[+] Loaded {len(self.cloud_results)} Cloud results")

    def analyze(self):

        domains = self.amass_results + [
            item.split(" - ")[0]
            for item in self.cloud_results
        ]

        patterns = defaultdict(int)

        tlds = defaultdict(int)

        for domain in domains:

            parts = domain.split(".")

            if len(parts) >= 2:

                patterns[parts[0]] += 1
                tlds[".".join(parts[-2:])] += 1

        return patterns, tlds

    def statistics(self):

        patterns, tlds = self.analyze()

        return {

            "amass": len(self.amass_results),

            "cloud": len(self.cloud_results),

            "unique": len(set(
                self.amass_results +
                [x.split(" - ")[0] for x in self.cloud_results]
            )),

            "patterns": Counter(patterns).most_common(10),

            "tlds": Counter(tlds).most_common(5)

        }

    def export_csv(self):

        with open("recon_results.csv","w",newline="") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Domain",
                "Source",
                "Protocol",
                "Status"
            ])

            for item in self.amass_results:

                writer.writerow([
                    item,
                    "Amass",
                    "DNS",
                    "Discovered"
                ])

            for item in self.cloud_results:

                parts = item.split(" - ")

                if len(parts)==3:

                    writer.writerow([
                        parts[0],
                        "Cloud",
                        parts[1],
                        parts[2]
                    ])

        print("[+] CSV exported")

    def export_json(self):

        data = {

            "amass_results": self.amass_results,

            "cloud_results": self.cloud_results,

            "statistics": self.statistics()

        }

        with open("recon_results.json","w") as f:

            json.dump(data,f,indent=4)

        print("[+] JSON exported")

    def markdown_report(self):

        stats = self.statistics()

        report = "# Reconnaissance Report\\n\\n"

        report += "## Statistics\\n"

        report += f"- Amass Results: {stats['amass']}\\n"

        report += f"- Cloud Results: {stats['cloud']}\\n"

        report += f"- Unique Domains: {stats['unique']}\\n\\n"

        report += "## Top Subdomains\\n"

        for item,count in stats["patterns"]:

            report += f"- {item}: {count}\\n"

        report += "\\n## Top TLDs\\n"

        for item,count in stats["tlds"]:

            report += f"- {item}: {count}\\n"

        with open("recon_summary.md","w") as f:

            f.write(report)

        print("[+] Markdown report created")

def main():

    processor = ReconResultsProcessor()

    processor.load_amass_results("amass_comprehensive.txt")

    processor.load_cloud_results("cloud_assets_example.com.txt")

    processor.export_csv()

    processor.export_json()

    processor.markdown_report()

    print("\\n[+] Processing completed successfully")

if __name__ == "__main__":
    main()
'''

    with open("process_results.py","w") as f:
        f.write(script_content)

    os.chmod("process_results.py",0o755)

    print("[+] process_results.py created")

create_results_processor()
```

---

# 📌 Generate the Processing Script

```bash
python3 create_processor.py
```

Verify it exists.

```bash
ls -la process_results.py
```

---

# 📌 Install Required Libraries

```bash
pip3 install pandas matplotlib
```

---

# 📌 Process Reconnaissance Results

```bash
python3 process_results.py
```

Expected output:

```
Loaded Amass results

Loaded Cloud results

CSV exported

JSON exported

Markdown report created

Processing completed successfully
```

---

# 📌 Generated Files

```
recon_results.csv

recon_results.json

recon_summary.md
```

---

# 📌 CSV Output Example

```
Domain,Source,Protocol,Status

api.example.com,Cloud,HTTPS,200

mail.example.com,Cloud,HTTP,200

www.example.com,Amass,DNS,Discovered
```

---

# 📌 JSON Output Example

```json
{
  "statistics": {
    "amass": 24,
    "cloud": 9,
    "unique": 31
  }
}
```

---

# 📌 Markdown Report Example

```markdown
# Reconnaissance Report

## Statistics

- Amass Results: 24

- Cloud Results: 9

- Unique Domains: 31

## Top Subdomains

api

mail

cdn

admin

dashboard
```

---

# 📌 Subtask 3.2 – Create Automated Reconnaissance Workflow

Create the master automation script.

```bash
nano automated_recon.sh
```

Paste the following Bash script.

```bash
#!/bin/bash

echo "==========================================="
echo " Automated Reconnaissance Workflow "
echo "==========================================="

if [ $# -eq 0 ]; then
    echo "Usage: $0 <domain>"
    exit
fi

DOMAIN=$1

mkdir -p results

echo "[1/4] Running Passive Enumeration"

amass enum -passive \
-d $DOMAIN \
-o results/amass_passive.txt

echo "[2/4] Running Active Enumeration"

amass enum \
-d $DOMAIN \
-brute \
-o results/amass_active.txt

sort -u \
results/amass_passive.txt \
results/amass_active.txt \
> results/amass_all.txt

echo "[3/4] Running Cloud Enumeration"

python3 cloud_enum.py $DOMAIN

mv cloud_assets_$DOMAIN.txt results/

echo "[4/4] Processing Results"

cp process_results.py results/

cd results

mv amass_all.txt amass_comprehensive.txt

mv cloud_assets_$DOMAIN.txt \
cloud_assets_example.com.txt

python3 process_results.py

echo
echo "Workflow Complete!"
echo
```

Save and exit.

---

# 📌 Make the Workflow Executable

```bash
chmod +x automated_recon.sh
```

---

# 📌 Run the Automated Workflow

```bash
./automated_recon.sh example.com
```

Example output:

```
Running Passive Enumeration

Running Active Enumeration

Running Cloud Enumeration

Processing Results

Workflow Complete!
```

---

# 📌 Review Generated Files

```bash
ls results
```

Expected:

```
amass_passive.txt

amass_active.txt

amass_comprehensive.txt

cloud_assets_example.com.txt

recon_results.csv

recon_results.json

recon_summary.md
```

---

# 📌 Verification Checklist

Ensure the following tasks have completed successfully.

✅ Results processor created

✅ CSV report generated

✅ JSON report generated

✅ Markdown summary generated

✅ Automated workflow created

✅ End-to-end automation executed successfully

---

# ✅ Task 3 Complete

You have successfully:

- Processed reconnaissance data
- Generated structured CSV reports
- Exported JSON data
- Created Markdown summaries
- Built a fully automated reconnaissance workflow

The next section covers verification, troubleshooting, optimization techniques, security best practices, and the lab conclusion.

# 🔹 Verification and Testing

After completing the automation workflow, verify that all tools, scripts, and outputs are functioning correctly.

---

# 📌 Verify Tool Installation

Check that Amass is installed properly.

```bash
amass version
```

Verify that all Python scripts are executable.

```bash
ls -la *.py
```

Test that all required Python modules are available.

```bash
python3 -c "import requests, json, csv; print('All dependencies available')"
```

Expected output:

```
All dependencies available
```

---

# 📌 Test Individual Components

## Test Amass

Run a quick passive scan.

```bash
amass enum -passive -d google.com -timeout 30
```

---

## Test Cloud Enumeration

```bash
python3 cloud_enum.py google.com
```

---

## Test Results Processing

```bash
python3 process_results.py
```

---

# 🔹 Troubleshooting Common Issues

---

## Issue 1 — Amass Installation Problems

If installation fails, install via Snap.

```bash
sudo snap install amass
```

Or compile from source.

```bash
git clone https://github.com/OWASP/Amass.git

cd Amass

make build

sudo cp ./amass /usr/local/bin/
```

---

## Issue 2 — Missing Python Dependencies

Install the required packages.

```bash
pip3 install --user requests pandas matplotlib
```

If pip is unavailable:

```bash
sudo apt install python3-pip
```

---

## Issue 3 — Permission Errors

Give execute permissions.

```bash
chmod +x *.sh *.py
```

Fix directory permissions.

```bash
chmod 755 ~/recon_lab
```

---

## Issue 4 — Network Connectivity Problems

Verify Internet connectivity.

```bash
ping -c 3 8.8.8.8
```

Verify DNS resolution.

```bash
nslookup example.com
```

Verify outbound HTTPS.

```bash
curl -I https://www.google.com
```

---

# 🔹 Advanced Techniques

---

## Optimizing Amass Performance

Use a configuration file.

```bash
amass enum \
-config ~/.config/amass/config.ini \
-d target.com
```

Increase timeout.

```bash
amass enum \
-timeout 30 \
-d target.com
```

Display source information.

```bash
amass enum \
-src \
-d target.com
```

---

## Enhancing Cloud Enumeration

Create a custom AWS wordlist.

```bash
cat > aws_subdomains.txt << EOF
s3
ec2
rds
lambda
cloudfront
ecs
eks
elb
api-gateway
EOF
```

Modify the cloud enumeration script to use this custom wordlist.

---

# 🔹 Automated HTML Report Generation

Create a reporting script.

```bash
nano generate_report.sh
```

Paste:

```bash
#!/bin/bash

TARGET=$1

DATE=$(date +"%Y-%m-%d")

REPORT="report_${TARGET}_${DATE}.html"

echo "<html>" > $REPORT
echo "<head><title>Recon Report</title></head>" >> $REPORT
echo "<body>" >> $REPORT

echo "<h1>Reconnaissance Report</h1>" >> $REPORT

echo "<h2>$TARGET</h2>" >> $REPORT

echo "<table border='1'>" >> $REPORT

head -1 recon_results.csv \
| sed 's/,/<\/th><th>/g' \
| sed 's/^/<tr><th>/' \
| sed 's/$/<\/th><\/tr>/' \
>> $REPORT

tail -n +2 recon_results.csv \
| sed 's/,/<\/td><td>/g' \
| sed 's/^/<tr><td>/' \
| sed 's/$/<\/td><\/tr>/' \
>> $REPORT

echo "</table>" >> $REPORT

echo "</body></html>" >> $REPORT

echo "Report generated successfully."
```

Make it executable.

```bash
chmod +x generate_report.sh
```

Generate the report.

```bash
./generate_report.sh example.com
```

---

# 🔹 Security Considerations

---

## Ethical Reconnaissance

✔ Always obtain written authorization before reconnaissance.

✔ Prefer passive information gathering.

✔ Respect rate limits.

✔ Avoid disrupting production systems.

✔ Document all activities.

✔ Follow responsible disclosure policies.

---

## Data Protection

Encrypt reconnaissance results.

```bash
gpg --symmetric \
--cipher-algo AES256 \
recon_results.json
```

Restrict permissions.

```bash
chmod 600 *.txt

chmod 600 *.csv

chmod 600 *.json
```

Remove temporary files.

```bash
find . -name "*.tmp" -delete
```

---

## Legal Considerations

Always ensure that:

- Reconnaissance complies with applicable laws.
- Third-party testing has written authorization.
- Organizational security policies are followed.
- Dedicated testing environments are used whenever possible.

---

# 🔹 Expected Outcomes

After completing this lab, you should have:

✅ Installed and configured Amass

✅ Installed Commonspeak2 wordlists

✅ Automated cloud asset discovery

✅ Created Python reconnaissance tools

✅ Generated CSV reports

✅ Generated JSON reports

✅ Generated Markdown reports

✅ Built a reusable reconnaissance pipeline

---

# 🔹 Skills Developed

This lab provides practical experience in:

- Automated reconnaissance
- Asset discovery
- Cloud enumeration
- Python automation
- DNS reconnaissance
- Results processing
- Report generation
- Security workflow automation

---

# 🔹 Key Takeaways

- Automation significantly accelerates reconnaissance activities.

- Combining multiple intelligence sources increases discovery coverage.

- Structured reporting improves collaboration and future assessments.

- Python is an excellent language for reconnaissance automation.

- Reconnaissance should always be conducted ethically and legally.

---

# 🔹 Next Steps

Continue building your reconnaissance capabilities by exploring:

- OWASP Amass advanced configuration

- Subfinder

- Assetfinder

- Nuclei

- HTTPX

- DNSX

- Katana

- Naabu

- D3.js visualizations

- Plotly dashboards

Practice these techniques in authorized environments such as:

- Hack The Box

- TryHackMe

- PortSwigger Web Security Academy

- VulnHub

---

# 🏁 Conclusion

Congratulations!

In this lab you successfully built a complete automated reconnaissance pipeline using **OWASP Amass**, **Commonspeak2**, and **Python**.

You learned how to:

- Install and configure professional reconnaissance tools
- Discover cloud assets through automated enumeration
- Process reconnaissance data into structured formats
- Generate professional reports in CSV, JSON, Markdown, and HTML
- Build an end-to-end automated workflow for future cloud security assessments

These skills form a strong foundation for cloud penetration testing, adversary simulation, red teaming, and preparation for the **Al Razzaq Certified Cloud Adversary Simulation Expert (CCASE)** certification.

---

# 🎉 Lab Complete

**Congratulations! You have successfully completed the _Automate Recon with Amass + Commonspeak2_ lab.**
