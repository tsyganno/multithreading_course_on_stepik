"""
В коде определения функции thread_log присутствуют несколько ошибок (и, возможно, не хватает нескольких инструкций). Исправьте их. Функция очень простая, она принимает два вызываемых объекта:

task — целевую задачу на выполнение отдельным демоническим потоком,
log_task — целевую задачу логирования, которая должна выполниться, если выполнение task не завершилось за отведенное время, задача "зависла".
Ну, а если задача завершилась за отведенное время — задача логирования не должна быть вызвана.
Контрольное время — третий аргумент функции.

Тестирующая система вызовет функцию thread_log и проверит ее работу с различными аргументами.
"""

import threading
from typing import Callable


def thread_log(task: Callable, log_task: Callable, t_check: int | float) -> None:
    thread = threading.Thread(target=task, daemon=True)
    timer = threading.Timer(interval=t_check + 0.1, function=log_task)
    thread.start()
    timer.start()
    thread.join(t_check)
    if not thread.is_alive():
        timer.cancel()
