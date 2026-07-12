from menu import (main_menu,file_menu,directory_menu,report_menu,history_menu,system_health_menu)
from modules.compression import *
from modules.directory_manager import *
from modules.encryption import *
from modules.file_manager import *
from modules.report import *
from modules.search import *
from core.history import *
from modules.system_health import *

def file_operations():
    while True:
        choice = file_menu()
        if choice == 1:
            create_file()
        elif choice == 2:
            rename_file()
        elif choice == 3:
            delete_file()
        elif choice == 4:
            copy_file()
        elif choice == 5:
            move_file()
        elif choice == 6:
            search_file()
        elif choice == 7:
            encrypt_file()
        elif choice == 8:
            decrypt_file()
        elif choice == 9:
            compress_file()
        elif choice == 10:
            decompress_file()
        elif choice == 11:
            break
        else:
            print("\nInvalid Choice")

def directory_operations():
    while True:
        choice = directory_menu()
        if choice == 1:
            create_directory()
        elif choice == 2:
            rename_directory()
        elif choice == 3:
            delete_directory()
        elif choice == 4:
            break
        else:
            print("\nInvalid Choice")

def report_operations():
    while True:
        choice = report_menu()
        if choice == 1:
            generate_csv_report()
        elif choice == 2:
            generate_json_report()
        elif choice == 3:
            break
        else:
            print("\nInvalid Choice")

def history_operations():
    while True:
        choice = history_menu()
        if choice == 1:
            show_file_history()
        elif choice == 2:
            show_directory_history()
        elif choice == 3:
            show_encryption_history()
        elif choice == 4:
            show_compression_history()
        elif choice == 5:
            show_csv_history()
        elif choice == 6:
            show_json_history()
        elif choice == 7:
            show_system_health_history()
        elif choice == 8:
            break
        else:
            print("\nInvalid Choice")

def system_health_operations():

    while True:
        choice = system_health_menu()
        if choice == 1:
            system_information()
        elif choice == 2:
            cpu_usage()
        elif choice == 3:
            memory_usage()
        elif choice == 4:
            disk_usage()
        elif choice == 5:
            network_information()
        elif choice == 6:
            system_summary()
        elif choice == 7:
            break
        else:
            print("\nInvalid Choice")

def main():

    while True:
        choice = main_menu()
        if choice == 1:
            file_operations()
        elif choice == 2:
            directory_operations()
        elif choice == 3:
            report_operations()
        elif choice == 4:
            history_operations()
        elif choice == 5:
            system_health_operations()
        elif choice == 6:
            print("\nThank You...")
            break
        else:
            print("\nInvalid Choice")

if __name__ == "__main__":
    main()