"""
На практике не всегда удобно "выцеливать" критическую секцию в коде, определяя ее границы методами acquire и release. Удобнее и нагляднее использовать контекстный менеджер with. Но, нередко целевые функции потоков включают в себя несколько вызовов других функций, требующих синхронизации. В таком случае удобно использовать декоратор.

Напишите декоратор with_lock, который защищает выполнение функции объектом синхронизации Lock.

Ваша задача — написать декоратор. Декорирование конкретных функций, создание и запуск нескольких потоков с использованием декоратора будет выполнено тестирующей системой.

Если забыли, вспомнить как писать декораторы поможет вот эта статья.
"""

import threading

lock = threading.Lock()


def with_lock(func):
    def inner(*args, **kwargs):
        lock.acquire()
        func(*args, **kwargs)
        lock.release()
    return inner
