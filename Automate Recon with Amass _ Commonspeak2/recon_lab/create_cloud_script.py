#!/usr/bin/env python3

import subprocess
import sys
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from urllib.parse import urlparse

def create_cloud_enum_script():
    script_content = '''#!/usr/bin/env python3

import subprocess
import sys
import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

class CloudAssetEnumerator:
    def __init__(self, target_domain):
        self.target_domain = target_domain
        self.results = []
        self.lock = threading.Lock()
        
    def check_subdomain(self, subdomain):
        """Check if a subdomain exists and is accessible"""
        full_domain = f"{subdomain}.{self.target_domain}"
        try:
            # Try HTTP first
            response = requests.get(f"http://{full_domain}", timeout=5, allow_redirects=True)
            if response.status_code == 200:
                with self.lock:
                    self.results.append(f"{full_domain} - HTTP - {response.status_code}")
                    print(f"[+] Found: {full_domain} (HTTP)")
                return True
        except:
            pass
            
        try:
            # Try HTTPS
            response = requests.get(f"https://{full_domain}", timeout=5, allow_redirects=True, verify=False)
            if response.status_code == 200:
                with self.lock:
                    self.results.append(f"{full_domain} - HTTPS - {response.status_code}")
                    print(f"[+] Found: {full_domain} (HTTPS)")
                return True
        except:
            pass
            
        return False
    
    def enumerate_with_wordlist(self, wordlist_path, max_workers=10):
        """Enumerate subdomains using a wordlist"""
        if not os.path.exists(wordlist_path):
            print(f"[-] Wordlist not found: {wordlist_path}")
            return
            
        print(f"[*] Starting enumeration with {wordlist_path}")
        
        with open(wordlist_path, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.check_subdomain, subdomains[:100])  # Limit to first 100 for demo
    
    def save_results(self, output_file):
        """Save results to file"""
        with open(output_file, 'w') as f:
            for result in self.results:
                f.write(result + '\\n')
        print(f"[*] Results saved to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cloud_enum.py <target_domain>")
        sys.exit(1)
    
    target_domain = sys.argv[1]
    enumerator = CloudAssetEnumerator(target_domain)
    
    # Common cloud service subdomains
    cloud_subdomains = [
        "api", "app", "admin", "dev", "test", "staging", "prod", "www",
        "mail", "ftp", "blog", "shop", "store", "portal", "dashboard",
        "cdn", "static", "assets", "media", "images", "files", "docs",
        "support", "help", "status", "monitor", "health", "metrics"
    ]
    
    print(f"[*] Starting cloud asset enumeration for {target_domain}")
    
    # Check common cloud subdomains
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(enumerator.check_subdomain, cloud_subdomains)
    
    # Save results
    enumerator.save_results(f"cloud_assets_{target_domain}.txt")
    
    print(f"[*] Enumeration complete. Found {len(enumerator.results)} assets.")

if __name__ == "__main__":
    main()
'''
    
    with open('cloud_enum.py', 'w') as f:
        f.write(script_content)
    
    os.chmod('cloud_enum.py', 0o755)
    print("[*] Cloud enumeration script created successfully")

# Create the script
create_cloud_enum_script()
