# 🔐 Harvest and Reuse Service Credentials

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- Extract API keys and credentials from development tool configurations  
- Understand common credential exposure patterns in development environments  
- Test harvested credentials against target systems  
- Recognize security vulnerabilities in credential management  
- Implement basic defensive measures against credential harvesting  

---

## 📌 Prerequisites

- Basic Linux command line proficiency  
- Understanding of HTTP requests and APIs  
- Elementary Python programming skills  
- Familiarity with JSON format  
- Basic cybersecurity awareness  

---

## 🧪 Lab Environment

Your cloud machine includes:

- Python 3  
- curl  
- Text editors (nano, vim)  

The environment simulates a real development setup with exposed credentials in configuration files.

---

# ⚙️ Task 1: Discover and Extract Credentials from Configuration Files

---

## 🗂 Step 1: Create Simulated Development Environment

```bash
mkdir -p ~/credential-lab/{postman,vscode,extracted}
cd ~/credential-lab
📦 Postman Configuration (Exposed Secrets)
cat > postman/api-collection.json << 'EOF'
{
  "info": {"name": "API Collection"},
  "item": [{
    "name": "Get Users",
    "request": {
      "header": [
        {"key": "X-API-Key", "value": "sk-prod-abc123def456ghi789"},
        {"key": "Authorization", "value": "Bearer prod-token-xyz789"}
      ],
      "url": "https://api.example.com/users"
    }
  }],
  "variable": [
    {"key": "aws_key", "value": "AKIAIOSFODNN7EXAMPLE"},
    {"key": "stripe_key", "value": "sk_live_51234567890abcdef"}
  ]
}
EOF
💻 VSCode Environment Variables (Leaked Secrets)
cat > vscode/settings.json << 'EOF'
{
  "terminal.integrated.env.linux": {
    "API_KEY": "prod-api-key-abc123",
    "DATABASE_URL": "postgresql://user:SecretPass@server.com:5432/db",
    "GITHUB_TOKEN": "ghp_1234567890abcdefghijklmnop"
  }
}
EOF
🔎 Step 2: Manual Credential Discovery
# Search for API keys, tokens, secrets
grep -ri "api.*key\|token\|secret" postman/ vscode/

# Extract JSON values
grep -oE '"value":\s*"[^"]+"' postman/api-collection.json

# Find environment variables
grep -A 5 "env" vscode/settings.json
🧠 Step 3: Credential Extraction Script

Create automation script:

nano credential_harvester.py
🐍 Credential Harvester Template
#!/usr/bin/env python3
import json
import re
import os

class CredentialHarvester:
    def __init__(self):
        self.credentials = []
        self.patterns = {
            'api_key': r'(?i)(api[_-]?key)[\s]*[:=][\s]*["\']([^"\']+)["\']',
            'bearer': r'(?i)(bearer|token)[\s]*[:=][\s]*["\']([^"\']+)["\']',
            'aws_key': r'(AKIA[0-9A-Z]{16})',
            'github': r'(ghp_[a-zA-Z0-9]{36})',
            'database': r'((?:postgresql|mongodb)://[^"\s]+)'
        }
    
    def extract_from_file(self, filepath):
        """
        TODO:
        - Read file content
        - Apply regex patterns
        - Store findings in credentials list
        """
        pass
    
    def extract_from_json(self, filepath):
        """
        TODO:
        - Load JSON structure
        - Recursively scan keys/values
        - Match credential patterns
        """
        pass
    
    def scan_directory(self, directory):
        """
        TODO:
        - Walk directory tree
        - Detect .json, .env, .conf files
        - Extract credentials
        """
        pass
    
    def save_results(self, output_file):
        """
        TODO:
        - Save credentials to JSON file
        """
        pass
📊 Expected Result
5–7 credentials extracted from configuration files
🧪 Task 2: Test Harvested Credentials Against API
🌐 Step 1: Mock API Server
#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MockAPIHandler(BaseHTTPRequestHandler):
    VALID_TOKENS = {
        'sk-prod-abc123def456ghi789': 'api_user',
        'prod-token-xyz789': 'prod_user'
    }
    
    def do_GET(self):
        """
        TODO:
        - Read headers (Authorization / X-API-Key)
        - Validate token
        - Return 200 or 401 response
        """
        pass
▶️ Run Server
python3 mock_api_server.py &
sleep 2
🧪 Manual Testing
# No credentials (fail)
curl -s http://localhost:8080/api/users

# Bearer token
curl -s -H "Authorization: Bearer prod-token-xyz789" \
http://localhost:8080/api/users

# API key
curl -s -H "X-API-Key: sk-prod-abc123def456ghi789" \
http://localhost:8080/api/users
🤖 Step 3: Automated Credential Tester
nano credential_tester.py
🐍 Tester Template
#!/usr/bin/env python3
import json
import requests

class CredentialTester:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.successful = []
    
    def load_credentials(self, creds_file):
        """
        TODO:
        - Load JSON credentials
        """
        pass
    
    def test_bearer_token(self, token, endpoint):
        """
        TODO:
        - Send Authorization header request
        """
        pass
    
    def test_api_key(self, api_key, endpoint):
        """
        TODO:
        - Send X-API-Key request
        """
        pass
    
    def test_credential(self, credential):
        """
        TODO:
        - Identify type
        - Test against API
        """
        pass
    
    def run_tests(self, creds_file):
        """
        TODO:
        - Load and test all credentials
        """
        pass
⚔️ Task 3: Automated Attack Chain
🚀 End-to-End Exploitation Script
class AutomatedAttack:
    def __init__(self, target_url):
        self.target_url = target_url
        self.results = {
            'harvested': 0,
            'tested': 0,
            'successful': 0
        }
    
    def phase1_harvest(self, scan_dirs):
        """
        TODO:
        - Run harvester
        - Scan directories
        """
        pass
    
    def phase2_test(self, creds_file):
        """
        TODO:
        - Run tester
        """
        pass
    
    def phase3_exploit(self):
        """
        TODO:
        - Access protected endpoints
        """
        pass
    
    def generate_report(self, output_file):
        """
        TODO:
        - Create JSON report
        """
        pass
▶️ Run Full Attack Chain
python3 automated_attack.py \
--scan postman,vscode \
--target http://localhost:8080
📊 Expected Outcomes

After completing this lab, students will:

Extract 5–7 credentials from config files
Successfully reuse 2–3 valid credentials
Access protected API endpoints
Generate full attack report
Understand credential exposure risks
⚠️ Troubleshooting
❌ Credentials not found
Verify regex patterns
Check file paths
Ensure JSON is valid
❌ API not responding
ps aux | grep mock_api
netstat -tuln | grep 8080
❌ Authentication fails
Confirm token matches server list
Verify header format
Check logs
🧠 Conclusion

This lab demonstrated how insecure configuration management leads to credential leakage and reuse attacks.

🔥 Key Takeaways
Dev tools often expose sensitive secrets
Credentials are reusable across systems
Regex-based harvesting is highly effective
Poor secret management leads to full compromise
🛡️ Security Recommendations
Never store secrets in config files
Use secret managers (Vault, AWS Secrets Manager)
Rotate credentials regularly
Scan repositories for leaked secrets
Block commits with tools like git-secrets
🧹 Cleanup
pkill -f mock_api_server.py
rm -rf ~/credential-lab

⚠️ Educational Notice: This lab is for authorized security training only. Unauthorized credential access is illegal and unethical.
