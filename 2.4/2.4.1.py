"""
Закрепим теорию очень простым заданием.

Создайте демонический объект Таймера my_timer, для которого:
- укажите interval в 1 секунду;
- назначьте целевую функцию: my_function
- в качестве единственного аргумента для функции my_function передайте переменную msg
- назначьте имя (.name): MyTimer

Не стартуйте Таймер! Только создайте объект Таймера.
Тестирующая система проверит аргументы и атрибуты, затем запустит Таймер и проверит его работу. Целевая функция my_function, которая принимает единственный аргумент msg, определена в тестирующей системе, не изменяйте ее, как и переменную msg.
"""

import threading

my_timer = threading.Timer(interval=1, function=my_function, args=(msg, ))
my_timer.name = 'MyTimer'
my_timer.daemon = True
