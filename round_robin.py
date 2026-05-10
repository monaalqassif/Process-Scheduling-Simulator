from collections import deque

def rr(processes, quantum=2):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    queue = deque()
    current_time = 0
    remaining_burst = {p.pid: p.burst_time for p in processes}
    gantt_chart = []
    completed =[]
    visited = set()

    while len(completed) < len(processes):
        for p in processes:
            if p.arrival_time <= current_time and p.pid not in visited:
                queue.append(p)
                visited.add(p.pid)

        if not queue:
            current_time += 1
            continue

        p = queue.popleft()
        pid = p.pid

        exec_time = min(quantum, remaining_burst[pid])
        start_time = current_time
        current_time += exec_time
        remaining_burst[pid] -= exec_time

        gantt_chart.append({"id": f"P{pid}", "start": start_time, "end": current_time, "color": p.color})

        for new_p in processes:
            if start_time < new_p.arrival_time <= current_time and new_p.pid not in visited:
                queue.append(new_p)
                visited.add(new_p.pid)

        if remaining_burst[pid] == 0:
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed.append(p)
        else:
            queue.append(p)

    return completed, gantt_chart