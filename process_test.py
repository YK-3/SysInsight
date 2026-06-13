from process_analyzer import get_top_processes

for proc in get_top_processes():

    print(
        proc["pid"],
        proc["name"],
        proc["cpu"],
        proc["memory"]
    )