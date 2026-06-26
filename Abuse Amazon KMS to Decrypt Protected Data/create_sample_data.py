#!/usr/bin/env python3
import base64
import json

def create_sample_encrypted_data():
    """Generate sample encrypted data for testing."""
    
    sensitive_data = {
        "database_password": "MySecretDBPassword123!",
        "api_key": "sk-1234567890abcdef",
        "customer_data": {
            "name": "John Doe",
            "ssn": "123-45-6789",
            "credit_card": "4532-1234-5678-9012"
        }
    }
    
    # TODO: Convert dictionary to JSON string
    # TODO: Encode as base64
    # TODO: Write to encrypted_data.txt
    # TODO: Print confirmation message
    
    pass

if __name__ == "__main__":
    create_sample_encrypted_data()
