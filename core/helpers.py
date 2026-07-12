from datetime import datetime
import os

def get_file_path(message):
    while True:
        path = input(message).strip()
        if path:
            return path
        print("Input cannot be empty.")

def get_directory_path(message):
    while True:
        path = input(message).strip()
        if os.path.isdir(path):
            return path
        print("Directory does not exist.")

def get_multiple_files():
    files = []
    while True:
        file_path = input("\nEnter file path (type 'exit' to finish): ").strip()
        if file_path.lower() == "exit":
            break
        files.append(file_path)
    return files

def get_date_range():
    while True:
        start_date = input("\nEnter Start Date (dd-mm-yyyy) [Press Enter for All]: ").strip()
        end_date = input("Enter End Date (dd-mm-yyyy) [Press Enter for All]: ").strip()
        if not start_date and not end_date:
            return None, None
        if not start_date or not end_date:
            print("\nPlease enter both dates.")
            continue
        try:
            start = datetime.strptime(start_date, "%d-%m-%Y")
            end = datetime.strptime(end_date, "%d-%m-%Y")
            if start > end:
                print("\nStart Date cannot be greater than End Date.")
                continue
            end = end.replace(
                hour=23,
                minute=59,
                second=59
            )
            return start, end
        except ValueError:
            print("\nInvalid date format. Please use dd-mm-yyyy.")