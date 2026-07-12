import os
import csv
import json

from datetime import datetime
from core.helpers import get_date_range
from core.logger import *

LOG_FOLDER = "logs"
CSV_FOLDER = os.path.join("reports", "csv")
JSON_FOLDER = os.path.join("reports", "json")

def _read_logs(start_date=None, end_date=None):
    records = []
    if not os.path.exists(LOG_FOLDER):
        return records
    for root, _, files in os.walk(LOG_FOLDER):
        if not files:
            continue
        module = os.path.basename(root)
        for file in files:
            if not file.endswith(".log"):
                continue
            log_file = os.path.join(root, file)
            with open(log_file, "r", encoding="utf-8") as log:
                for line in log:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [item.strip() for item in line.split("|")]
                    if len(parts) != 4:
                        continue
                    try:
                        log_datetime = datetime.strptime(parts[0],"%d-%m-%Y %H:%M:%S")
                    except ValueError:
                        continue
                    if start_date and end_date:
                        if not (start_date <= log_datetime <= end_date):
                            continue
                    records.append({
                        "Date": parts[0],
                        "Module": module,
                        "Severity Level": parts[1],
                        "Status": parts[2],
                        "Remark": parts[3]
                    })
    return records


def generate_csv_report():
    logger = get_logger("generate_csv_report")
    start_date, end_date = get_date_range()
    records = _read_logs(start_date, end_date)
    if not records:
        print("\nNo records found.")
        logger.info(f"No records found. | {start_date.strftime('%d-%m-%Y')}-{end_date.strftime('%d-%m-%Y')}")
        return
    os.makedirs(CSV_FOLDER, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if start_date and end_date:
        filename = (
            f"{start_date.strftime('%d-%m-%Y')}"
            f"_to_"
            f"{end_date.strftime('%d-%m-%Y')}"
            f"_{timestamp}.csv"
        )
    else:
        filename = f"{timestamp}.csv"
    report_path = os.path.join(CSV_FOLDER, filename)
    with open(report_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=["Date","Module","Severity Level","Status","Remark"]
        )
        writer.writeheader()
        writer.writerows(records)
    print("\nCSV Report Generated Successfully.")
    logger.info(f"CSV Report Generated Successfully. | {report_path}")
    print(report_path)
    os.startfile(report_path)

def generate_json_report():
    logger = get_logger("generate_json_report")
    start_date, end_date = get_date_range()
    records = _read_logs(start_date, end_date)
    if not records:
        print("\nNo records found.")
        logger.info(f"No records found. | {start_date.strftime('%d-%m-%Y')}-{end_date.strftime('%d-%m-%Y')}")
        return
    os.makedirs(JSON_FOLDER, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if start_date and end_date:
        filename = (
            f"{start_date.strftime('%d-%m-%Y')}"
            f"_to_"
            f"{end_date.strftime('%d-%m-%Y')}"
            f"_{timestamp}.json"
        )
    else:
        filename = f"{timestamp}.json"
    report_path = os.path.join(JSON_FOLDER, filename)
    with open(report_path, "w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=4)
    print("\nJSON Report Generated Successfully.")
    logger.info(f"JSON Report Generated Successfully. | {report_path}")
    print(report_path)
    os.startfile(report_path)