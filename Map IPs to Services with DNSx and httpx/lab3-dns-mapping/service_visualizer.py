#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

class ServiceVisualizer:
    def __init__(self, results_dir="lab3_results"):
        self.results_dir = results_dir
        plt.style.use('default')
    
    def load_data(self):
        """Load data from CSV report"""
        try:
            df = pd.read_csv(f"{self.results_dir}/service_mapping_report.csv")
            return df
        except FileNotFoundError:
            print("[-] CSV report not found. Run the mapper script first.")
            return None
    
    def create_status_code_chart(self, df):
        """Create status code distribution chart"""
        plt.figure(figsize=(10, 6))
        status_counts = df['status_code'].value_counts()
        
        plt.subplot(1, 2, 1)
        status_counts.plot(kind='bar', color='skyblue')
        plt.title('HTTP Status Code Distribution')
        plt.xlabel('Status Code')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        
        plt.subplot(1, 2, 2)
        plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%')
        plt.title('Status Code Distribution (Pie Chart)')
        
        plt.tight_layout()
        plt.savefig(f"{self.results_dir}/status_code_distribution.png", dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_technology_chart(self, df):
        """Create technology distribution chart"""
        # Extract all technologies
        all_techs = []
        for tech_str in df['technologies'].dropna():
            if tech_str:
                all_techs.extend([t.strip() for t in tech_str.split(',')])
        
        tech_counts = Counter(all_techs)
        top_techs = dict(tech_counts.most_common(10))
        
        plt.figure(figsize=(12, 6))
        plt.bar(top_techs.keys(), top_techs.values(), color='lightcoral')
        plt.title('Top 10 Technologies Detected')
        plt.xlabel('Technology')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f"{self.results_dir}/technology_distribution.png", dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_server_chart(self, df):
        """Create server type distribution chart"""
        server_counts = df['server'].value_counts().head(10)
        
        plt.figure(figsize=(10, 6))
        server_counts.plot(kind='barh', color='lightgreen')
        plt.title('Top 10 Server Types')
        plt.xlabel('Count')
        plt.ylabel('Server Type')
        plt.tight_layout()
        plt.savefig(f"{self.results_dir}/server_distribution.png", dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_all_visualizations(self):
        """Generate all visualization charts"""
        df = self.load_data()
        if df is None:
            return
        
        print("[+] Generating visualizations...")
        
        self.create_status_code_chart(df)
        self.create_technology_chart(df)
        self.create_server_chart(df)
        
        print(f"[+] All visualizations saved to {self.results_dir}/ directory")

def main():
    visualizer = ServiceVisualizer()
    visualizer.generate_all_visualizations()

if __name__ == "__main__":
    main()
