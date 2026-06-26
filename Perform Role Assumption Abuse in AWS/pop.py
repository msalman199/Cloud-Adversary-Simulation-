#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError

def test_role_capabilities(credentials):
    """
    Test permissions available with assumed role credentials.
    
    Args:
        credentials: Dictionary with AccessKeyId, SecretAccessKey, SessionToken
    
    TODO: Create boto3 session with provided credentials
    TODO: Test IAM actions (list_users, list_roles, create_user)
    TODO: Test EC2 actions (describe_instances, run_instances)
    TODO: Test S3 actions (list_buckets, create_bucket)
    TODO: Return list of successful actions
    
    Returns:
        List of capabilities (e.g., ['iam:list_users', 's3:list_buckets'])
    """
    session = boto3.Session(
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    
    capabilities = []
    
    # TODO: Test various service actions
    # Use try/except to catch AccessDenied errors
    # Only test read operations, avoid destructive actions
    
    pass

# TODO: Load assumed_roles.json and test each rol
