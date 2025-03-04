"""
Как и в предыдущем задании, напишите функцию и организуйте обработку не перехваченных исключений.

Создание и запуск дополнительного потока для проверки обработки не перехваченных исключений будет выполнено тест. системой.

Теперь функция обработки сложнее. Если тип исключения TypeError или ValueError — то необходимо просто выводить информацию об ошибке в консоль. Если исключение другого типа - то необходимо создать файл custom_errors.txt и уже туда записать информацию об ошибке. Информация об ошибке для двух источников вывода — одинакова и соответствует шаблону предыдущей задачи:
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
    if exc_type in (TypeError, ValueError):
        print(f'{exc_thread.name}, {exc_type.__name__}, {exc_value}')
    else:
        with open("custom_errors.txt", "w") as file:
            file.write(f'{exc_thread.name}, {exc_type.__name__}, {exc_value}')


threading.excepthook = custom_hook
