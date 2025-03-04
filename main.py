import threading
from time import sleep
from itertools import count

count = count()

def trace_func(frame, event, arg):
    print(f"{next(count)} executing trace func with {threading.current_thread().name=}")
    print(f"{frame=}\n{event=}\n{arg=}")

def get_inform():
    print(f"{threading.current_thread().name=}")
    print(f"{threading.current_thread().ident=}")
    print(f"{threading.current_thread().native_id=}")
    print(f"{threading.get_ident()=}")
    print(f"{threading.get_native_id()=}")
    print("---------------")
    sleep(2)

threading.settrace(trace_func)

thr = [threading.Thread(target=get_inform) for _ in range(1)]
for t in thr:
    t.start()

