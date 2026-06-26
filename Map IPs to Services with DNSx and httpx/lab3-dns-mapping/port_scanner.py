import subprocess
import json

def scan_ports(ip_file):
    with open(ip_file, 'r') as f:
        ips = f.read().strip().split('\n')
    
    for ip in ips:
        if ip.strip():
            print(f"Scanning {ip}...")
            result = subprocess.run(['nmap', '-sS', '-O', ip], 
                                  capture_output=True, text=True)
            print(result.stdout)

if __name__ == "__main__":
    scan_ports("lab3_results/extracted_ips.txt")
