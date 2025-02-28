"""
Есть две целевые функции:
user_interface — представляет собой работу графического интерфейса пользователя;
task — представляет собой расчетные задачи.
Напишите код, позволяющий выполнять эти две целевые задачи одновременно (псевдо одновременно, используя два потока).

Если бы в тестирующей системе были следующие простые определения:
 def user_interface():
    while True:
        sleep(0.2)
        print("-", end="")


def task():
    while True:
        sleep(0.61)
        print("*", end="")


import threading


# Ваше решение
то вследствие выполнения двух потоков выводилась строка вида: ---*---*---* и т.д

Копировать в свое решение или переписывать целевые функции не надо!
Они определены в тестирующей системе.
"""

from time import sleep


def user_interface():
    while True:
        sleep(0.2)
        print("-", end="")


def task():
    while True:
        sleep(0.61)
        print("*", end="")


import threading


threading.Thread(target=user_interface, name="Thread_1").start()
threading.Thread(target=task, name="Thread_2").start()
