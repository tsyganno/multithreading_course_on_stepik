import threading


def add(a, b):
    print(a + b)


thr = threading.Thread(target=add, args=(1, 2), name="new_name")
thr.start()

threading.Thread(target=add, args=(1, 2), name="new_name").start()
