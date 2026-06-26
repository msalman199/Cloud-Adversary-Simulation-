#!/bin/bash
TARGET=$1
DATE=$(date +"%Y-%m-%d")

# Generate HTML report
echo "<html><head><title>Recon Report for $TARGET</title></head><body>" > "report_${TARGET}_${DATE}.html"
echo "<h1>Reconnaissance Report for $TARGET</h1>" >> "report_${TARGET}_${DATE}.html"
echo "<h2>Generated on: $DATE</h2>" >> "report_${TARGET}_${DATE}.html"

# Add CSV data as HTML table
echo "<h3>Discovered Assets</h3>" >> "report_${TARGET}_${DATE}.html"
echo "<table border='1'>" >> "report_${TARGET}_${DATE}.html"
head -1 recon_results.csv | sed 's/,/<\/th><th>/g' | sed 's/^/<tr><th>/' | sed 's/$/<\/th><\/tr>/' >> "report_${TARGET}_${DATE}.html"
tail -n +2 recon_results.csv | sed 's/,/<\/td><td>/g' | sed 's/^/<tr><td>/' | sed 's/$/<\/td><\/tr>/' >> "report_${TARGET}_${DATE}.html"
echo "</table>" >> "report_${TARGET}_${DATE}.html"
echo "</body></html>" >> "report_${TARGET}_${DATE}.html"

echo "HTML report generated: report_${TARGET}_${DATE}.html"
EOF
