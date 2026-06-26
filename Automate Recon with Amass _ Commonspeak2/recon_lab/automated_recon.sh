#!/bin/bash

# Automated Reconnaissance Workflow Script
# Lab 1: Automate Recon with Amass + Commonspeak2

echo "[*] Starting Automated Reconnaissance Workflow"
echo "================================================"

# Check if target domain is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_domain>"
    echo "Example: $0 example.com"
    exit 1
fi

TARGET_DOMAIN=$1
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
RESULTS_DIR="recon_${TARGET_DOMAIN}_${TIMESTAMP}"

# Create results directory
mkdir -p "$RESULTS_DIR"
cd "$RESULTS_DIR"

echo "[*] Target Domain: $TARGET_DOMAIN"
echo "[*] Results Directory: $RESULTS_DIR"
echo "[*] Timestamp: $TIMESTAMP"

# Step 1: Run Amass enumeration
echo ""
echo "[*] Step 1: Running Amass enumeration..."
echo "----------------------------------------"

# Passive enumeration
echo "[*] Running passive enumeration..."
amass enum -passive -d "$TARGET_DOMAIN" -o "amass_passive_${TARGET_DOMAIN}.txt"

# Active enumeration with brute force (limited for demo)
echo "[*] Running active enumeration..."
timeout 300 amass enum -d "$TARGET_DOMAIN" -brute -w /usr/share/wordlists/dirb/common.txt -o "amass_active_${TARGET_DOMAIN}.txt" 2>/dev/null || echo "[*] Amass active scan completed (timeout reached)"

# Combine results
cat "amass_passive_${TARGET_DOMAIN}.txt" "amass_active_${TARGET_DOMAIN}.txt" 2>/dev/null | sort -u > "amass_combined_${TARGET_DOMAIN}.txt"

echo "[+] Amass enumeration completed"
echo "    Passive results: $(wc -l < amass_passive_${TARGET_DOMAIN}.txt 2>/dev/null || echo 0)"
echo "    Active results: $(wc -l < amass_active_${TARGET_DOMAIN}.txt 2>/dev/null || echo 0)"
echo "    Combined unique results: $(wc -l < amass_combined_${TARGET_DOMAIN}.txt)"

# Step 2: Run cloud asset enumeration
echo ""
echo "[*] Step 2: Running cloud asset enumeration..."
echo "----------------------------------------------"

# Copy the cloud enumeration script to current directory
cp ../cloud_enum.py .

# Run cloud enumeration
python3 cloud_enum.py "$TARGET_DOMAIN"

echo "[+] Cloud asset enumeration completed"

# Step 3: Process and analyze results
echo ""
echo "[*] Step 3: Processing and analyzing results..."
echo "-----------------------------------------------"

# Copy the results processing script
cp ../process_results.py .

# Modify the processor to use our specific files
sed -i "s/amass_comprehensive.txt/amass_combined_${TARGET_DOMAIN}.txt/g" process_results.py
sed -i "s/cloud_assets_example.com.txt/cloud_assets_${TARGET_DOMAIN}.txt/g" process_results.py

# Run results processing
python3 process_results.py

echo "[+] Results processing completed"

# Step 4: Generate final summary
echo ""
echo "[*] Step 4: Generating final summary..."
echo "---------------------------------------"

TOTAL_AMASS=$(wc -l < "amass_combined_${TARGET_DOMAIN}.txt" 2>/dev/null || echo 0)
TOTAL_CLOUD=$(wc -l < "cloud_assets_${TARGET_DOMAIN}.txt" 2>/dev/null || echo 0)

cat > "final_summary_${TARGET_DOMAIN}.txt" << EOL
Automated Reconnaissance Summary for ${TARGET_DOMAIN}
Generated on: $(date)

RESULTS OVERVIEW:
================
- Amass Discoveries: ${TOTAL_AMASS}
- Cloud Asset Discoveries: ${TOTAL_CLOUD}
- Total Unique Assets: $((TOTAL_AMASS + TOTAL_CLOUD))

FILES GENERATED:
===============
- amass_passive_${TARGET_DOMAIN}.txt
- amass_active_${TARGET_DOMAIN}.txt
- amass_combined_${TARGET_DOMAIN}.txt
- cloud_assets_${TARGET_DOMAIN}.txt
- recon_results.csv
- recon_results.json
- recon_summary.md

NEXT STEPS:
==========
1. Review the generated CSV file for structured data analysis
2. Examine the JSON file for programmatic processing
3. Read the markdown summary for human-readable insights
4. Validate discovered assets manually
5. Proceed with further security assessment based on findings

EOL

echo "[+] Final summary generated: final_summary_${TARGET_DOMAIN}.txt"

# Display final results
echo ""
echo "=========================================="
echo "AUTOMATED RECONNAISSANCE COMPLETED"
echo "=========================================="
echo "Target Domain: $TARGET_DOMAIN"
echo "Results Directory: $(pwd)"
echo "Total Files Generated: $(ls -1 | wc -l)"
echo ""
echo "Key Results:"
echo "- Amass Discoveries: $TOTAL_AMASS"
echo "- Cloud Asset Discoveries: $TOTAL_CLOUD"
echo ""
echo "Review the files in this directory for detailed results."
echo "=========================================="

# Return to parent directory
cd ..

echo "[*] Workflow completed successfully!"
EOF
