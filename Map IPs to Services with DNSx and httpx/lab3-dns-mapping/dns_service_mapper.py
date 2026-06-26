#!/usr/bin/env python3

import subprocess
import json
import csv
import os
from datetime import datetime

class DNSServiceMapper:
    def __init__(self, output_dir="lab3_results"):
        self.output_dir = output_dir
        self.create_output_directory()
    
    def create_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def run_dnsx_enumeration(self, domains_file):
        """Run DNSx enumeration on provided domains"""
        print("[+] Starting DNS enumeration with DNSx...")
        
        # Basic DNS resolution
        dns_cmd = f"dnsx -l {domains_file} -a -resp -json -o {self.output_dir}/dns_results.json"
        subprocess.run(dns_cmd, shell=True, capture_output=True)
        
        # Extract IPs
        ip_extraction_cmd = f"dnsx -l {domains_file} -a -resp-only | grep -oE '([0-9]{{1,3}}\.){{3}}[0-9]{{1,3}}' > {self.output_dir}/extracted_ips.txt"
        subprocess.run(ip_extraction_cmd, shell=True)
        
        print("[+] DNS enumeration completed")
    
    def run_httpx_enumeration(self, ips_file):
        """Run httpx enumeration on discovered IPs"""
        print("[+] Starting HTTP service enumeration with httpx...")
        
        httpx_cmd = f"httpx -l {ips_file} -ports 80,443,8080,8443,3000,5000,9000 -title -tech-detect -status-code -json -o {self.output_dir}/http_services.json"
        subprocess.run(httpx_cmd, shell=True, capture_output=True)
        
        print("[+] HTTP service enumeration completed")
    
    def parse_results(self):
        """Parse and combine DNS and HTTP results"""
        print("[+] Parsing and combining results...")
        
        combined_results = []
        
        # Parse DNS results
        dns_results = {}
        try:
            with open(f"{self.output_dir}/dns_results.json", 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line.strip())
                        if 'host' in data and 'a' in data:
                            dns_results[data['host']] = data['a']
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            print("[-] DNS results file not found")
        
        # Parse HTTP results
        try:
            with open(f"{self.output_dir}/http_services.json", 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line.strip())
                        combined_results.append({
                            'url': data.get('url', ''),
                            'status_code': data.get('status_code', ''),
                            'title': data.get('title', ''),
                            'tech': data.get('tech', []),
                            'server': data.get('server', ''),
                            'content_length': data.get('content_length', 0)
                        })
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            print("[-] HTTP results file not found")
        
        return combined_results
    
    def generate_csv_report(self, results):
        """Generate CSV report from results"""
        print("[+] Generating CSV report...")
        
        csv_file = f"{self.output_dir}/service_mapping_report.csv"
        
        with open(csv_file, 'w', newline='') as csvfile:
            fieldnames = ['url', 'status_code', 'title', 'technologies', 'server', 'content_length']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in results:
                writer.writerow({
                    'url': result['url'],
                    'status_code': result['status_code'],
                    'title': result['title'],
                    'technologies': ', '.join(result['tech']) if result['tech'] else '',
                    'server': result['server'],
                    'content_length': result['content_length']
                })
        
        print(f"[+] CSV report saved to {csv_file}")
    
    def generate_summary_report(self, results):
        """Generate summary statistics"""
        print("[+] Generating summary report...")
        
        total_services = len(results)
        status_codes = {}
        technologies = {}
        servers = {}
        
        for result in results:
            # Count status codes
            status = str(result['status_code'])
            status_codes[status] = status_codes.get(status, 0) + 1
            
            # Count technologies
            for tech in result['tech']:
                technologies[tech] = technologies.get(tech, 0) + 1
            
            # Count servers
            server = result['server']
            if server:
                servers[server] = servers.get(server, 0) + 1
        
        # Write summary report
        summary_file = f"{self.output_dir}/summary_report.txt"
        with open(summary_file, 'w') as f:
            f.write(f"DNS and HTTP Service Mapping Summary Report\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*50}\n\n")
            
            f.write(f"Total Services Discovered: {total_services}\n\n")
            
            f.write("Status Code Distribution:\n")
            for status, count in sorted(status_codes.items()):
                f.write(f"  {status}: {count}\n")
            
            f.write("\nTop Technologies Detected:\n")
            for tech, count in sorted(technologies.items(), key=lambda x: x[1], reverse=True)[:10]:
                f.write(f"  {tech}: {count}\n")
            
            f.write("\nTop Server Types:\n")
            for server, count in sorted(servers.items(), key=lambda x: x[1], reverse=True)[:10]:
                f.write(f"  {server}: {count}\n")
        
        print(f"[+] Summary report saved to {summary_file}")

def main():
    # Initialize mapper
    mapper = DNSServiceMapper()
    
    # Create sample domains file
    domains_file = "target_domains.txt"
    with open(domains_file, 'w') as f:
        f.write("google.com\ngithub.com\nstackoverflow.com\ncloudflare.com\namazon.com\nmicrosoft.com\n")
    
    # Run enumeration
    mapper.run_dnsx_enumeration(domains_file)
    mapper.run_httpx_enumeration(f"{mapper.output_dir}/extracted_ips.txt")
    
    # Parse and generate reports
    results = mapper.parse_results()
    mapper.generate_csv_report(results)
    mapper.generate_summary_report(results)
    
    print(f"\n[+] All results saved to {mapper.output_dir}/ directory")
    print("[+] Automation completed successfully!")

if __name__ == "__main__":
    main()
