# 🔐 Abuse Azure SSO via Misconfigured OAuth Flows 

## 🎯 Objectives

By the end of this lab, students will be able to:

- Enumerate :contentReference[oaicite:0]{index=0} SSO configurations and identify OAuth misconfigurations  
- Exploit OAuth 2.0 flow weaknesses such as redirect URI validation bypass  
- Intercept and manipulate authorization codes for unauthorized access  
- Automate OAuth exploitation workflows using Python scripts  
- Implement defensive controls to mitigate OAuth-based attacks  

---

## 📚 Prerequisites

- Basic understanding of :contentReference[oaicite:1]{index=1} and :contentReference[oaicite:2]{index=2}  
- Familiarity with Azure Active Directory concepts  
- Python programming fundamentals  
- Understanding of HTTP requests and REST APIs  

---

## 🧪 Lab Environment Setup

Al Nafi provides pre-configured Linux cloud machines.

### 🖥️ Included Tools
- Python 3.x with `requests`
- curl & wget
- nano / vim editors
- Network utilities
- Web browser access

---

# 🧭 Task 1: Enumerate Azure OAuth Configuration

## Step 1: Create Working Directory

```bash
mkdir ~/azure-oauth-lab
cd ~/azure-oauth-lab

Create configuration file:

cat > config.env << EOF
TENANT_ID=common
CLIENT_ID=your-client-id-here
REDIRECT_URI=http://localhost:8080/callback
SCOPE=openid profile email
EOF
Step 2: OAuth Discovery Script

Create oauth_enum.py:

#!/usr/bin/env python3

import requests
import json
import sys

class OAuthEnumerator:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.base_url = f"https://login.microsoftonline.com/{tenant_id}"

    def discover_endpoints(self):
        """
        Discover OAuth endpoints using OpenID configuration
        """
        discovery_url = f"{self.base_url}/.well-known/openid-configuration"

        # TODO: Fetch and parse configuration
        pass

    def test_redirect_validation(self, client_id):
        """
        Test redirect URI validation weaknesses
        """
        test_redirects = [
            "http://localhost:8080/callback",
            "https://evil.com/callback"
        ]

        # TODO: Implement validation testing
        pass

    def enumerate_scopes(self, client_id):
        """
        Enumerate available OAuth scopes
        """
        common_scopes = [
            "openid", "profile", "email",
            "User.Read", "Mail.Read"
        ]

        # TODO: Implement scope testing
        pass


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 oauth_enum.py <tenant_id> <client_id>")
        sys.exit(1)

    tenant_id = sys.argv[1]
    client_id = sys.argv[2]

    # TODO: Run enumeration
    pass


if __name__ == "__main__":
    main()

Run:

chmod +x oauth_enum.py
source config.env
python3 oauth_enum.py $TENANT_ID $CLIENT_ID
🧭 Task 2: Exploit OAuth Authorization Code Flow
Step 1: Code Interceptor Server

Create code_interceptor.py:

#!/usr/bin/env python3

import http.server
import urllib.parse

class AuthCodeHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        # TODO:
        # - Extract authorization code
        # - Save to file
        # - Respond to browser
        pass

    def log_message(self, format, *args):
        pass
Step 2: Token Exchange Script

Create token_exchange.py:

#!/usr/bin/env python3

import requests
import base64

class TokenExchanger:

    def exchange_code(self, auth_code, redirect_uri):
        """
        Exchange authorization code for access token
        """
        # TODO: POST request to token endpoint
        pass

    def decode_jwt(self, token):
        """
        Decode JWT claims
        """
        # TODO: decode header + payload
        pass

    def test_token(self, access_token):
        """
        Test token against Microsoft Graph API
        """
        endpoints = [
            "https://graph.microsoft.com/v1.0/me"
        ]

        # TODO: validate token
        pass
Related API Target

Microsoft Graph API

🧭 Task 3: Automate OAuth Exploitation
Automation Framework

Create oauth_exploit_automation.py:

class OAuthExploitFramework:

    def run_full_enumeration(self):
        # TODO: discover endpoints + scopes
        pass

    def generate_phishing_campaign(self, scopes):
        # TODO: generate auth URLs
        pass

    def automated_token_theft(self):
        # TODO: intercept + exchange flow
        pass

    def generate_report(self):
        # TODO: produce JSON/HTML report
        pass
🪟 PowerShell Alternative (Windows)
param(
    [string]$TenantId,
    [string]$ClientId
)

function Discover-OAuthConfig {
    # TODO: fetch OpenID configuration
}

function Test-RedirectValidation {
    # TODO: test redirect URI handling
}

function Invoke-TokenExchange {
    # TODO: exchange code for token
}
🧭 Task 4: Defensive Measures
OAuth Security Validator
class OAuthSecurityValidator:

    def validate_redirect_uris(self):
        # TODO:
        # - No wildcards
        # - HTTPS enforcement
        pass

    def validate_scope_configuration(self):
        # TODO:
        # - Least privilege validation
        pass

    def validate_token_handling(self):
        # TODO:
        # - Expiry checks
        # - Secure storage
        pass
🔐 Security Checklist
# Azure OAuth Security Checklist

## Redirect URI Security
- Exact match only (no wildcards)
- HTTPS enforced in production
- Validate server-side

## Scope Control
- Least privilege principle
- Avoid over-permissioned apps
- Regular audits

## Token Security
- Short-lived tokens
- Refresh token rotation
- Encrypted storage

## Monitoring
- Enable sign-in logs
- Detect suspicious consent
- Monitor redirect anomalies
🧪 Expected Outcomes

After completing this lab, students will:

Understand OAuth 2.0 authorization flow internals
Identify misconfigured redirect URIs
Intercept authorization codes
Exchange codes for access tokens
Analyze token payloads (JWT structure)
Implement security validation mechanisms
⚠️ Troubleshooting
❌ Redirect not working
Ensure redirect URI matches exactly
Check port availability (8080)
❌ Token exchange failure
Authorization code expired
Redirect URI mismatch
❌ Graph API failure
Missing permissions/scopes
Invalid or expired token
🧠 Conclusion

This lab demonstrated how misconfigurations in Azure Active Directory OAuth implementations can lead to serious authentication bypass scenarios.

You learned:

OAuth endpoint enumeration
Authorization code interception
Token exchange mechanisms
Security validation strategies
🔒 Key Takeaways
OAuth security depends heavily on correct redirect URI validation
Authorization codes must be protected during transmission
Least privilege scope design is critical
Monitoring and conditional access reduce attack risk
🚨 Ethical Reminder

These techniques are intended for authorized security testing only. Unauthorized access to systems or accounts is illegal and unethical.
