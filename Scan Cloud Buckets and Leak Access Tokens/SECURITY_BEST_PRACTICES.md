# Cloud Storage Security Best Practices

## AWS S3 Security

### Block Public Access
- Enable "Block all public access" at account level
- Use bucket policies to restrict access
- Implement least privilege IAM policies

### Encryption
- Enable default encryption (AES-256 or KMS)
- Use SSL/TLS for data in transit
- Rotate encryption keys regularly

### Monitoring
- Enable CloudTrail logging
- Set up S3 access logging
- Configure CloudWatch alarms for unusual access

## Token Management

### Prevention
- Never commit credentials to version control
- Use environment variables or secret managers
- Implement pre-commit hooks to scan for secrets

### Detection
- Regularly scan repositories for leaked tokens
- Use automated secret scanning tools
- Monitor for unauthorized API usage

### Response
- Immediately revoke compromised tokens
- Rotate all related credentials
- Audit access logs for unauthorized activity
