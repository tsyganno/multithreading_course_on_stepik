"""
Напишите функцию обработки не перехваченных исключений и переопределите threading.excepthook на нее.

Кастомная функция обработки очень простая. Все что она делает — это печать в консоль сообщение исключения (exc_value).

Создание и запуск дополнительных потоков для проверки обработки не перехваченных исключений и указание сообщений исключений будет выполнено тест. системой.
"""

import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    print(exc_value)


threading.excepthook = custom_hook
