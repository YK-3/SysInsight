import psutil

def get_top_processes():

    process_list = []

    for proc in psutil.process_iter(
        ['name', 'memory_percent']
    ):

        try:

            name = proc.info['name']

            if not name:
                continue

            mem = proc.info['memory_percent']

            process_list.append(
                (name, mem)
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    process_list.sort(
        key=lambda x: x[1],
        reverse=True
    )

    result = []

    for name, mem in process_list[:10]:

        result.append(
            f"{name:<30} {mem:.2f}%"
        )

    return result