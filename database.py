import sqlite3

def create_database():

    conn = sqlite3.connect("sysinsight.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        cpu REAL,
        ram REAL,
        disk REAL,
        health REAL
    )
    """)

    conn.commit()
    conn.close()


def save_metrics(cpu, ram, disk, health):

    conn = sqlite3.connect("sysinsight.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO metrics(cpu, ram, disk, health)
    VALUES(?,?,?,?)
    """, (cpu, ram, disk, health))

    conn.commit()
    conn.close()