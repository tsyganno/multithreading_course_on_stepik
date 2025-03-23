"""
Дополните Ваше предыдущее решение прошлой задачи согласно дополнительным условиям:

Целевая задача должна выполнять три функции в три этапа, разделенные двумя барьерами. Вторая функция должна вызываться только после успешного выполнения первой функции всеми потоками-участниками.
Функция финализатора finalizer должна быть вызвана дважды: первый раз при успешном выполнении первой функции task_stage1 всеми потоками-участниками.  Второй раз — при успешном выполнении второй функции task_stage2 всеми потоками-участниками. Финализатор должен вызываться последним потоком-участником этапа, который вызвал wait.
Последним потоком-участником, который последний преодолевает барьер (последний выходит из блокирующего метода wait) необходимо вызвать функцию shutdown, которая является завершающей функцией целевой задачи.
Все остальные условия прошлой задачи остаются в силе.

Функция shutdown заранее определена в тестирующей системе. Не изменяйте ее.

Если бы в тестирующей системе были вот такие простые определения:


import time
import random


def shutdown():
    print(f"ALL DONE! by {threading.current_thread().name}")


def finalizer():
    print(f"STAGE DONE! by {threading.current_thread().name}")


def task_stage1():
    time.sleep(random.uniform(0, 1))
    print(f"stage #1 done by {threading.current_thread().name}")


def task_stage2():
    time.sleep(random.uniform(0, 1))
    print(f"stage #2 done by {threading.current_thread().name}")

#  Ваше решение:

import threading

# Создайте объект барьера
# Создайте целевую функцию
# Создайте и запустите 4 потока
то в результате решения должен быть аналогичный вывод:

stage #1 done by Thread #4
stage #1 done by Thread #1
stage #1 done by Thread #3
stage #1 done by Thread #2
STAGE DONE! by Thread #2
stage #2 done by Thread #1
stage #2 done by Thread #4
stage #2 done by Thread #2
stage #2 done by Thread #3
STAGE DONE! by Thread #3
ALL DONE! by Thread #1
"""

import threading

# Создайте объект барьера
barrier = threading.Barrier(4, action=finalizer)


# Создайте целевую функцию
def task():
    task_stage1()
    barrier.wait()
    task_stage2()
    try:
        if barrier.wait() == 0:
            shutdown()
    except threading.BrokenBarrierError:
        pass


# Создайте и запустите 4 потока c требуемыми именами
for i in range(4):
    threading.Thread(target=task, name=f'Thread #{i + 1}').start()
    