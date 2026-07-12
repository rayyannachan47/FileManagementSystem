def get_choice(title, options, max_choice):
    while True:
        print(f"\n========== {title} ==========")
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("\nEnter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= max_choice:
                return choice
        print("\nInvalid Choice! Please enter a valid number.")

def main_menu():
    return get_choice(
        "FILE MANAGEMENT SYSTEM",
        {
            1: "File Operations",
            2: "Directory Operations",
            3: "Reports",
            4: "History",
            5: "System Health Check",
            6: "Exit"
        },
        6
    )

def file_menu():
    return get_choice(
        "FILE OPERATIONS",
        {
            1: "Create File",
            2: "Rename File",
            3: "Delete File",
            4: "Copy File",
            5: "Move File",
            6: "Search File",
            7: "Encrypt File",
            8: "Decrypt File",
            9: "Compress File",
            10: "Decompress File",
            11: "Back"
        },
        11
    )

def directory_menu():
    return get_choice(
        "DIRECTORY OPERATIONS",
        {
            1: "Create Directory",
            2: "Rename Directory",
            3: "Delete Directory",
            4: "Back"
        },
        4
    )

def report_menu():
    return get_choice(
        "REPORTS",
        {
            1: "Generate CSV Report",
            2: "Generate JSON Report",
            3: "Back"
        },
        3
    )

def history_menu():
    return get_choice(
        "HISTORY",
        {
            1: "File History",
            2: "Directory History",
            3: "Encryption History",
            4: "Compression History",
            5: "CSV Report",
            6: "JSON Report",
            7: "System Health Check Report",
            8: "Back"
        },
        8
    )

def system_health_menu():

    return get_choice(
        "SYSTEM HEALTH CHECK",
        {
            1: "System Information",
            2: "CPU Usage",
            3: "Memory Usage",
            4: "Disk Usage",
            5: "Network Information",
            6: "System Summary",
            7: "Back"
        },
        7
    )