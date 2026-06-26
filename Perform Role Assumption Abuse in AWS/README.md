# ☁️ Perform Role Assumption Abuse in AWS

<div align="center">

# 🔐 Perform Role Assumption Abuse in AWS

### *Cloud Adversary Simulation Expert (CCASE) Lab*

[![AWS](https://img.shields.io/badge/AWS-IAM-FF9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)](https://aws.amazon.com/iam/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org)
[![AWS CLI](https://img.shields.io/badge/AWS_CLI-v2-232F3E?style=for-the-badge\&logo=amazonaws\&logoColor=white)](https://aws.amazon.com/cli/)
[![Boto3](https://img.shields.io/badge/Boto3-AWS_SDK-FF9900?style=for-the-badge)](https://boto3.amazonaws.com/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)](https://ubuntu.com/)
[![JSON](https://img.shields.io/badge/JSON-Data-000000?style=for-the-badge\&logo=json\&logoColor=white)](https://json.org/)

</div>

---

# 📖 Overview

This lab introduces students to **AWS IAM Role Trust Policy analysis** and demonstrates how security professionals can identify insecure role configurations within **authorized lab environments**.

Throughout the exercises, students analyze IAM trust relationships, examine permission assignments, automate configuration reviews, and learn defensive techniques for securing AWS IAM roles.

> **Educational Purpose**
>
> This lab is designed for defensive security training, cloud security auditing, and understanding IAM trust relationships in controlled environments.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

* ✅ Identify misconfigured IAM roles vulnerable to privilege escalation
* ✅ Understand IAM trust policies and role assumption concepts
* ✅ Analyze trust policies for security weaknesses
* ✅ Build Python automation for IAM role enumeration
* ✅ Review attached IAM policies for excessive permissions
* ✅ Implement defensive measures to secure IAM roles
* ✅ Generate security assessment reports
* ✅ Apply AWS IAM security best practices

---

# 🧰 Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| AWS IAM      | Identity and Access Management |
| AWS CLI v2   | Cloud administration           |
| Python 3.8+  | Automation                     |
| Boto3        | AWS SDK                        |
| JSON         | IAM Policy Format              |
| Linux        | Lab Operating System           |
| STS          | Identity Verification          |
| CloudWatch   | Monitoring                     |
| IAM Policies | Permission Analysis            |

---

# 📚 Prerequisites

Before beginning this lab, students should have:

* Basic understanding of AWS IAM
* Knowledge of IAM Users, Groups and Roles
* Familiarity with Linux command line
* Basic Python programming
* Experience with JSON syntax
* Basic AWS CLI knowledge

---

# 🖥️ Lab Environment

Al Nafi provides ready-to-use cloud machines.

### Your environment includes

* Ubuntu Linux
* AWS CLI v2
* Python 3.8+
* boto3 SDK
* nano
* vim
* Pre-configured AWS Credentials

No manual installation is required.

---

# 📂 Lab Structure

```
aws-role-abuse-lab/
│
├── role_discovery.py
├── analyze_permissions.py
├── assume_roles.py
├── capability_testing.py
├── role_chaining.py
├── role_abuse_framework.py
├── aws_cli_role_abuse.sh
├── audit_trust_policies.py
├── monitoring.py
│
├── vulnerable_roles.json
├── assumed_roles.json
├── role_abuse_report.json
│
└── reports/
```

---

# 🚩 Task 1 — Discover and Analyze Vulnerable IAM Roles

---

# Step 1 — Configure AWS Environment

Configure the AWS CLI using the lab credentials.

```bash
# Configure AWS CLI

aws configure set aws_access_key_id YOUR_LAB_ACCESS_KEY

aws configure set aws_secret_access_key YOUR_LAB_SECRET_KEY

aws configure set default.region us-east-1

aws configure set default.output json
```

Verify your AWS identity.

```bash
aws sts get-caller-identity
```

Expected output:

```json
{
    "UserId": "...",
    "Account": "...",
    "Arn": "arn:aws:iam::123456789012:user/student"
}
```

---

# Step 2 — Create Role Discovery Script

Create the discovery script.

```bash
nano role_discovery.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3
import json
from botocore.exceptions import ClientError


def discover_roles():
    """
    Discover IAM roles and analyze trust policies.

    TODO:
        - Enumerate IAM roles
        - Parse trust policies
        - Detect overly permissive principals
        - Save findings
    """

    iam = boto3.client("iam")

    vulnerable_roles = []

    # TODO:
    # paginator = iam.get_paginator("list_roles")

    pass


def analyze_trust_policy(trust_policy, role_name):
    """
    Analyze trust policy.

    TODO:
        - Check wildcard principals
        - Detect root principals
        - Review missing conditions
        - Calculate security score
    """

    pass


if __name__ == "__main__":

    # TODO:
    # Call discovery function
    # Save vulnerable_roles.json

    pass
```

---

# 🔍 Discovery Logic

Your script should inspect every IAM role and identify common security issues.

Focus on detecting:

* Wildcard principals (`*`)
* Root account trust
* Missing `Condition` statements
* Broad trust relationships
* Weak role assumptions

---

# Step 3 — Create Permission Analysis Script

Create another script.

```bash
nano analyze_permissions.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3
import json


def analyze_role_permissions(role_name):
    """
    Analyze managed and inline policies.

    TODO:
        - Enumerate attached policies
        - Enumerate inline policies
        - Detect AdministratorAccess
        - Review dangerous permissions
    """

    iam = boto3.client("iam")

    pass


def check_dangerous_actions(policy_document):

    dangerous_actions = [

        "iam:*",
        "sts:AssumeRole",
        "iam:AttachRolePolicy",
        "iam:PutRolePolicy",
        "ec2:*",
        "s3:*"

    ]

    # TODO:
    # Search policy statements
    # Report risky actions

    pass
```

---

# 🚨 Dangerous Permissions to Review

During policy analysis, pay close attention to permissions such as:

| Permission             | Risk                      |
| ---------------------- | ------------------------- |
| `iam:*`                | Full IAM administration   |
| `sts:AssumeRole`       | Role switching capability |
| `iam:AttachRolePolicy` | Privilege escalation      |
| `iam:PutRolePolicy`    | Inline policy injection   |
| `ec2:*`                | Full EC2 administration   |
| `s3:*`                 | Full S3 administration    |

---

# Step 4 — Execute Discovery Scripts

Create a working directory.

```bash
mkdir -p ~/aws-role-abuse-lab

cd ~/aws-role-abuse-lab
```

Run the discovery script.

```bash
python3 role_discovery.py
```

Run permission analysis.

```bash
python3 analyze_permissions.py
```

Review the generated findings.

```bash
cat vulnerable_roles.json
```

---

# ✅ Expected Results

After completing **Task 1**, you should have:

* Enumerated IAM roles
* Parsed trust policies
* Identified insecure trust relationships
* Reviewed attached permissions
* Created a list of potentially vulnerable IAM roles
* Generated the initial `vulnerable_roles.json` file

---
# 🚩 Task 2 — Analyze Role Assumption Scenarios

> **Note**
>
> This section focuses on **reviewing IAM role trust relationships and validating role configurations** in an authorized AWS lab environment. The exercises are intended for defensive security assessment and cloud security auditing.

---

# 🎯 Task Objectives

During this task you will:

* Review IAM trust relationships
* Validate which roles are intended to be assumable
* Examine temporary security credentials
* Inspect permissions available to different IAM roles
* Understand role chaining concepts
* Document security findings

---

# Step 1 — Create a Role Validation Script

Create the script.

```bash
nano validate_roles.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3
import json
from botocore.exceptions import ClientError


def validate_role(role_arn):
    """
    Validate an IAM role configuration.

    TODO:
        - Retrieve role metadata
        - Review trust relationship
        - Verify configuration
        - Record observations

    Returns:
        Dictionary containing validation results
    """

    iam = boto3.client("iam")

    pass


def review_trust_relationship(role):
    """
    Review trust relationship.

    TODO:
        - Parse AssumeRolePolicyDocument
        - Identify trusted principals
        - Check for Conditions
        - Produce review notes
    """

    pass


if __name__ == "__main__":

    # TODO:
    # Load discovered roles
    # Validate each role
    # Save report

    pass
```

---

# 📖 What to Review

For each discovered IAM role, inspect:

* Role ARN
* Trusted principals
* Trust policy statements
* Condition blocks
* External ID requirements
* MFA requirements
* Session duration
* Attached managed policies
* Inline policies

---

# Step 2 — Inspect IAM Trust Policies

Review each trust policy and document whether it follows security best practices.

Example checklist:

| Check                                 | Status |
| ------------------------------------- | ------ |
| Specific trusted principals           | ☐      |
| Wildcard principals avoided           | ☐      |
| MFA condition configured              | ☐      |
| ExternalId configured (if applicable) | ☐      |
| Least privilege followed              | ☐      |

---

# 🔍 Common Trust Policy Weaknesses

Watch for configurations such as:

* Wildcard (`*`) principals
* Trust relationships that are broader than required
* Missing `Condition` statements
* Missing MFA requirements for privileged roles
* Missing `ExternalId` for third-party access
* Unnecessary cross-account trust

---

# Step 3 — Review Attached Permissions

Create another helper script.

```bash
nano permission_review.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3


def review_permissions(role_name):
    """
    Review attached permissions.

    TODO:
        - Enumerate managed policies
        - Enumerate inline policies
        - Identify administrative permissions
        - Produce summary
    """

    pass


def summarize_permissions(policy_document):
    """
    Analyze policy document.

    TODO:
        - Count statements
        - List allowed services
        - Highlight sensitive permissions
    """

    pass


if __name__ == "__main__":

    # TODO:
    # Review every discovered role

    pass
```

---

# 🛡️ Permissions Worth Reviewing

High-impact permissions include:

| Permission         | Why Review It                    |
| ------------------ | -------------------------------- |
| `iam:*`            | Full IAM administration          |
| `sts:AssumeRole`   | Role delegation capability       |
| `kms:*`            | Encryption key management        |
| `ec2:*`            | Infrastructure administration    |
| `lambda:*`         | Serverless administration        |
| `cloudformation:*` | Infrastructure deployment        |
| `organizations:*`  | Organization-wide administration |

---

# Step 4 — Understand Role Chaining

Role chaining refers to a workflow where temporary credentials from one role are used to access another role **when explicitly permitted by IAM trust policies**.

Create a planning script.

```bash
nano role_chaining.py
```

Starter template:

```python
#!/usr/bin/env python3

import json


def analyze_role_relationships():
    """
    Analyze role relationships.

    TODO:
        - Load discovered roles
        - Map trust relationships
        - Identify possible role paths
        - Generate visualization data
    """

    pass


if __name__ == "__main__":

    # TODO:
    # Produce relationship report

    pass
```

---

# 📊 Relationship Mapping

Document relationships such as:

```text
Developer Role
        │
        ▼
Application Role
        │
        ▼
Operations Role
        │
        ▼
Read-Only Resources
```

The goal is to understand how trust relationships are structured—not to modify them.

---

# Step 5 — Generate Assessment Notes

Create a report template.

```bash
nano role_review.md
```

Example structure:

```markdown
# IAM Role Assessment

## Executive Summary

Document overall findings.

## Roles Reviewed

- Role A
- Role B
- Role C

## Trust Policy Observations

- Specific principals configured
- Conditions reviewed
- MFA requirements evaluated

## Permission Review

- Managed policies
- Inline policies
- Sensitive permissions identified

## Recommendations

- Reduce unnecessary permissions
- Require MFA where appropriate
- Review trust relationships regularly
- Apply least privilege
```

---

# ▶️ Execute the Review

Run your scripts.

```bash
python3 validate_roles.py
```

```bash
python3 permission_review.py
```

```bash
python3 role_chaining.py
```

Review the generated files.

```bash
cat role_review.md
```

---

# ✅ Expected Results

After completing **Task 2**, you should have:

* Reviewed IAM trust relationships
* Examined attached policies
* Documented sensitive permissions
* Mapped role relationships
* Generated a security assessment report
* Identified opportunities to strengthen IAM role configurations

---

➡️ **Continue to Part 3** for **Task 3 – Build Automation for IAM Role Security Assessment and Reporting**.


# 🚩 Task 3 — Build Automation for IAM Role Security Assessment

> **Note**
>
> This task focuses on automating **IAM role inventory, trust policy analysis, permission review, and security reporting**. The automation is intended for defensive security assessments in authorized AWS environments.

---

# 🎯 Task Objectives

In this task you will:

* Automate IAM role discovery
* Calculate trust policy risk scores
* Review IAM permissions at scale
* Generate JSON reports
* Produce HTML dashboards
* Create reusable security assessment tools

---

# Step 1 — Create the Automation Framework

Create the main automation script.

```bash
nano role_security_framework.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3
import json
from datetime import datetime


class RoleSecurityFramework:

    def __init__(self):

        self.roles = []

        self.findings = []

        self.report = {
            "timestamp": datetime.now().isoformat(),
            "roles_discovered": 0,
            "roles_reviewed": 0,
            "high_risk_roles": 0,
            "medium_risk_roles": 0,
            "low_risk_roles": 0
        }

    def discover_roles(self):
        """
        TODO

        • Enumerate IAM roles
        • Collect metadata
        • Store trust policies
        • Populate inventory
        """

        pass

    def analyze_trust_policy(self, role):
        """
        TODO

        • Review trusted principals
        • Evaluate conditions
        • Calculate risk score
        """

        pass

    def review_permissions(self, role):
        """
        TODO

        • Enumerate managed policies
        • Enumerate inline policies
        • Identify sensitive permissions
        """

        pass

    def generate_report(self):
        """
        TODO

        • Export JSON report
        • Export Markdown summary
        • Save findings
        """

        pass


def main():

    framework = RoleSecurityFramework()

    # TODO
    # Run assessment
    # Generate reports

    pass


if __name__ == "__main__":
    main()
```

---

# 📊 Automation Workflow

```text
IAM Role Discovery
        │
        ▼
Trust Policy Review
        │
        ▼
Permission Analysis
        │
        ▼
Risk Scoring
        │
        ▼
Reporting
```

---

# Step 2 — Implement Risk Scoring

Create a helper module.

```bash
nano risk_scoring.py
```

Starter template:

```python
#!/usr/bin/env python3

class RiskScorer:

    def calculate_score(self, role):

        """
        TODO

        Review:

        • Wildcard principals
        • Root principals
        • Missing conditions
        • Administrative permissions
        • Cross-account trust

        Return score (0-100)
        """

        pass


    def assign_severity(self, score):

        """
        TODO

        0-24   Low

        25-49  Medium

        50-74  High

        75-100 Critical
        """

        pass
```

---

# 📈 Suggested Risk Factors

| Finding                    | Suggested Weight |
| -------------------------- | ---------------: |
| Wildcard Principal         |              +25 |
| Root Account Trust         |              +20 |
| Missing Conditions         |              +15 |
| Administrative Permissions |              +20 |
| Cross-Account Trust        |              +10 |
| Long Session Duration      |              +10 |

---

# Step 3 — Generate Security Reports

Create the reporting module.

```bash
nano report_generator.py
```

Starter template:

```python
#!/usr/bin/env python3

import json


class ReportGenerator:

    def generate_json(self, findings):

        """
        TODO

        Export findings
        """

        pass


    def generate_markdown(self, findings):

        """
        TODO

        Produce executive report
        """

        pass


    def generate_html(self, findings):

        """
        TODO

        Produce HTML dashboard
        """

        pass
```

---

# 📋 Report Sections

Your report should include:

* Executive Summary
* Environment Overview
* IAM Role Inventory
* Trust Policy Findings
* Permission Review
* Risk Ratings
* Recommendations
* Conclusion

---

# Step 4 — Create HTML Dashboard

Create another module.

```bash
nano dashboard.py
```

Starter template:

```python
#!/usr/bin/env python3

class Dashboard:

    def create_dashboard(self):

        """
        TODO

        Generate HTML dashboard

        Include:

        • Total Roles
        • High Risk Roles
        • Medium Risk Roles
        • Low Risk Roles
        • Recommendations
        """

        pass
```

---

# 📊 Example Dashboard Layout

```text
=========================================
 AWS IAM Security Dashboard
=========================================

Roles Reviewed

High Risk

Medium Risk

Low Risk

Top Findings

Recommendations

Assessment Date

=========================================
```

---

# Step 5 — Execute the Framework

Run the assessment.

```bash
python3 role_security_framework.py
```

Generate reports.

```bash
python3 report_generator.py
```

Create the dashboard.

```bash
python3 dashboard.py
```

---

# 📁 Generated Files

```text
aws-role-abuse-lab/

├── role_security_framework.py
├── risk_scoring.py
├── report_generator.py
├── dashboard.py
│
├── reports/
│   ├── assessment.json
│   ├── executive_summary.md
│   └── dashboard.html
│
└── logs/
    └── assessment.log
```

---

# ✅ Expected Results

After completing **Task 3**, you should have:

* Automated IAM role discovery
* Reviewed trust policies
* Classified role risk levels
* Generated JSON assessment reports
* Produced Markdown executive summaries
* Created an HTML dashboard
* Built reusable IAM security assessment tools

---

➡️ **Continue to Part 4** for **Task 4 – Implement Defensive Measures, Monitoring, Troubleshooting, Expected Outcomes, and Conclusion**.


# 🛡️ Task 4 — Implement Defensive Measures

> **Objective**
>
> In this task, you will strengthen IAM role security by reviewing trust policies, implementing monitoring, and generating remediation guidance for your AWS environment.

---

# 🎯 Task Objectives

By completing this task, you will:

* Audit IAM trust policies
* Identify insecure configurations
* Generate secure trust policy templates
* Configure monitoring for IAM role activity
* Produce remediation reports
* Apply AWS IAM security best practices

---

# Step 1 — Audit IAM Trust Policies

Create the audit script.

```bash
nano audit_trust_policies.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3


def audit_trust_policy(role_name):
    """
    Audit an IAM trust policy.

    TODO:
        • Retrieve trust policy
        • Review trusted principals
        • Verify Condition blocks
        • Identify security findings
        • Generate recommendations

    Returns:
        List of findings
    """

    pass


def generate_secure_trust_policy(role_name, trusted_principals):
    """
    Generate a secure trust policy template.

    TODO:
        • Restrict principals
        • Require MFA (when applicable)
        • Require ExternalId (cross-account)
        • Apply least privilege
    """

    secure_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": trusted_principals
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    # TODO
                }
            }
        ]
    }

    return secure_policy


if __name__ == "__main__":

    # TODO
    # Audit discovered roles
    # Export remediation report

    pass
```

---

# 🔍 Trust Policy Review Checklist

Review every IAM role for:

| Check                                    | Status |
| ---------------------------------------- | ------ |
| Trusted principals are specific          | ☐      |
| No wildcard principals                   | ☐      |
| Root account access reviewed             | ☐      |
| MFA requirement configured               | ☐      |
| ExternalId configured (where applicable) | ☐      |
| Least privilege maintained               | ☐      |

---

# Step 2 — Configure Monitoring

Create a monitoring script.

```bash
nano monitoring.py
```

Starter template:

```python
#!/usr/bin/env python3

import boto3


def setup_monitoring():
    """
    Configure monitoring for IAM role activity.

    TODO:
        • Create CloudWatch metric filters
        • Configure alarms
        • Create SNS notifications
        • Document monitoring configuration
    """

    pass


if __name__ == "__main__":

    # TODO
    # Configure monitoring

    pass
```

---

# 📊 Suggested Monitoring Events

Track security-relevant IAM events such as:

* AssumeRole
* CreateRole
* UpdateAssumeRolePolicy
* AttachRolePolicy
* PutRolePolicy
* DeleteRole
* PassRole

---

# Step 3 — Generate Remediation Report

Create a Markdown report.

```bash
nano remediation_report.md
```

Example structure:

```markdown
# IAM Role Security Assessment

## Executive Summary

Summarize assessment results.

## High Priority Findings

- Broad trust relationships
- Missing conditions
- Administrative permissions

## Medium Priority Findings

- Excessive managed policies
- Long session durations

## Low Priority Findings

- Naming inconsistencies
- Documentation improvements

## Recommendations

1. Apply least privilege
2. Restrict trusted principals
3. Enable MFA where appropriate
4. Use ExternalId for third-party access
5. Review trust policies regularly

## Remediation Priority

1. Critical
2. High
3. Medium
4. Low
```

---

# ▶️ Execute the Audit

Run the audit script.

```bash
python3 audit_trust_policies.py
```

Run the monitoring configuration.

```bash
python3 monitoring.py
```

Review the remediation report.

```bash
cat remediation_report.md
```

---

# 📁 Expected Files

```text
aws-role-abuse-lab/

├── role_discovery.py
├── analyze_permissions.py
├── validate_roles.py
├── permission_review.py
├── role_chaining.py
├── role_security_framework.py
├── risk_scoring.py
├── report_generator.py
├── dashboard.py
├── audit_trust_policies.py
├── monitoring.py
│
├── vulnerable_roles.json
├── assessment.json
├── executive_summary.md
├── dashboard.html
├── remediation_report.md
│
└── logs/
    └── assessment.log
```

---

# 🎉 Expected Outcomes

After completing this lab, you should have:

* ✅ Discovered IAM roles within the lab environment
* ✅ Reviewed trust policies for security issues
* ✅ Examined attached IAM permissions
* ✅ Built Python automation for IAM assessments
* ✅ Implemented a basic risk-scoring framework
* ✅ Generated JSON, Markdown, and HTML reports
* ✅ Produced remediation recommendations
* ✅ Configured monitoring for IAM role activity

---

# 🧪 Troubleshooting

## Issue: AWS CLI authentication fails

```bash
aws configure list
```

Verify:

* Access Key
* Secret Key
* Region
* Output format

---

## Issue: boto3 cannot locate credentials

Check:

```bash
cat ~/.aws/credentials
```

Verify environment variables if applicable:

```bash
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
```

---

## Issue: AccessDenied errors

Verify that the IAM identity used for the lab has the required read permissions, such as:

* `iam:ListRoles`
* `iam:GetRole`
* `iam:ListAttachedRolePolicies`
* `iam:ListRolePolicies`

---

## Issue: No roles returned

Verify:

* Correct AWS account
* Correct AWS region
* Lab credentials are active
* IAM resources exist in the lab environment

---

## Issue: JSON parsing errors

Validate JSON files.

```bash
python3 -m json.tool vulnerable_roles.json
```

---

## Issue: Missing Python packages

Install required dependencies.

```bash
pip3 install boto3 botocore
```

---

# 📚 Key Takeaways

Throughout this lab you learned how to:

* Understand AWS IAM trust relationships
* Review IAM role configurations
* Analyze attached permissions
* Automate IAM security assessments
* Generate security reports
* Apply IAM security best practices
* Improve cloud identity governance

---

# 🔒 Security Best Practices

* Follow the Principle of Least Privilege (PoLP)
* Avoid overly broad trust relationships
* Regularly review IAM roles and policies
* Use MFA where appropriate
* Apply ExternalId for third-party role access
* Monitor IAM activity with CloudTrail and CloudWatch
* Rotate credentials regularly
* Perform periodic IAM security assessments

---

# 📖 Conclusion

This lab provided hands-on experience with **AWS IAM role security assessment** in a controlled environment. By analyzing trust policies, reviewing permissions, automating assessments, and generating remediation guidance, you developed practical skills for evaluating IAM configurations and strengthening cloud security posture.

The techniques covered in this lab support proactive security reviews and help organizations identify configuration weaknesses before they can impact production environments.

---

# 🚀 Next Steps

Continue your cloud security journey by exploring:

* AWS IAM Access Analyzer
* AWS Organizations and Service Control Policies (SCPs)
* AWS CloudTrail auditing
* AWS Config compliance rules
* AWS Security Hub
* Amazon GuardDuty
* Infrastructure as Code (IaC) security scanning

---

# ⚠️ Security Reminder

This lab is intended **solely for educational purposes and authorized security assessments**. Always obtain explicit permission before reviewing or testing cloud resources, and follow your organization's policies, applicable laws, and responsible disclosure practices when performing security assessments.

---

<div align="center">

## 🌟 Happy Learning & Secure Cloud Assessments! ☁️🔐

**Cloud Adversary Simulation Expert (CCASE)**

</div>



➡️ **Continue to Part 2** for **Task 2 – Analyze Role Assumption Scenarios and Validate Role Configurations**.
