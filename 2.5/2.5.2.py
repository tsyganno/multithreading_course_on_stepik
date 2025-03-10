"""
Напишите класс SimpleThread, который:
1. Наследуется от класса Thread.
2. В конструкторе позволяет указывать два аргумента — function и data.
2. Для экземпляров класса позволяет обращаться к атрибутам .function и .data.
4. Переопределяет метод run() так, чтобы запускать функцию переданную в атрибут function с аргументом data. А результат выполнения этой функции — выводит на печать.

Тестирующая система создаст экземпляр класса, проверит наличие атрибутов и результат выполнения.
"""

import threading


class SimpleThread(threading.Thread):
    def __init__(self, data, function):
        super().__init__()
        self.data = data
        self.function = function

    def run(self) -> None:
        print(self.function(self.data))
