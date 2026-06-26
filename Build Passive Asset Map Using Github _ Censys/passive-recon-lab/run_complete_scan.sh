#!/bin/bash

echo "=== PASSIVE ASSET RECONNAISSANCE - COMPLETE SCAN ==="
echo "Starting comprehensive scan..."

cd ~/passive-recon-lab

# GitHub reconnaissance
echo -e "\n[1/3] Running GitHub reconnaissance..."
cd github-recon
python3 github_scanner.py
cd ..

# Censys scanning
echo -e "\n[2/3] Running Censys cloud asset discovery..."
cd censys-recon
python3 censys_scanner.py
cd ..

# Data aggregation
echo -e "\n[3/3] Aggregating data and generating reports..."
python3 asset_aggregator.py

echo -e "\n=== SCAN COMPLETE ==="
echo "Reports generated in ~/passive-recon-lab/reports/"
