def calculate_health(cpu, ram, disk):

    score = 100

    score -= cpu * 0.2
    score -= ram * 0.15
    score -= disk * 0.05

    return round(max(score, 0), 2)