#!/usr/bin/env python3
import json

def analyze_kms_policy(policy_file):
    """
    Analyze KMS policy for security vulnerabilities.
    
    Args:
        policy_file: Path to the policy JSON file
    
    Returns:
        List of vulnerability descriptions
    """
    vulnerabilities = []
    
    # TODO: Load the policy JSON file
    # TODO: Iterate through policy statements
    # TODO: Check for wildcard principals
    # TODO: Check for overly broad actions (kms:*, kms:Decrypt)
    # TODO: Check for missing condition statements
    # TODO: Return list of vulnerabilities
    
    pass

def main():
    vulns = analyze_kms_policy('vulnerable_policy.json')
    
    print("KMS Policy Vulnerability Analysis")
    print("=" * 40)
    
    # TODO: Display each vulnerability with numbering
    # TODO: Print total count of vulnerabilities
    
    pass

if __name__ == "__main__":
    main()
