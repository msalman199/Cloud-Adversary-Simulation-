#!/usr/bin/env python3
"""
SSM Parameter Vulnerability Assessment
Students: Complete the security checks
"""

import json
import os
import re

class SSMVulnerabilityScanner:
    def __init__(self, parameters_dir="parameters"):
        self.parameters_dir = parameters_dir
        self.vulnerabilities = []
        self.sensitive_keywords = [
            'password', 'secret', 'key', 'token', 
            'credential', 'auth', 'private'
        ]
    
    def load_parameters(self):
        """
        Load all parameters from directory
        
        TODO: Implement parameter loading
        Returns:
            List of parameter dictionaries
        """
        # TODO: Load all JSON files from parameters_dir
        pass
    
    def check_plaintext_secrets(self, parameters):
        """
        Identify sensitive data stored as plaintext (Type: String)
        
        TODO: Implement the following checks:
        1. Check if parameter name contains sensitive keywords
        2. Check if Type is "String" (not SecureString)
        3. If both true, add to vulnerabilities list
        4. Print findings with severity level
        """
        print("[+] Checking for plaintext secrets...")
        
        # TODO: Implement plaintext secret detection
        pass
    
    def check_naming_conventions(self, parameters):
        """
        Check for overly descriptive parameter names
        
        TODO: Identify parameters with names that reveal:
        - Environment (prod, production, staging)
        - Access level (admin, root, master)
        - Specific technologies (mysql, postgres, redis)
        """
        print("[+] Checking parameter naming conventions...")
        
        # TODO: Implement naming convention checks
        pass
    
    def check_version_history(self, parameters):
        """
        Identify parameters with multiple versions
        
        TODO: Check Version field and flag parameters with Version > 1
        Note: Old versions may contain different secrets
        """
        print("[+] Checking parameter version history...")
        
        # TODO: Implement version history checks
        pass
    
    def generate_report(self):
        """
        Generate vulnerability report
        
        TODO: Create a summary report showing:
        - Total vulnerabilities found
        - Breakdown by severity (CRITICAL, HIGH, MEDIUM, LOW)
        - Specific findings with recommendations
        """
        # TODO: Implement report generation
        pass

if __name__ == "__main__":
    scanner = SSMVulnerabilityScanner()
    # TODO: Load parameters
    # TODO: Run all security checks
    # TODO: Generate report
