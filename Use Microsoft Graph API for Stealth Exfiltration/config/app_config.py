class GraphConfig:
    """Configuration for Microsoft Graph API access"""
    
    # Simulated credentials (educational purposes only)
    CLIENT_ID = "12345678-1234-1234-1234-123456789012"
    CLIENT_SECRET = "simulated_secret_for_lab"
    TENANT_ID = "87654321-4321-4321-4321-210987654321"
    
    # API endpoints
    GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"
    AUTH_URL = "https://login.microsoftonline.com"
    
    # Required scopes
    SCOPES = [
        "https://graph.microsoft.com/.default"
    ]
    
    # Operational parameters
    REQUEST_DELAY = 2  # seconds
    MAX_RETRIES = 3
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
