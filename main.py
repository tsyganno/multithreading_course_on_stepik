import threading
import time

_block, _timer, _value = False, 0, 0


def task(sema: threading.Semaphore, text):
    s = sema.acquire(blocking=_block, timeout=_timer)
    print(f"thread id = {threading.current_thread().ident} print {text}, acquire={s}, value= {sema._value}")
    time.sleep(1)
    sema.release()


semaphore = threading.Semaphore(_value)

thr = []
for i in range(20):
    thr.append(threading.Thread(target=task, args=(semaphore, i)))
for t in thr:
    t.start()
for t in thr:
    t.join()

print(semaphore._value)

