import os
from datetime import datetime

from core.helpers import get_date_range

LOG_FOLDER = "logs"

def _show_history(file_names):
    start_date, end_date = get_date_range()
    found = False
    if not os.path.exists(LOG_FOLDER):
        print("\nNo history found.")
        return
    for root, _, files in os.walk(LOG_FOLDER):
        for file in files:
            if file not in file_names:
                continue
            log_path = os.path.join(root, file)
            matched_records = []
            with open(log_path, "r", encoding="utf-8") as log:
                for line in log:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [part.strip() for part in line.split("|")]
                    if len(parts) < 4:
                        continue
                    try:
                        log_date = datetime.strptime(
                            parts[0],
                            "%d-%m-%Y %H:%M:%S"
                        )
                    except ValueError:
                        continue
                    if start_date and end_date:
                        if not (start_date <= log_date <= end_date):
                            continue
                    matched_records.append(line)
            if matched_records:
                print(f"\n{'=' * 80}")
                print(file.replace(".log", "").replace("_", " ").title())
                print(f"{'=' * 80}")
                for record in matched_records:
                    print(record)
                found = True
    if not found:
        print("\nNo history found for the selected date range.")

def show_file_history():
    _show_history([
        "create_file.log",
        "move_file.log",
        "copy_file.log",
        "rename_file.log",
        "delete_file.log"
    ])

def show_directory_history():
    _show_history([
        "create_directory.log",
        "rename_directory.log",
        "delete_directory.log"
    ])

def show_encryption_history():
    _show_history([
        "encrypt_file.log",
        "decrypt_file.log"
    ])

def show_compression_history():
    _show_history([
        "compress_file.log",
        "decompress_file.log"
    ])

def show_csv_history():
    _show_history([
        "generate_csv_report.log"
    ])

def show_json_history():
    _show_history([
        "generate_json_report.log"
    ])

def show_system_health_history():
    _show_history([
        "system_information.log",
        "cpu_usage.log",
        "memory_usage.log",
        "disk_usage.log",
        "network_information.log",
        "system_summary.log"
    ])