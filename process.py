class Process:
    def __init__(self, pid, arrival_time, burst_time, color="#000"):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.color = color

    def __repr__(self):
        return f"Process(pid={self.pid}, AT={self.arrival_time}, BT={self.burst_time})"