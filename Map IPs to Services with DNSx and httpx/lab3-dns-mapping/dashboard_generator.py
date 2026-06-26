#!/usr/bin/env python3

import pandas as pd
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import threading
import time

class DashboardGenerator:
    def __init__(self, results_dir="lab3_results"):
        self.results_dir = results_dir
    
    def generate_html_dashboard(self):
        """Generate HTML dashboard"""
        try:
            df = pd.read_csv(f"{self.results_dir}/service_mapping_report.csv")
        except FileNotFoundError:
            print("[-] CSV report not found. Run the mapper script first.")
            return
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>DNS Service Mapping Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .stats {{ display: flex; justify-content: space-around; }}
        .stat-box {{ text-align: center; padding: 20px; background-color: #e9ecef; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>DNS Service Mapping Dashboard</h1>
        <p>Comprehensive analysis of discovered services and their characteristics</p>
    </div>
    
    <div class="section">
        <h2>Summary Statistics</h2>
        <div class="stats">
            <div class="stat-box">
                <h3>{len(df)}</h3>
                <p>Total Services</p>
            </div>
            <div class="stat-box">
                <h3>{len(df['status_code'].unique())}</h3>
                <p>Unique Status Codes</p>
            </div>
            <div class="stat-box">
                <h3>{len(df[df['status_code'] == 200])}</h3>
                <p>Successful Responses</p>
            </div>
        </div>
    </div>
    
    <div class="section">
        <h2>Discovered Services</h2>
        <table>
            <tr>
                <th>URL</th>
                <th>Status Code</th>
                <th>Title</th>
                <th>Technologies</th>
                <th>Server</th>
            </tr>
"""
        
        for _, row in df.iterrows():
            html_content += f"""
            <tr>
                <td><a href="{row['url']}" target="_blank">{row['url']}</a></td>
                <td>{row['status_code']}</td>
                <td>{row['title'] if pd.notna(row['title']) else 'N/A'}</td>
                <td>{row['technologies'] if pd.notna(row['technologies']) else 'N/A'}</td>
                <td>{row['server'] if pd.notna(row['server']) else 'N/A'}</td>
            </tr>
"""
        
        html_content += """
        </table>
    </div>
</body>
</html>
"""
        
        # Save HTML file
        with open(f"{self.results_dir}/dashboard.html", 'w') as f:
            f.write(html_content)
        
        print(f"[+] Dashboard generated: {self.results_dir}/dashboard.html")
    
    def serve_dashboard(self):
        """Serve dashboard on local web server"""
        import os
        os.chdir(self.results_dir)
        
        server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
        print("[+] Dashboard server starting on http://localhost:8000/dashboard.html")
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://localhost:8000/dashboard.html')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.start()
        
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n[+] Dashboard server stopped")
            server.shutdown()

def main():
    dashboard = DashboardGenerator()
    dashboard.generate_html_dashboard()
    
    print("\nOptions:")
    print("1. View dashboard in browser (press Enter)")
    print("2. Skip dashboard server (type 'skip')")
    
    choice = input("Choice: ").strip().lower()
    
    if choice != 'skip':
        dashboard.serve_dashboard()

if __name__ == "__main__":
    main()
