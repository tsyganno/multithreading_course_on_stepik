"""
Как и в предыдущем задании, напишите функцию и организуйте обработку не перехваченных исключений.

Создание и запуск дополнительных потоков для проверки обработки не перехваченных исключений будет выполнено тест. системой.

Теперь функция обработки должна выводить информацию об ошибке в консоль быть более информативно, согласно шаблону:

<thread_name>, <type_error_name>, <msg>
где:
<thread_name> — имя потока, который вызвал исключение (exc_thread.name);
<type_error_name> — имя типа исключения (exc_type.__name__);
<msg> — сообщение исключения (exc_value).

Соблюдайте пробелы и запятые!
"""

import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    print(f'{exc_thread.name}, {exc_type.__name__}, {exc_value}')


threading.excepthook = custom_hook