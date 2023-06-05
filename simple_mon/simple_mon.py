import time
import csv
import psutil
import os

INTERVAL = 10  # Interval in seconds

# initialize disk_io and net_io globally
start_disk_io = psutil.disk_io_counters()
start_net_io = psutil.net_io_counters()

def get_cpu_load():
    return psutil.cpu_percent(interval=None)

def get_disk_io():
    global start_disk_io

    # Get disk io counters, sum up bytes read and written
    end_disk_io = psutil.disk_io_counters()

    # Calculate the difference in read and write operations
    read_diff = end_disk_io.read_bytes - start_disk_io.read_bytes
    write_diff = end_disk_io.write_bytes - start_disk_io.write_bytes

    # Update start_disk_io
    start_disk_io = end_disk_io

    return read_diff / INTERVAL, write_diff / INTERVAL

def get_memory_usage():
    mem = psutil.virtual_memory()
    return (mem.total, mem.used, mem.available, mem.percent)

def get_network_load():
    global start_net_io

    # Get net io counters, sum up bytes sent and received
    end_net_io = psutil.net_io_counters()

    # Calculate the difference in bytes sent and received
    sent_diff = end_net_io.bytes_sent - start_net_io.bytes_sent
    recv_diff = end_net_io.bytes_recv - start_net_io.bytes_recv

    # Update start_net_io
    start_net_io = end_net_io

    return sent_diff / INTERVAL, recv_diff / INTERVAL

def log_metrics():
    cpu_load = get_cpu_load()
    disk_read, disk_write = get_disk_io()
    sent, recv = get_network_load()
    memory_usage = get_memory_usage()

    with open('system_metrics.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time.ctime(), cpu_load, sent, recv, disk_read, disk_write]+ list(memory_usage))

def main():
    if not os.path.isfile('system_metrics.csv'):
        with open('system_metrics.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'CPU Load', 'Network Sent (bytes/sec)', 'Network Received (bytes/sec)', 'Disk Read (bytes/sec)', 'Disk Write (bytes/sec)', 'Total Memory', 'Used Memory', 'Available Memory', 'Percent Memory Used'])

    while True:
        log_metrics()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
    
