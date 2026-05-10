def fcfs(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    gantt_chart =[]

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        start_time = current_time
        completion_time = start_time + p.burst_time

        gantt_chart.append({"id": f"P{p.pid}", "start": start_time, "end": completion_time, "color": p.color})

        p.completion_time = completion_time
        p.turnaround_time = completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        current_time = completion_time

    return processes, gantt_chart

def sjf(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    completed =[]
    ready_queue = []
    remaining = processes.copy()
    gantt_chart =[]

    while remaining or ready_queue:
        for p in remaining[:]:
            if p.arrival_time <= current_time:
                ready_queue.append(p)
                remaining.remove(p)

        if not ready_queue:
            current_time += 1
            continue

        ready_queue.sort(key=lambda p: p.burst_time)
        p = ready_queue.pop(0)

        start_time = current_time
        completion_time = start_time + p.burst_time

        gantt_chart.append({"id": f"P{p.pid}", "start": start_time, "end": completion_time, "color": p.color})

        p.completion_time = completion_time
        p.turnaround_time = completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        completed.append(p)
        current_time = completion_time

    return completed, gantt_chart

def priority_scheduling(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    completed = []
    ready_queue =[]
    remaining = processes.copy()
    gantt_chart = []

    while remaining or ready_queue:
        for p in remaining[:]:
            if p.arrival_time <= current_time:
                ready_queue.append(p)
                remaining.remove(p)

        if not ready_queue:
            current_time += 1
            continue

        ready_queue.sort(key=lambda p: (p.priority, p.arrival_time))
        p = ready_queue.pop(0)

        start_time = current_time
        completion_time = start_time + p.burst_time

        gantt_chart.append({"id": f"P{p.pid}", "start": start_time, "end": completion_time, "color": p.color})

        p.completion_time = completion_time
        p.turnaround_time = completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        completed.append(p)
        current_time = completion_time

    return completed, gantt_chart