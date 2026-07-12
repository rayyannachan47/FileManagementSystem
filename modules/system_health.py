import platform
import socket
import getpass
import psutil
import uuid
from datetime import datetime
from core.logger import *

def get_health_status(value, healthy_limit, warning_limit):
    if value <= healthy_limit:
        return "Healthy"
    elif value <= warning_limit:
        return "Warning"
    return "Critical"

def system_information():
    try:
        logger = get_logger("system_information")
        print("\n" + "=" * 60)
        print("SYSTEM INFORMATION".center(60))
        print("=" * 60)
        computer_name = socket.gethostname()
        username = getpass.getuser()
        operating_system = platform.system()
        os_version = platform.version()
        release = platform.release()
        architecture = platform.architecture()[0]
        machine = platform.machine()
        processor = platform.processor()
        python_version = platform.python_version()
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        current_time = datetime.now()
        print(f"{'Computer Name':<20}: {computer_name}")
        print(f"{'Username':<20}: {username}")
        print(f"{'Operating System':<20}: {operating_system}")
        print(f"{'OS Version':<20}: {os_version}")
        print(f"{'Release':<20}: {release}")
        print(f"{'Architecture':<20}: {architecture}")
        print(f"{'Machine':<20}: {machine}")
        print(f"{'Processor':<20}: {processor}")
        print(f"{'Python Version':<20}: {python_version}")
        print(f"{'Boot Time':<20}: {boot_time.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"{'Current Time':<20}: {current_time.strftime('%d-%m-%Y %H:%M:%S')}")
        print("=" * 60)
        system_info = (
            f"Computer Name: {computer_name}, "
            f"Username: {username}, "
            f"OS: {operating_system}, "
            f"Version: {os_version}, "
            f"Release: {release}, "
            f"Architecture: {architecture}, "
            f"Machine: {machine}, "
            f"Processor: {processor}, "
            f"Python: {python_version}, "
            f"Boot Time: {boot_time:%d-%m-%Y %H:%M:%S}, "
            f"Current Time: {current_time:%d-%m-%Y %H:%M:%S}"
        )
        logger.info(f"System Information Retrieved | {system_info}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve system information.")

def cpu_usage():
    try:
        logger = get_logger("cpu_usage")
        print("\n" + "=" * 60)
        print("CPU INFORMATION".center(60))
        print("=" * 60)
        usage = psutil.cpu_percent(interval=1)
        physical_cores = psutil.cpu_count(logical=False)
        logical_cores = psutil.cpu_count(logical=True)
        frequency = psutil.cpu_freq()
        current_frequency = frequency.current if frequency else 0
        minimum_frequency = frequency.min if frequency else 0
        maximum_frequency = frequency.max if frequency else 0
        if usage <= 60:
            status = "Healthy"
        elif usage <= 80:
            status = "Warning"
        else:
            status = "Critical"
        print(f"{'CPU Usage':<25}: {usage:.2f}%")
        print(f"{'Physical Cores':<25}: {physical_cores}")
        print(f"{'Logical Cores':<25}: {logical_cores}")
        print(f"{'Current Frequency':<25}: {current_frequency:.2f} MHz")
        print(f"{'Minimum Frequency':<25}: {minimum_frequency:.2f} MHz")
        print(f"{'Maximum Frequency':<25}: {maximum_frequency:.2f} MHz")
        print(f"{'Health Status':<25}: {status}")
        print("=" * 60)
        cpu_info = (
            f"CPU Usage: {usage:.2f}%, "
            f"Physical Cores: {physical_cores}, "
            f"Logical Cores: {logical_cores}, "
            f"Current Frequency: {current_frequency:.2f} MHz, "
            f"Minimum Frequency: {minimum_frequency:.2f} MHz, "
            f"Maximum Frequency: {maximum_frequency:.2f} MHz, "
            f"Health Status: {status}"
        )
        logger.info(f"CPU Information Retrieved | {cpu_info}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve CPU information.")

def memory_usage():
    try:
        logger = get_logger("memory_usage")
        print("\n" + "=" * 60)
        print("MEMORY INFORMATION".center(60))
        print("=" * 60)
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)
        used_memory = memory.used / (1024 ** 3)
        available_memory = memory.available / (1024 ** 3)
        memory_usage = memory.percent
        swap = psutil.swap_memory()
        total_swap = swap.total / (1024 ** 3)
        used_swap = swap.used / (1024 ** 3)
        free_swap = swap.free / (1024 ** 3)
        swap_usage = swap.percent
        if memory_usage <= 70:
            status = "Healthy"
        elif memory_usage <= 90:
            status = "Warning"
        else:
            status = "Critical"
        print(f"{'Total RAM':<25}: {total_memory:.2f} GB")
        print(f"{'Used RAM':<25}: {used_memory:.2f} GB")
        print(f"{'Available RAM':<25}: {available_memory:.2f} GB")
        print(f"{'Memory Usage':<25}: {memory_usage:.2f}%")
        print("-" * 60)
        print(f"{'Total Swap':<25}: {total_swap:.2f} GB")
        print(f"{'Used Swap':<25}: {used_swap:.2f} GB")
        print(f"{'Free Swap':<25}: {free_swap:.2f} GB")
        print(f"{'Swap Usage':<25}: {swap_usage:.2f}%")
        print("-" * 60)
        print(f"{'Health Status':<25}: {status}")
        print("=" * 60)
        memory_info = (
            f"Total RAM: {total_memory:.2f} GB, "
            f"Used RAM: {used_memory:.2f} GB, "
            f"Available RAM: {available_memory:.2f} GB, "
            f"Memory Usage: {memory_usage:.2f}%, "
            f"Total Swap: {total_swap:.2f} GB, "
            f"Used Swap: {used_swap:.2f} GB, "
            f"Free Swap: {free_swap:.2f} GB, "
            f"Swap Usage: {swap_usage:.2f}%, "
            f"Health Status: {status}"
        )
        logger.info(f"Memory Information Retrieved | {memory_info}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve memory information.")

