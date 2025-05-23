"""
check_nodes.py
--------------
Reads a list of URLs from nodes.txt and checks if each URL is responding (HTTP 200).
Outputs the results to report.txt as UP or DOWN.
"""

import requests

# Input and output file names
input_file = "nodes.txt"
output_file = "report.txt"

# Open the input file and read URLs
with open(input_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Open the output file
with open(output_file, "w") as report:
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            status = "UP" if response.status_code == 200 else "DOWN"
        except requests.RequestException:
            status = "DOWN"
        report.write(f"{url} - {status}\n")

print("Check complete. See report.txt for results.")
