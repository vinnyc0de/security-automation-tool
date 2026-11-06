import requests
import subprocess
import os

def test_sqli(url):
    print(f"\n--- Scanning {url} for SQLi ---")
    # Simple payload to see if the server reacts
    payload = "' OR '1'='1"
    try:
        response = requests.get(url, params={'id': payload}, timeout=5)
        if response.status_code == 200:
            print("[+] Target reachable. Check manual logs for bypass results.")
        else:
            print("[-] No immediate vulnerability found.")
    except:
        print("[!] Connection failed.")

def check_privesc():
    print("\n--- Checking Privilege Escalation Vectors ---")
    # On Windows, this shows what permissions your current user has
    os.system("whoami /priv")

def analyze_logs():
    print("\n--- Analyzing Log Files ---")
    # Creates a dummy log to demonstrate analysis
    log_content = "ERROR: Failed login from 192.168.1.1\nINFO: User 'lincoln' logged in\n"
    with open("temp_log.txt", "w") as f: f.write(log_content)
    
    with open("temp_log.txt", "r") as f:
        for line in f:
            if "ERROR" in line:
                print(f"[ALERT] Found suspicious entry: {line.strip()}")

if __name__ == "__main__":
    print("Security Engineering Automation Tool Loaded.")
    target = input("Enter a URL to test (e.g., http://httpbin.org): ")
    test_sqli(target)
    check_privesc()
    analyze_logs()
