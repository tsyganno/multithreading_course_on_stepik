"""
Напишите функцию отложенного запуска delayed_launch(initializer: Callable, task: Callable, permission: Callable), которая позволяет запускать задачу инициализатора initializer в отдельном потоке, периодически проверяет разрешение permission и, когда разрешение получено, запускает основную задачу task. Функции initializer, task, permission не принимают аргументов!

Функция должна:

Создавать и использовать примитив синхронизации Event.
Запускать рабочий поток, который выполняет (вызывает) функцию инициализатора initializer, а затем ждет разрешения (события Event), чтобы вызвать основную функцию task.
Запускать еще один контрольный поток, который в цикле вызывает функцию permission до тех пор, пока она не вернет True. Функция permission возвращает True, если разрешение получено, или False — если еще нет. Если разрешение получено, контрольный поток должен разрешить выполнить основную задачу рабочему потоку.
Функция не должна блокировать выполнение главного потока. Никаких join и прочих блокирующих операций. В delayed_launch создайте и запустите два дополнительных потока, которые должны выполнить остальную логику решения согласно заданию.

Напишите функцию согласно условию задания. Ваше решение, при необходимости, может включать в себя другие вспомогательные функции. Тестирующая система вызовет Вашу функцию с различными аргументами initializer, task, permission и проверит ее работу. Передаваемые в функцию delayed_launch в качестве аргументов initializer, task, permission будут определены в тестирующей системе.

Для возможности самостоятельной проверки перед сдачей решения можно использовать этот код:

import time
from itertools import count


_count = count(1)


def my_initializer():
    print("Вызов initializer\n", end="")


def my_task():
    print("Вызов task\n", end="")


def my_test_permission():
    time.sleep(1)
    i = next(_count)
    print(f"Вызов permission {i} раз\n", end="")
    return i >= 4


#----------Ваше решение
import threading
from typing import Callable


# Создайте дополнительные функции при необходимости

def delayed_launch(initializer: Callable, task: Callable, permission: Callable) -> None:
    pass # допишите код


#-----------

start_time = time.perf_counter()

delayed_launch(my_initializer, my_task, my_test_permission)

if time.perf_counter()-start_time >= 0.01:
    print("Функция delayed_launch блокирует работу главного потока!")
Если Ваше определение функции будет верным, то программа завершится успешно и будет распечатан следующий результат:

Вызов initializer
Вызов permission 1 раз
Вызов permission 2 раз
Вызов permission 3 раз
Вызов permission 4 раз
Вызов task
"""

import threading
from typing import Callable


event = threading.Event()


def func_1(initializer, task, event):
    initializer()
    event.wait()
    task()


def func_2(permission, event):
    while permission() != True:
        pass
    event.set()


def delayed_launch(initializer: Callable, task: Callable, permission: Callable) -> None:
    threading.Thread(target=func_1, args=(initializer, task, event)).start()
    threading.Thread(target=func_2, args=(permission, event)).start()
