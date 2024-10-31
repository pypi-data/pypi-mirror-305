
import os
import requests
import zipfile
import subprocess
import re
import webbrowser  # Import the webbrowser module

# Step 1: Download Feroxbuster
def download_feroxbuster():
    print("Downloading Feroxbuster...")
    url = "https://github.com/epi052/feroxbuster/releases/latest/download/x86_64-windows-feroxbuster.exe.zip"
    response = requests.get(url)
    with open("feroxbuster.zip", "wb") as f:
        f.write(response.content)
    print("Download complete!")

# Step 2: Unzip Feroxbuster
def unzip_feroxbuster():
    print("Unzipping Feroxbuster...")
    with zipfile.ZipFile("feroxbuster.zip", "r") as zip_ref:
        zip_ref.extractall("feroxbuster")
    print("Unzipping complete!")

# Step 3: Run Feroxbuster with URL and Wordlist
def run_feroxbuster(url, wordlist_path):
    feroxbuster_path = os.path.join("feroxbuster", "feroxbuster.exe")
    command = f'{feroxbuster_path} -u {url} -w {wordlist_path} -o feroxbuster_output.log'
    print(f"Running Feroxbuster: {command}")
    subprocess.run(command, shell=True)

# Step 4: Generate HTML Report
def generate_report():
    report_lines = []
    status_count = {}  # Dictionary to count occurrences of each status code

    # Check if the log file exists
    if not os.path.exists("feroxbuster_output.log"):
        print("Error: Log file not found!")
        return

    with open("feroxbuster_output.log", "r") as f:
        output = f.read()

    # Extracting paths and status codes
    paths = re.findall(r'(\d{3})\s+GET\s+(.+)', output)

    # Counting occurrences of each status code
    for status, path in paths:
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    total_found = len(paths)

    # HTML Report Header
    report_lines.append("<html>\n<head>\n<title>Feroxbuster Scan Report</title>\n")
    report_lines.append("<style>\n")
    report_lines.append("body { font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9; }\n")
    report_lines.append("h1 { color: #333; }\n")
    report_lines.append("h2 { color: #555; }\n")
    report_lines.append("table { width: 100%; border-collapse: collapse; margin-top: 20px; }\n")
    report_lines.append("th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }\n")
    report_lines.append("th { background-color: #007BFF; color: white; }\n")
    report_lines.append("tr:nth-child(even) { background-color: #f2f2f2; }\n")
    report_lines.append("tr:nth-child(odd) { background-color: #ffffff; }\n")
    report_lines.append("</style>\n</head>\n<body>\n")

    # Report Body
    report_lines.append("<h1>Feroxbuster Scan Report</h1>\n")
    report_lines.append("<h2>Summary</h2>\n")
    report_lines.append(f"<p>Total Paths Discovered: <strong>{total_found}</strong></p>\n")

    # Display the count of each status code
    if status_count:
        report_lines.append("<h2>Status Codes Summary</h2>\n")
        report_lines.append("<table>\n")
        report_lines.append("<tr><th>Status Code</th><th>Count</th></tr>\n")
        for status, count in status_count.items():
            report_lines.append(f"<tr><td>{status}</td><td>{count}</td></tr>\n")
        report_lines.append("</table>\n")

    if total_found > 0:
        report_lines.append("<h2>Discovered Paths</h2>\n")
        report_lines.append("<table>\n")
        report_lines.append("<tr><th>Status Code</th><th>Path URL</th></tr>\n")
        for status, path in paths:
            report_lines.append(f"<tr><td>{status}</td><td>{path}</td></tr>\n")
        report_lines.append("</table>\n")

    report_lines.append("</body>\n</html>")

    # Write the report to an HTML file
    with open("feroxbuster_report.html", "w") as report_file:
        report_file.writelines(report_lines)
    print("Report generated: feroxbuster_report.html")

# Main function to run the entire process
def main():
    # Step 6: Check if Feroxbuster is already downloaded
    if not os.path.exists("feroxbuster"):
        download_feroxbuster()
        unzip_feroxbuster()
        
    # Step 7: Prompt for the URL
    url = input("Enter the URL of the website to scan: ")

    # Step 8: Wordlist file path (adjust to your specific wordlist location or URL)
    wordlist_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt"
    wordlist_path = "common.txt"
    
    # Download the wordlist if not already present
    if not os.path.exists(wordlist_path):
        print("Downloading wordlist...")
        wordlist_response = requests.get(wordlist_url)
        with open(wordlist_path, "wb") as f:
            f.write(wordlist_response.content)
        print("Wordlist downloaded.")
    
    # Step 9: Run Feroxbuster with the URL and wordlist
    run_feroxbuster(url, wordlist_path)
    
    # Step 10: Generate the report
    generate_report()
    
    # Step 11: Display link to report
    report_path = os.path.abspath("feroxbuster_report.html")
    print("You can view the report at: file://" + report_path)

    # Automatically open the report in the default web browser
    webbrowser.open("file://" + report_path)

# Run main() if this script is executed directly
if __name__ == "__main__":
    main()
