from concurrent.futures import ThreadPoolExecutor
import threading
import time


def task(n):
    name = threading.current_thread().name
    s = n/10
    print(f"Поток {name} засыпает на {s} секунд")
    time.sleep(s)
    return f"Поток {name} завершился, проспал {s} секунд"


with ThreadPoolExecutor(max_workers=5) as pool:  # <- ?
    try:
        for r in pool.map(task, range(1, 11), timeout=0.55):
            print(r)
    except TimeoutError:
        print("Завершение по таймауту!")
