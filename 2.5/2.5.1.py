"""
В коде определения класса MyThread присутствуют несколько ошибок. Исправьте их. Класс очень простой: запускает задачу task в новом потоке и если в результате возникает ошибка — выводит заданное в конструкторе сообщение об ошибке.

Тестирующая система создаст экземпляр класса. Запустит его, проверит создание нового потока, доступность атрибутов наследуемого класса, значение и доступность нового атрибута: msg_error.  Проверит работу целевой функции.
"""

import threading
from typing import Callable


# Исправьте ошибки в классе
class MyThread(threading.Thread):
    def __init__(self, msg_error: str = "error", task: Callable = None):
        super().__init__()
        self.msg_error = msg_error
        self.task = task

    def run(self) -> None:
        try:
            self.task()
        except Exception as err:
            self.msg_error = err
            print(self.msg_error)
