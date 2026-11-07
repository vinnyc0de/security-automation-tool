# security-automation-tool
# Security Engineering Automation Tool

A simple Python command-line tool that demonstrates three basic security engineering concepts: SQL injection probing, privilege escalation checks, and log file analysis. Built as a learning project to explore core security analyst workflows.

## ⚠️ Disclaimer

This tool is intended **strictly for educational purposes** and for testing against systems you own or have **explicit written permission** to test. Running SQL injection payloads or reconnaissance tools against systems you do not own or lack authorization for is illegal in most jurisdictions and may violate the Computer Fraud and Abuse Act (US), the Computer Misuse Act (UK/Kenya), or similar laws elsewhere. Use responsibly.

## Features

- **SQL Injection Probe** — Sends a basic `' OR '1'='1` payload as a query parameter to a target URL and reports whether the server responded, as a starting point for manual testing.
- **Privilege Escalation Check** — Runs `whoami /priv` (Windows) to list the privileges available to the current user account.
- **Log Analysis** — Generates a sample log file and scans it for lines containing `ERROR` to demonstrate basic log-parsing and alerting logic.

## Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) library

Install dependencies:

```bash
pip install requests
```

## Usage

Run the script and enter a target URL when prompted:

```bash
python security_tool.py
```

Example:

```
Enter a URL to test (e.g., http://httpbin.org): http://httpbin.org
```

The tool will then:
1. Attempt the SQLi probe against the target.
2. Check current user privileges (Windows only).
3. Create a sample log file (`temp_log.txt`) and scan it for errors.

## Notes

- `check_privesc()` currently only supports Windows (`whoami /priv`). On Linux/macOS you'd want to swap this for something like `sudo -l` or `id`.
- The SQLi check is a reachability test, not a real vulnerability scanner — a `200 OK` response doesn't confirm an actual injection flaw. Treat results as a starting point for manual review, not a verdict.
- `analyze_logs()` uses a hardcoded dummy log for demonstration; point it at a real log file to use it practically.

## Roadmap Ideas

- Add OS detection to branch `check_privesc()` logic properly across platforms
- Replace the single SQLi payload with a configurable payload list
- Parse real log files instead of a generated sample
- Add structured output (JSON/CSV) for findings

## License

MIT License — feel free to use and modify for learning purposes.
