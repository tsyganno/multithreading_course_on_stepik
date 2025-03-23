"""
Для кода ниже:

import threading
from typing import Callable
from time import perf_counter
from itertools import count


class TestWorker(threading.Thread):
    def __init__(self, task: Callable, permission: Callable):
        super().__init__()
        self.permission = permission
        self.task = task
        self.condition = threading.Condition()

    def make_work(self):  # основной метод выполняет задачу если получено условие
        with self.condition:
            tmp = self.condition.wait_for(predicate=self.permission, timeout=1)
            if tmp:
                self.task()  # выполняем задачу если разрешено
            else:
                # не выполняем задачу, просто логируем, что не дождались условия
                print(f"{threading.current_thread().name} завершается по таймеру")

    def run(self):
        self.make_work()


def task():
    print(f"{threading.current_thread().name} ВЫЗЫВАЕТ ЗАДАЧУ task!")


_count = count(1)


# допишите функцию permission
def permission():
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"{thread_name} проверяет предикат, permission вызывается {n}-й раз")
    ...
допишите функцию permission так, чтобы целевую задачу выполнил успешно только второй по очередности поток, вызвавший проверку условия, причем только со второго раза после истечения таймера. Только допишите необходимую логику в функции и все, что она может еще использовать. Все что уже задано — изменять нельзя. И сам класс и создание и запуск нескольких потоков — все определено в тестирующей системе.

Гарантируется, что будет создано и запущено два или более потоков в период до истечения таймаута ожидания условия.
"""

call_counter = 0  # Глобальный счётчик вызовов permission
allowed_thread = None  # Поток, который получит разрешение


def permission():
    global call_counter, allowed_thread
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"{thread_name} проверяет предикат, permission вызывается {n}-й раз")

    call_counter += 1  # Увеличиваем общий счётчик вызовов

    if call_counter == 2:  # Запоминаем второй поток, который вызвал permission()
        allowed_thread = thread_name
        return False  # Пока не даём разрешение, ждем повторного вызова

    if call_counter > 2 and thread_name == allowed_thread:  # Со второго раза даём разрешение
        return True

    return False
