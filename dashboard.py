import customtkinter as ctk
import psutil
import platform
import socket
from datetime import datetime

from health import calculate_health
from process_analyzer import get_top_processes

from database import create_database
from database import save_metrics

# =====================================
# Theme
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# Window
# =====================================

app = ctk.CTk()

create_database()

app.title("SysInsight")
app.geometry("1200x850")

# =====================================
# Header
# =====================================

title = ctk.CTkLabel(
    app,
    text="🖥 SysInsight",
    font=("Arial", 36, "bold")
)
title.pack(pady=(15, 5))

subtitle = ctk.CTkLabel(
    app,
    text="AI-Powered System Monitoring and Resource Prediction Platform",
    font=("Arial", 18)
)
subtitle.pack()

time_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14)
)
time_label.pack(pady=10)

# =====================================
# Metric Cards
# =====================================

cards_frame = ctk.CTkFrame(app)
cards_frame.pack(pady=10)

# CPU Card

cpu_card = ctk.CTkFrame(cards_frame, width=250, height=120)
cpu_card.grid(row=0, column=0, padx=15, pady=10)

ctk.CTkLabel(
    cpu_card,
    text="CPU Usage",
    font=("Arial", 18, "bold")
).pack(pady=(15, 5))

cpu_value = ctk.CTkLabel(
    cpu_card,
    text="0%",
    font=("Arial", 28)
)
cpu_value.pack()

# RAM Card

ram_card = ctk.CTkFrame(cards_frame, width=250, height=120)
ram_card.grid(row=0, column=1, padx=15, pady=10)

ctk.CTkLabel(
    ram_card,
    text="RAM Usage",
    font=("Arial", 18, "bold")
).pack(pady=(15, 5))

ram_value = ctk.CTkLabel(
    ram_card,
    text="0%",
    font=("Arial", 28)
)
ram_value.pack()

# Disk Card

disk_card = ctk.CTkFrame(cards_frame, width=250, height=120)
disk_card.grid(row=0, column=2, padx=15, pady=10)

ctk.CTkLabel(
    disk_card,
    text="Disk Usage",
    font=("Arial", 18, "bold")
).pack(pady=(15, 5))

disk_value = ctk.CTkLabel(
    disk_card,
    text="0%",
    font=("Arial", 28)
)
disk_value.pack()

# Network Card

network_card = ctk.CTkFrame(cards_frame, width=250, height=120)
network_card.grid(row=0, column=3, padx=15, pady=10)

ctk.CTkLabel(
    network_card,
    text="Network",
    font=("Arial", 18, "bold")
).pack(pady=(15, 5))

network_value = ctk.CTkLabel(
    network_card,
    text="0 MB",
    font=("Arial", 28)
)
network_value.pack()

# =====================================
# Health Score
# =====================================

health_label = ctk.CTkLabel(
    app,
    text="100%",
    font=("Arial", 52, "bold")
)
health_label.pack(pady=(15, 0))

health_text = ctk.CTkLabel(
    app,
    text="System Health Score",
    font=("Arial", 18)
)
health_text.pack()

status_label = ctk.CTkLabel(
    app,
    text="● HEALTHY",
    font=("Arial", 24, "bold"),
    text_color="#00cc44"
)
status_label.pack(pady=10)

# =====================================
# Content Area
# =====================================

content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True, padx=20, pady=15)

# Left Side

left_frame = ctk.CTkFrame(content_frame)
left_frame.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(
    left_frame,
    text="System Information",
    font=("Arial", 20, "bold")
).pack(pady=10)

system_info = ctk.CTkTextbox(
    left_frame,
    width=400,
    height=250
)
system_info.pack(padx=10, pady=10)

# Right Side

right_frame = ctk.CTkFrame(content_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=10)

ctk.CTkLabel(
    right_frame,
    text="Top Processes",
    font=("Arial", 20, "bold")
).pack(pady=10)

process_box = ctk.CTkTextbox(
    right_frame,
    width=500,
    height=250
)
process_box.pack(padx=10, pady=10)

# =====================================
# Footer
# =====================================

footer = ctk.CTkLabel(
    app,
    text="SysInsight v1.0",
    font=("Arial", 12)
)
footer.pack(pady=10)

# =====================================
# Update Dashboard
# =====================================

def get_color(value):

    if value < 50:
        return "green"
    elif value < 80:
        return "orange"
    return "red"


def update_dashboard():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent

    net = psutil.net_io_counters()

    upload = round(net.bytes_sent / (1024 * 1024), 2)
    download = round(net.bytes_recv / (1024 * 1024), 2)

    health = calculate_health(cpu, ram, disk)

    save_metrics(
    cpu,
    ram,
    disk,
    health
    )

    current_time = datetime.now().strftime(
        "%d-%b-%Y %H:%M:%S"
    )

    time_label.configure(text=current_time)

    # Cards

    cpu_value.configure(
        text=f"{cpu:.1f}%",
        text_color=get_color(cpu)
    )

    ram_value.configure(
        text=f"{ram:.1f}%",
        text_color=get_color(ram)
    )

    disk_value.configure(
        text=f"{disk:.1f}%",
        text_color=get_color(disk)
    )

    network_value.configure(
        text=f"{download:.0f} MB"
    )

    # Health

    health_label.configure(
        text=f"{health:.2f}%"
    )

    if health >= 80:

        status_label.configure(
            text="● HEALTHY",
            text_color="#00cc44"
        )

    elif health >= 60:

        status_label.configure(
            text="● WARNING",
            text_color="orange"
        )

    else:

        status_label.configure(
            text="● CRITICAL",
            text_color="red"
        )

    # System Info

    system_info.delete("1.0", "end")

    system_info.insert(
        "end",
        f"""
Hostname      : {socket.gethostname()}

OS            : {platform.system()} {platform.release()}

Processor     : {platform.processor()}

CPU Cores     : {psutil.cpu_count(logical=False)}

Threads       : {psutil.cpu_count()}

Total RAM     :
{round(psutil.virtual_memory().total/(1024**3),2)} GB

Available RAM :
{round(psutil.virtual_memory().available/(1024**3),2)} GB

Network Sent  :
{upload} MB

Network Recv  :
{download} MB
"""
    )

    # Top Processes

    process_box.delete("1.0", "end")

    process_box.insert(
        "end",
        f"{'Process Name':<30} Memory%\n"
    )

    process_box.insert(
        "end",
        "-" * 45 + "\n"
    )

    for proc in get_top_processes():
        process_box.insert("end", proc + "\n")

    app.after(2000, update_dashboard)


# =====================================
# Start
# =====================================

update_dashboard()

app.mainloop()