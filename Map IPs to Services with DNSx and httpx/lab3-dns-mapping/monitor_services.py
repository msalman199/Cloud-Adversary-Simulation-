import time
import subprocess
from datetime import datetime

def monitor_services():
    while True:
        print(f"[{datetime.now()}] Running service check...")
        
        # Run httpx check
        subprocess.run(['httpx', '-l', 'lab3_results/extracted_ips.txt', 
                       '-status-code', '-title', '-o', 'monitoring_results.txt'])
        
        print("Check completed. Waiting 300 seconds...")
        time.sleep(300)  # Wait 5 minutes

if __name__ == "__main__":
    monitor_services()
