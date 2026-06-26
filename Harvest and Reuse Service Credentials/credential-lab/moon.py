#!/usr/bin/env python3
import json
import requests

class CredentialTester:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.successful = []
        self.endpoints = [
            {'path': '/api/users', 'method': 'GET'},
            {'path': '/api/admin', 'method': 'GET'}
        ]
    
    def load_credentials(self, creds_file):
        """
        Load harvested credentials from JSON file.
        
        TODO: Read and parse JSON file
        TODO: Return list of credentials
        """
        pass
    
    def test_bearer_token(self, token, endpoint):
        """
        Test credential as Bearer token.
        
        TODO: Create Authorization header
        TODO: Make HTTP request
        TODO: Return response details
        """
        pass
    
    def test_api_key(self, api_key, endpoint):
        """
        Test credential as API key.
        
        TODO: Create X-API-Key header
        TODO: Make HTTP request
        TODO: Check response status
        """
        pass
    
    def test_credential(self, credential):
        """
        Test single credential against all endpoints.
        
        TODO: Determine credential type
        TODO: Try appropriate authentication method
        TODO: Record successful authentications
        """
        pass
    
    def run_tests(self, creds_file):
        """
        Test all credentials from file.
        
        TODO: Load credentials
        TODO: Iterate and test each one
        TODO: Print summary of results
        """
        pass

# TODO: Create tester instance
# TODO: Run tests on extracted credentials
# TODO: Display results
