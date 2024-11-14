def round_robin(processes, quantum):
    print("\nRound Robin Scheduling (Preemptive):")
    n = len(processes)
    remaining_burst_times = [process[2] for process in processes]  # remaining burst time for each process
    waiting_time = [0] * n  # waiting time for each process
    turnaround_time = [0] * n  # turnaround time for each process
    current_time = 0  # current time
    queue = []  # queue to hold processes
    idx = 0  # index for processes

    # While there are processes remaining to be executed
    while True:
        all_done = True  # flag to check if all processes are done
        for i in range(n):
            pid, arrival, burst = processes[i]
            if remaining_burst_times[i] > 0:  # if the process is still not finished
                all_done = False
                queue.append(i)  # add process to the queue

        if all_done:
            break  # break if all processes are finished

        # Run processes in the queue for the time quantum
        for i in queue:
            if remaining_burst_times[i] > 0:
                pid, arrival, burst = processes[i]
                time_to_run = min(remaining_burst_times[i], quantum)
                remaining_burst_times[i] -= time_to_run
                current_time += time_to_run

                # If the process finishes
                if remaining_burst_times[i] == 0:
                    waiting_time[i] = current_time - arrival - burst
                    turnaround_time[i] = current_time - arrival
                    print(f"Process {pid}: Waiting Time = {waiting_time[i]}, Turnaround Time = {turnaround_time[i]}")

        queue.clear()  # Clear the queue for the next round

    # Calculate the average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print(f"Average Waiting Time (Round Robin): {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time (Round Robin): {avg_turnaround_time:.2f}")


# Example usage:

# Format: [Process ID, Arrival Time, Burst Time]
processes_rr = [
    [1, 0, 4],  # Process 1: Arrival Time = 0, Burst Time = 4
    [2, 1, 3],  # Process 2: Arrival Time = 1, Burst Time = 3
    [3, 2, 2],  # Process 3: Arrival Time = 2, Burst Time = 2
    [4, 3, 1]   # Process 4: Arrival Time = 3, Burst Time = 1
]

quantum = 2  # Time quantum for Round Robin
round_robin(processes_rr, quantum)
