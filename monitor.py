import psutil

def get_metrics():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('C:\\').percent

    net = psutil.net_io_counters()

    return {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "sent": net.bytes_sent,
        "received": net.bytes_recv
    }