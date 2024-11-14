from queue import PriorityQueue

# FCFS Scheduling
def fcfs(processes):
    print("\nFirst-Come, First-Serve (FCFS) Scheduling:")
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    current_time = 0
    total_waiting_time = 0
    for pid, arrival, burst in processes:
        if current_time < arrival:
            current_time = arrival
        waiting_time = current_time - arrival
        total_waiting_time += waiting_time
        print(f"Process {pid}: Waiting Time = {waiting_time}, Turnaround Time = {waiting_time + burst}")
        current_time += burst
    print(f"Average Waiting Time (FCFS): {total_waiting_time / len(processes):.2f}")
    
    # SJF (Non-Preemptive) Scheduling
def sjf_non_preemptive(processes):
    print("\nShortest Job First (Non-Preemptive) Scheduling:")
    processes = processes.copy()  # Copy the list to avoid emptying the original
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    ready_queue = []
    current_time = 0
    total_waiting_time = 0
    num_processes = len(processes)  # Store the original number of processes

    while processes or ready_queue:
        while processes and processes[0][1] <= current_time:
            ready_queue.append(processes.pop(0))
        ready_queue.sort(key=lambda x: x[2])  # Sort by burst time for SJF

        if ready_queue:
            pid, arrival, burst = ready_queue.pop(0)
            waiting_time = current_time - arrival
            total_waiting_time += waiting_time
            print(f"Process {pid}: Waiting Time = {waiting_time}, Turnaround Time = {waiting_time + burst}")
            current_time += burst
        else:
            current_time = processes[0][1] if processes else current_time

    print(f"Average Waiting Time (SJF Non-Preemptive): {total_waiting_time / num_processes:.2f}")





# SJF (Preemptive) Scheduling
def sjf_preemptive(processes):
    print("\nShortest Job First (Preemptive) Scheduling:")
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    remaining_burst = {pid: burst for pid, arrival, burst in processes}
    current_time = 0
    completed = 0
    total_waiting_time = 0
    ready_queue = PriorityQueue()
    i = 0

    while completed < len(processes):
        while i < len(processes) and processes[i][1] <= current_time:
            ready_queue.put((remaining_burst[processes[i][0]], processes[i][0], processes[i][1]))
            i += 1

        if not ready_queue.empty():
            burst, pid, arrival = ready_queue.get()
            remaining_burst[pid] -= 1
            current_time += 1

            if remaining_burst[pid] == 0:
                completed += 1
                waiting_time = current_time - arrival - burst
                total_waiting_time += waiting_time
                print(f"Process {pid}: Waiting Time = {waiting_time}, Turnaround Time = {waiting_time + burst}")
            else:
                ready_queue.put((remaining_burst[pid], pid, arrival))
        else:
            current_time += 1

    print(f"Average Waiting Time (SJF Preemptive): {total_waiting_time / len(processes):.2f}")

# Priority Scheduling (Non-Preemptive)
def priority_non_preemptive(processes):
    print("\nPriority Scheduling (Non-Preemptive):")
    processes = processes.copy()  # Copy the list to avoid modifying the original list
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time, then priority
    ready_queue = []
    current_time = 0
    total_waiting_time = 0
    num_processes = len(processes)  # Store the original number of processes

    while processes or ready_queue:
        while processes and processes[0][1] <= current_time:
            ready_queue.append(processes.pop(0))
        ready_queue.sort(key=lambda x: x[3])  # Sort by priority for non-preemptive

        if ready_queue:
            pid, arrival, burst, priority = ready_queue.pop(0)
            waiting_time = current_time - arrival
            total_waiting_time += waiting_time
            print(f"Process {pid}: Waiting Time = {waiting_time}, Turnaround Time = {waiting_time + burst}")
            current_time += burst
        else:
            current_time = processes[0][1] if processes else current_time

    print(f"Average Waiting Time (Priority Non-Preemptive): {total_waiting_time / num_processes:.2f}")


# Priority Scheduling (Preemptive)
def priority_preemptive(processes):
    print("\nPriority Scheduling (Preemptive):")
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time, then priority
    remaining_burst = {pid: burst for pid, arrival, burst, priority in processes}
    current_time = 0
    completed = 0
    total_waiting_time = 0
    ready_queue = PriorityQueue()
    i = 0

    while completed < len(processes):
        while i < len(processes) and processes[i][1] <= current_time:
            ready_queue.put((processes[i][3], processes[i][0], processes[i][1], processes[i][2]))
            i += 1

        if not ready_queue.empty():
            priority, pid, arrival, burst = ready_queue.get()
            remaining_burst[pid] -= 1
            current_time += 1

            if remaining_burst[pid] == 0:
                completed += 1
                waiting_time = current_time - arrival - burst
                total_waiting_time += waiting_time
                print(f"Process {pid}: Waiting Time = {waiting_time}, Turnaround Time = {waiting_time + burst}")
            else:
                ready_queue.put((priority, pid, arrival, remaining_burst[pid]))
        else:
            current_time += 1

    print(f"Average Waiting Time (Priority Preemptive): {total_waiting_time / len(processes):.2f}")


# Round Robin Scheduling
def round_robin(processes, quantum):
    print("\nRound Robin Scheduling:")
    current_time = 0
    waiting_time = {}
    remaining_burst = {}
    arrival_time = {}

    for pid, arrival, burst in processes:
        remaining_burst[pid] = burst
        arrival_time[pid] = arrival
        waiting_time[pid] = 0

    ready_queue = [p for p in processes if p[1] <= current_time]
    completed = 0

    while completed < len(processes):
        for i, (pid, arrival, burst) in enumerate(ready_queue):
            if remaining_burst[pid] > 0:
                execute_time = min(remaining_burst[pid], quantum)
                remaining_burst[pid] -= execute_time
                current_time += execute_time

                if remaining_burst[pid] == 0:
                    completed += 1
                    waiting_time[pid] = current_time - arrival - burst
                    print(f"Process {pid}: Waiting Time = {waiting_time[pid]}, Turnaround Time = {waiting_time[pid] + burst}")
            else:
                continue

        ready_queue = [p for p in processes if p[1] <= current_time and remaining_burst[p[0]] > 0]

    avg_waiting_time = sum(waiting_time.values()) / len(processes)
    print(f"Average Waiting Time (Round Robin): {avg_waiting_time:.2f}")


# Test data
processes_fcfs = [(1, 0, 5), (2, 2, 3), (3, 4, 1), (4, 6, 2)]
processes_sjf_np = [(1, 0, 6), (2, 2, 8), (3, 4, 7), (4, 6, 3)]
processes_sjf_p = [(1, 0, 6), (2, 2, 8), (3, 4, 7), (4, 6, 3)]
processes_priority_np = [(1, 0, 5, 2), (2, 2, 3, 1), (3, 4, 4, 3), (4, 6, 2, 4)]
processes_priority_p = [(1, 0, 5, 2), (2, 2, 3, 1), (3, 4, 4, 3), (4, 6, 2, 4)]
processes_rr = [(1, 0, 5), (2, 1, 3), (3, 2, 8), (4, 3, 6)]
quantum = 2

# Run each scheduling algorithm
fcfs(processes_fcfs)
sjf_non_preemptive(processes_sjf_np)
sjf_preemptive(processes_sjf_p)
priority_non_preemptive(processes_priority_np)
priority_preemptive(processes_priority_p)
