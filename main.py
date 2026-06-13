from monitor import get_metrics

print("\n===== SysInsight =====\n")

data = get_metrics()

print(f"CPU Usage       : {data['cpu']} %")
print(f"RAM Usage       : {data['ram']} %")
print(f"Disk Usage      : {data['disk']} %")
print(f"Bytes Sent      : {data['sent']}")
print(f"Bytes Received  : {data['received']}")