def disk_usage():
    try:
        logger = get_logger("disk_usage")
        print("\n" + "=" * 60)
        print("DISK INFORMATION".center(60))
        print("=" * 60)
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                total_space = usage.total / (1024 ** 3)
                used_space = usage.used / (1024 ** 3)
                free_space = usage.free / (1024 ** 3)
                disk_usage = usage.percent
                if disk_usage <= 80:
                    status = "Healthy"
                elif disk_usage <= 90:
                    status = "Warning"
                else:
                    status = "Critical"
                print(f"Drive                     : {partition.device}")
                print(f"Mount Point               : {partition.mountpoint}")
                print(f"File System               : {partition.fstype}")
                print(f"Total Space               : {total_space:.2f} GB")
                print(f"Used Space                : {used_space:.2f} GB")
                print(f"Free Space                : {free_space:.2f} GB")
                print(f"Disk Usage                : {disk_usage:.2f}%")
                print(f"Health Status             : {status}")
                print("-" * 60)
                disk_info = (
                    f"Drive: {partition.device}, "
                    f"Mount Point: {partition.mountpoint}, "
                    f"File System: {partition.fstype}, "
                    f"Total Space: {total_space:.2f} GB, "
                    f"Used Space: {used_space:.2f} GB, "
                    f"Free Space: {free_space:.2f} GB, "
                    f"Disk Usage: {disk_usage:.2f}%, "
                    f"Health Status: {status}"
                )
                logger.info(f"Disk Information Retrieved | {disk_info}")
            except PermissionError as e:
                logger.error(f"Permission Error | {str(e)}")
                print("\nUnable to retrieve disk information.")
                continue
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve disk information.")

def network_information():
    try:
        logger = get_logger("network_information")
        print("\n" + "=" * 60)
        print("NETWORK INFORMATION".center(60))
        print("=" * 60)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        mac_address = ':'.join(f'{(uuid.getnode() >> element) & 0xff:02x}'for element in range(40, -1, -8)).upper()
        network = psutil.net_io_counters()
        bytes_sent = network.bytes_sent / (1024 ** 2)
        bytes_received = network.bytes_recv / (1024 ** 2)
        packets_sent = network.packets_sent
        packets_received = network.packets_recv
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            internet_status = "Connected"
        except OSError as e:
            internet_status = "Disconnected"
            logger.error(f"Internet Connection Error : {internet_status} | {str(e)}")
        print(f"{'Hostname':<25}: {hostname}")
        print(f"{'IP Address':<25}: {ip_address}")
        print(f"{'MAC Address':<25}: {mac_address}")
        print(f"{'Bytes Sent':<25}: {bytes_sent:.2f} MB")
        print(f"{'Bytes Received':<25}: {bytes_received:.2f} MB")
        print(f"{'Packets Sent':<25}: {packets_sent}")
        print(f"{'Packets Received':<25}: {packets_received}")
        print(f"{'Internet Status':<25}: {internet_status}")
        print("=" * 60)
        network_info = (
            f"Hostname: {hostname}, "
            f"IP Address: {ip_address}, "
            f"MAC Address: {mac_address}, "
            f"Bytes Sent: {bytes_sent:.2f} MB, "
            f"Bytes Received: {bytes_received:.2f} MB, "
            f"Packets Sent: {packets_sent}, "
            f"Packets Received: {packets_received}, "
            f"Internet Status: {internet_status}"
        )
        logger.info(f"Network Information Retrieved | {network_info}")

    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve network information.")

def system_summary():
    try:
        logger = get_logger("system_summary")
        print("\n" + "=" * 60)
        print("SYSTEM HEALTH SUMMARY".center(60))
        print("=" * 60)
        hostname = socket.gethostname()
        operating_system = f"{platform.system()} {platform.release()}"
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            internet = "Connected"
        except OSError:
            internet = "Disconnected"
        cpu_status = get_health_status(cpu, 60, 80)
        memory_status = get_health_status(memory, 70, 90)
        disk_status = get_health_status(disk, 80, 90)
        statuses = [cpu_status,memory_status,disk_status]
        if "Critical" in statuses:
            overall_status = "CRITICAL"
        elif "Warning" in statuses:
            overall_status = "WARNING"
        else:
            overall_status = "HEALTHY"
        print(f"{'Computer Name':<20}: {hostname}")
        print(f"{'Operating System':<20}: {operating_system}")
        print("-" * 60)
        print(f"{'CPU Usage':<20}: {cpu:.2f}% ({cpu_status})")
        print(f"{'Memory Usage':<20}: {memory:.2f}% ({memory_status})")
        print(f"{'Disk Usage':<20}: {disk:.2f}% ({disk_status})")
        print(f"{'Internet':<20}: {internet}")
        print("-" * 60)
        print(f"{'Overall Status':<20}: {overall_status}")
        print("=" * 60)
        health_summary = (
            f"Computer Name: {hostname}, "
            f"Operating System: {operating_system}, "
            f"CPU Usage: {cpu:.2f}% ({cpu_status}), "
            f"Memory Usage: {memory:.2f}% ({memory_status}), "
            f"Disk Usage: {disk:.2f}% ({disk_status}), "
            f"Internet Status: {internet}, "
            f"Overall Status: {overall_status}"
        )
        logger.info(f"System Health Summary Retrieved | {health_summary}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to retrieve system summary.")