import psutil
import datetime


CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80


LOG_FILE = "sample_log.txt"

def log_message(message):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{time_stamp} - {message}\n")
    print(f"{time_stamp} - {message}")

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        log_message(f"High CPU Usage Alert: {cpu}%")
    else:
        log_message(f"CPU Usage OK: {cpu}%")

def check_memory():
    mem = psutil.virtual_memory().percent
    if mem > MEM_THRESHOLD:
        log_message(f"High Memory Usage Alert: {mem}%")
    else:
        log_message(f"Memory Usage OK: {mem}%")

def check_disk():
    disk = psutil.disk_usage("/").percent
    if disk > DISK_THRESHOLD:
        log_message(f"High Disk Usage Alert: {disk}%")
    else:
        log_message(f"Disk Usage OK: {disk}%")

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()
