import re

def analyze_logs(file_path):
    suspicious_keywords = ["failed", "unauthorized", "invalid", "error"]
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, start=1):
            if any(keyword in line.lower() for keyword in suspicious_keywords):
                print(f"[!] Suspicious entry on line {line_num}: {line.strip()}")

if __name__ == "__main__":
    log_file = "sample_logs.txt"
    analyze_logs(log_file)

Add initial log analyzer script
