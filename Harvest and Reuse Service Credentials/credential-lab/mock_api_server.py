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
        Handle GET requests to /api/users endpoint.
        
        TODO: Extract Authorization or X-API-Key header
        TODO: Validate against VALID_TOKENS
        TODO: Return 200 with user data if valid
        TODO: Return 401 if invalid
        """
        pass
    
    def send_json_response(self, status, data):
        """
        Send JSON response with proper headers.
        
        TODO: Set response code
        TODO: Set Content-Type header
        TODO: Write JSON data
        """
        pass

# TODO: Start server on localhost:8080
