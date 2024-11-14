import threading
import time

# Number of philosophers
N = 5

# Semaphore for the forks (each fork can be used by one philosopher at a time)
forks = [threading.Semaphore(1) for _ in range(N)]

# Philosopher function
def philosopher(i):
    while True:
        # Thinking
        print(f"Philosopher {i} is thinking.")
        time.sleep(2)  # Thinking for 2 seconds

        # Trying to pick up both forks (if available)
        forks[i].acquire()  # Pick up the left fork
        forks[(i + 1) % N].acquire()  # Pick up the right fork

        # Eating
        print(f"Philosopher {i} is eating.")
        time.sleep(2)  # Eating for 2 seconds

        # Putting down both forks
        forks[i].release()  # Put down the left fork
        forks[(i + 1) % N].release()  # Put down the right fork

# Create philosopher threads
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# Join all threads
for t in threads:
    t.join()
