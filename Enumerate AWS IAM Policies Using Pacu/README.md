# ☁️ Enumerate AWS IAM Policies Using Pacu (Lab Guide)

## 🎯 Objectives

By the end of this lab, students will be able to:

- Install and configure the :contentReference[oaicite:0]{index=0} framework for AWS security testing  
- Perform IAM policy enumeration using Pacu modules  
- Identify privilege escalation paths and IAM misconfigurations  
- Automate enumeration tasks using Python scripts  
- Generate structured cloud security assessment reports  

---

## 📚 Prerequisites

- Basic understanding of :contentReference[oaicite:1]{index=1} IAM concepts (users, roles, policies)  
- Familiarity with Linux command line  
- Basic Python programming knowledge  
- Understanding of JSON format  
- AWS CLI fundamentals  

---

## 🧪 Lab Environment

Al Nafi provides pre-configured Linux cloud machines.

### 🖥️ Included Tools
- Ubuntu 20.04 LTS  
- Python 3.8+  
- Git + text editors  
- Pre-installed dependencies  

---

# 🧭 Task 1: Install and Configure Pacu

## Step 1: Install Pacu

```bash
sudo apt update && sudo apt install -y python3 python3-pip git

cd /home/ubuntu
git clone https://github.com/RhinoSecurityLabs/pacu.git
cd pacu

pip3 install -r requirements.txt
Step 2: Initialize Pacu Session
python3 pacu.py

Create session:

Session name: iam-enum-lab
Step 3: Configure Test Credentials
mkdir -p ~/.aws
cat > ~/.aws/credentials << 'EOF'
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
region = us-east-1
EOF
🧭 Task 2: IAM Enumeration Using Pacu
Step 1: Load Credentials

Inside Pacu:

import_keys --profile default
whoami
Step 2: Run IAM Enumeration
list iam
run iam__enum_users_roles_policies_groups
data IAM
Step 3: Permission & Privilege Analysis
run iam__enum_permissions
run iam__enum_attached_policies
run iam__privesc_scan
🧭 Task 3: IAM Policy Analysis Script

Create:

nano analyze_policies.py
#!/usr/bin/env python3

import json
import sqlite3

class IAMPolicyAnalyzer:
    def __init__(self, db_path):
        self.db_path = db_path
        self.dangerous_actions = [
            "iam:CreateRole",
            "iam:AttachRolePolicy",
            "iam:PutRolePolicy",
            "sts:AssumeRole",
            "iam:*",
            "*"
        ]

    def connect_db(self):
        # TODO: connect to Pacu SQLite DB
        pass

    def analyze_policies(self):
        # TODO: query IAM tables
        pass

    def check_dangerous_permissions(self, policy_document):
        # TODO: detect risky permissions
        pass

    def generate_report(self, output_file):
        # TODO: generate report
        pass
🧠 Policy Review Script
#!/usr/bin/env python3

class PolicyReviewer:

    def check_wildcard_permissions(self, policy_doc):
        # TODO: detect "*" permissions
        pass

    def check_privilege_escalation(self, policy_doc):
        escalation_actions = [
            "iam:CreateRole",
            "iam:AttachRolePolicy",
            "iam:PutRolePolicy",
            "iam:CreateUser",
            "sts:AssumeRole"
        ]
        # TODO: analyze escalation risk
        pass

    def check_cross_account_access(self, policy_doc):
        # TODO: detect external trust relationships
        pass
📄 Task 4: IAM Findings Report
# IAM Policy Enumeration Report

## 🧾 Summary
IAM enumeration completed using Pacu framework.

## 🔴 High Risk Issues
- Wildcard permissions (*)
- Overprivileged roles
- Missing MFA enforcement
- Cross-account trust misconfigurations

## 🟠 Medium Risk Issues
- Excessive IAM permissions
- Unused roles/users
- Broad policy attachments

## 🟢 Low Risk Issues
- Naming inconsistencies
- Missing tagging standards

## 🛠 Recommendations
- Enforce least privilege
- Enable MFA everywhere
- Use AWS Config rules
- Enable CloudTrail monitoring
⚙️ Task 5: Automation Framework
#!/usr/bin/env python3

import subprocess
import json

class PacuAutomation:

    def run_pacu_module(self, module_name):
        # TODO: execute pacu module
        pass

    def enumerate_iam_resources(self):
        modules = [
            "iam__enum_users_roles_policies_groups",
            "iam__enum_permissions",
            "iam__privesc_scan"
        ]
        # TODO: run modules sequentially
        pass

    def generate_report(self, results, output_path):
        # TODO: export results
        pass
📊 Task 6: Monitoring Script
class EnumerationMonitor:

    def monitor_database(self):
        # TODO: inspect pacu.db
        pass

    def log_activity(self, activity_type, details):
        # TODO: write logs
        pass

    def create_timeline(self, output_path):
        # TODO: build HTML timeline
        pass
🚀 Execution Commands
chmod +x analyze_policies.py policy_review.py automated_iam_enum.py enum_monitor.py

python3 analyze_policies.py
python3 policy_review.py
python3 automated_iam_enum.py
python3 enum_monitor.py
📦 Expected Outputs

After completing the lab:

IAM users, roles, and policies enumerated
Privilege escalation paths identified
Risk-based policy analysis generated
Automated Pacu enumeration scripts created
Security reports documented
📄 Generated Files
iam_analysis_report.txt
iam_findings.md
iam_dashboard.html
enum_activity.log
pacu_automation.log
⚠️ Troubleshooting
❌ Pacu fails to install
pip3 install --upgrade pip
pip3 install -r requirements.txt --user
❌ Database errors
chmod 644 /home/ubuntu/pacu/pacu.db
❌ No IAM data
Re-run import_keys
Verify credentials
🧠 Conclusion

This lab demonstrated how IAM misconfigurations in Amazon Identity and Access Management can be discovered using the Pacu framework.

🔑 Key Takeaways
IAM misconfigurations enable privilege escalation
Pacu automates AWS security enumeration
Wildcard permissions are high-risk indicators
Continuous IAM auditing is essential
🚨 Ethical Reminder

Use these techniques only in authorized AWS environments. Unauthorized access or scanning of cloud systems is illegal and unethical.
