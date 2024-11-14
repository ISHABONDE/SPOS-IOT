import threading
import time
import random

BUFFER_SIZE = 5  # Size of the buffer
buffer = []  # Shared buffer between producer and consumer

# Semaphore to control the empty and full slots in the buffer
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

# Mutex to protect the shared buffer
mutex = threading.Lock()

def producer():
    global buffer
    while True:
        item = random.randint(1, 100)  # Generate a random item
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time to produce item
        empty.acquire()  # Wait if there is no empty space
        mutex.acquire()  # Lock the buffer while producing
        buffer.append(item)  # Add item to buffer
        print(f"Produced: {item}, Buffer: {buffer}")
        mutex.release()  # Release the lock after adding the item
        full.release()  # Signal that there is an item to consume

def consumer():
    global buffer
    while True:
        time.sleep(random.uniform(1, 2))  # Simulate time to consume item
        full.acquire()  # Wait if there is no item to consume
        mutex.acquire()  # Lock the buffer while consuming
        item = buffer.pop(0)  # Remove the item from the buffer
        print(f"Consumed: {item}, Buffer: {buffer}")
        mutex.release()  # Release the lock after consuming
        empty.release()  # Signal that there is space available

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
