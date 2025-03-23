"""
Целевая функция task выполняет три функции, первые две являются подготовительными и их не нужно защищать примитивами синхронизации. Третья функция является завершающей. Ее можно вызывать только тогда, когда контролирующий поток даст на это разрешение. Используя объект синхронизации Event создайте необходимое ожидание перед вызовом третьей функции.

Только допишите функцию task, не изменяя уже заданного в ней. Создание и запуск нескольких потоков для ее выполнения, создание и запуск контролирующего потока, который в необходимый момент вызовет метод set у объекта event — все это будет выполнено в тестирующей системе.
"""

import threading

# создайте объект синхронизации Event
event = threading.Event()


def task():
    # Выполните необходимое ожидание перед вызовом some_work_part3
    some_work_part1()
    some_work_part2()
    event.wait()
    some_work_part3()
