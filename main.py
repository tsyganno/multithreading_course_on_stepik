from time import sleep
from random import uniform
import threading


def task():
    work_time = uniform(0.1, 2)  # рандомное значение от 0.1 до 2 секунд
    sleep(work_time)
    print(f"task worked {work_time:.5f}")


threads = []
for _ in range(50):
    thread = threading.Thread(target=task, daemon=True)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join(0.01)






