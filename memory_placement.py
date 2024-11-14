def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    print_allocation("First Fit", allocation, processes)

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    print_allocation("Best Fit", allocation, processes)

def next_fit(blocks, processes):
    allocation = [-1] * len(processes)
    j = 0  # Start from the first block and move to the next
    for i in range(len(processes)):
        count = 0
        while count < len(blocks):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
            j = (j + 1) % len(blocks)
            count += 1
    print_allocation("Next Fit", allocation, processes)

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]
    print_allocation("Worst Fit", allocation, processes)

def print_allocation(strategy, allocation, processes):
    print(f"\n{strategy} Allocation:")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i+1} of size {processes[i]} allocated to block {allocation[i] + 1}")
        else:
            print(f"Process {i+1} of size {processes[i]} could not be allocated")

# Example values
blocks = [100, 500, 200, 300, 600]  # Memory block sizes
processes = [212, 417, 112, 426]     # Process sizes

print("Initial Block Sizes:", blocks)
print("Process Sizes:", processes)

# Make copies of blocks for each strategy to avoid interference
first_fit(blocks[:], processes)
best_fit(blocks[:], processes)
next_fit(blocks[:], processes)
worst_fit(blocks[:], processes)
def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    print_allocation("First Fit", allocation, processes)

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    print_allocation("Best Fit", allocation, processes)

def next_fit(blocks, processes):
    allocation = [-1] * len(processes)
    j = 0  # Start from the first block and move to the next
    for i in range(len(processes)):
        count = 0
        while count < len(blocks):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
            j = (j + 1) % len(blocks)
            count += 1
    print_allocation("Next Fit", allocation, processes)

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]
    print_allocation("Worst Fit", allocation, processes)

def print_allocation(strategy, allocation, processes):
    print(f"\n{strategy} Allocation:")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i+1} of size {processes[i]} allocated to block {allocation[i] + 1}")
        else:
            print(f"Process {i+1} of size {processes[i]} could not be allocated")

# Example values
blocks = [100, 500, 200, 300, 600]  # Memory block sizes
processes = [212, 417, 112, 426]     # Process sizes

print("Initial Block Sizes:", blocks)
print("Process Sizes:", processes)

# Make copies of blocks for each strategy to avoid interference
first_fit(blocks[:], processes)
best_fit(blocks[:], processes)
next_fit(blocks[:], processes)
worst_fit(blocks[:], processes)
