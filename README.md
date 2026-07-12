# File Management System

A command-line based File Management System developed in Python for automating common file operations. The application provides file and directory management, compression, encryption, backup, report generation, and activity logging with history tracking.

This project is designed with a modular architecture and follows good coding practices such as code reusability, centralized logging, input validation, and separation of concerns.

## Features

### File Management
- Create File
- Move File
- Copy File
- Rename File
- Delete File

### Directory Management
- Create Directory
- Rename Directory
- Delete Directory

### Compression
- Compress Files/Folders into ZIP
- Decompress ZIP Files

### Encryption
- Encrypt Files using Fernet Encryption
- Decrypt Files

### Reports
- Generate CSV Report
- Generate JSON Report
- Date Range Filter
- Timestamp-based Report Generation

### History
- File History
- Directory History
- Compression History
- Encryption History
- CSV Report History
- JSON Report History
- Date Range Filter

### Logging
- Daily Log Generation
- Separate Log File for Each Module
- INFO and ERROR Level Logging
- Timestamped Logs

# Project Structure

FileManagementSystem/
│
├── config/
│   └── secret.key
│
├── core/
│   ├── constants.py
│   ├── helpers.py
│   ├── key_manager.py
│   ├── logger.py
│   └── validator.py
│
├── logs/
│   └── dd-mm-yyyy/
│       ├── create_file/
│       ├── move_file/
│       ├── copy_file/
│       ├── rename_file/
│       ├── delete_file/
│       ├── create_directory/
│       ├── rename_directory/
│       ├── delete_directory/
│       ├── compress_file/
│       ├── decompress_file/
│       ├── encrypt_file/
│       ├── decrypt_file/
│       ├── generate_csv_report/
│       └── generate_json_report/
│
├── modules/
│   ├── backup.py
│   ├── compression.py
│   ├── directory_manager.py
│   ├── encryption.py
│   ├── file_manager.py
│   ├── history.py
│   ├── report.py
│   └── search.py
│
├── reports/
│   ├── csv/
│   └── json/
│
├── main.py
├── menu.py
├── requirements.txt
└── README.md

# Technologies Used

- Python 3.13+
- os
- shutil
- pathlib
- csv
- json
- zipfile
- hashlib
- datetime
- logging
- cryptography (Fernet)

# Installation

Clone the repository

git clone <repository-url>

Go to project directory

cd FileManagementSystem

Install dependencies

pip install -r requirements.txt

Run the project

python main.py

# Menu Structure

MAIN MENU

1. File Management
2. Directory Management
3. Reports
4. History
5. System Health Check
6. Exit

# Logging Format

Every operation is logged with timestamp, severity level, status, and remarks.

Example

12-07-2026 03:36:23 | ERROR | Copy Failed | test.txt

12-07-2026 03:37:25 | INFO | Copied | E:\abc.txt -> E:\Videos

# Report Generation

The application generates reports directly from log files.

Supported formats

- CSV
- JSON

Users can

- Generate complete reports
- Generate reports within a selected date range
- Automatically create timestamp-based report files

Example filenames

20260712_151230.csv

10-07-2026_to_12-07-2026_20260712_151230.csv

20260712_151230.json

10-07-2026_to_12-07-2026_20260712_151230.json

# History Module

History is generated from log files and supports date filtering.

Available History

- File Operations
- Directory Operations
- Compression Operations
- Encryption Operations
- CSV Report Generation
- JSON Report Generation

# Security

Sensitive files are encrypted using Fernet Symmetric Encryption provided by the cryptography library.

A secret encryption key is automatically generated and stored inside
config/secret.key

# Error Handling

The application handles

- Invalid file paths
- Invalid directory paths
- Missing files
- Existing files/folders
- Invalid date format
- Invalid backup
- Invalid ZIP files
- Encryption/Decryption errors
- File permission errors

# Coding Standards

- Modular Architecture
- Code Reusability
- Separation of Concerns
- Centralized Logging
- Input Validation
- Exception Handling
- No Duplicate Code

# Future Enhancements

- File Search
- Directory Search
- Scheduled Backup
- Password-Protected ZIP Files
- Multi-user Authentication
- Configuration File Support
- GUI Version
- Database Logging

# Author

**Rayyan Nachan**

Software Developer

Python | PHP | Laravel