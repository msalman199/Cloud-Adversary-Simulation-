#!/usr/bin/env python3

import json
import csv
import os
import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

def create_results_processor():
    script_content = '''#!/usr/bin/env python3

import json
import csv
import os
import re
from collections import Counter, defaultdict
import sys

class ReconResultsProcessor:
    def __init__(self):
        self.amass_results = []
        self.cloud_results = []
        self.combined_results = []
        
    def load_amass_results(self, filename):
        """Load Amass enumeration results"""
        if not os.path.exists(filename):
            print(f"[-] Amass results file not found: {filename}")
            return
            
        with open(filename, 'r') as f:
            self.amass_results = [line.strip() for line in f if line.strip()]
        
        print(f"[+] Loaded {len(self.amass_results)} Amass results")
    
    def load_cloud_results(self, filename):
        """Load cloud enumeration results"""
        if not os.path.exists(filename):
            print(f"[-] Cloud results file not found: {filename}")
            return
            
        with open(filename, 'r') as f:
            self.cloud_results = [line.strip() for line in f if line.strip()]
        
        print(f"[+] Loaded {len(self.cloud_results)} cloud enumeration results")
    
    def analyze_subdomains(self):
        """Analyze subdomain patterns"""
        all_domains = self.amass_results + [result.split(' - ')[0] for result in self.cloud_results]
        
        # Extract subdomain patterns
        patterns = defaultdict(int)
        tlds = defaultdict(int)
        
        for domain in all_domains:
            if '.' in domain:
                parts = domain.split('.')
                if len(parts) >= 2:
                    subdomain = parts[0]
                    tld = '.'.join(parts[-2:])
                    patterns[subdomain] += 1
                    tlds[tld] += 1
        
        return patterns, tlds
    
    def generate_statistics(self):
        """Generate comprehensive statistics"""
        patterns, tlds = self.analyze_subdomains()
        
        stats = {
            'total_amass_results': len(self.amass_results),
            'total_cloud_results': len(self.cloud_results),
            'unique_domains': len(set(self.amass_results + [r.split(' - ')[0] for r in self.cloud_results])),
            'top_subdomains': dict(Counter(patterns).most_common(10)),
            'top_tlds': dict(Counter(tlds).most_common(5))
        }
        
        return stats
    
    def export_to_csv(self, output_file):
        """Export results to CSV format"""
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Domain', 'Source', 'Status', 'Protocol'])
            
            # Add Amass results
            for domain in self.amass_results:
                writer.writerow([domain, 'Amass', 'Discovered', 'DNS'])
            
            # Add cloud results
            for result in self.cloud_results:
                parts = result.split(' - ')
                if len(parts) >= 3:
                    domain, protocol, status = parts[0], parts[1], parts[2]
                    writer.writerow([domain, 'Cloud_Enum', status, protocol])
        
        print(f"[+] Results exported to {output_file}")
    
    def export_to_json(self, output_file):
        """Export results to JSON format"""
        data = {
            'amass_results': self.amass_results,
            'cloud_results': self.cloud_results,
            'statistics': self.generate_statistics(),
            'timestamp': str(pd.Timestamp.now()) if 'pd' in globals() else 'N/A'
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"[+] Results exported to {output_file}")
    
    def create_summary_report(self, output_file):
        """Create a comprehensive summary report"""
        stats = self.generate_statistics()
        
        report = f"""
# Reconnaissance Results Summary Report

## Overview
- Total Amass Results: {stats['total_amass_results']}
- Total Cloud Enumeration Results: {stats['total_cloud_results']}
- Unique Domains Found: {stats['unique_domains']}

## Top Subdomain Patterns
"""
        
        for subdomain, count in stats['top_subdomains'].items():
            report += f"- {subdomain}: {count} occurrences\\n"
        
        report += "\\n## Top Level Domains\\n"
        for tld, count in stats['top_tlds'].items():
            report += f"- {tld}: {count} occurrences\\n"
        
        report += f"""
## Detailed Results

### Amass Discoveries
"""
        for domain in self.amass_results[:20]:  # Show first 20
            report += f"- {domain}\\n"
        
        if len(self.amass_results) > 20:
            report += f"... and {len(self.amass_results) - 20} more\\n"
        
        report += "\\n### Cloud Asset Discoveries\\n"
        for result in self.cloud_results[:20]:  # Show first 20
            report += f"- {result}\\n"
        
        if len(self.cloud_results) > 20:
            report += f"... and {len(self.cloud_results) - 20} more\\n"
        
        with open(output_file, 'w') as f:
            f.write(report)
        
        print(f"[+] Summary report created: {output_file}")

def main():
    processor = ReconResultsProcessor()
    
    # Load results
    processor.load_amass_results('amass_comprehensive.txt')
    processor.load_cloud_results('cloud_assets_example.com.txt')
    
    # Generate outputs
    processor.export_to_csv('recon_results.csv')
    processor.export_to_json('recon_results.json')
    processor.create_summary_report('recon_summary.md')
    
    # Display statistics
    stats = processor.generate_statistics()
    print("\\n[*] Reconnaissance Statistics:")
    print(f"    Total unique domains: {stats['unique_domains']}")
    print(f"    Amass results: {stats['total_amass_results']}")
    print(f"    Cloud enumeration results: {stats['total_cloud_results']}")
    
    print("\\n[*] Processing complete!")

if __name__ == "__main__":
    main()
'''
    
    with open('process_results.py', 'w') as f:
        f.write(script_content)
    
    os.chmod('process_results.py', 0o755)
    print("[*] Results processing script created successfully")

# Create the processing script
create_results_processor()
