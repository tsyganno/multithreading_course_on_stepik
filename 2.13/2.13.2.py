"""
Если вы решили предыдущую задачу с использованием глобальной области видимости или через счетчик активных потоков, попробуйте решить задачу только с использованием локального хранилища потоков.

stor_local = threading.local()
Предыдущие условия немного изменились:
1. В какой-то момент времени один из потоков получает разрешение по внешнему условию (например, получает ответ от микросервиса), в этом случае в коде программы для него формируется локальный атрибут

stor_local.permission = True
Для остальных потоков такой атрибут не будет назначен. С течением времени несколько потоков могут получить положительный ответ от сервиса, а значит уже у нескольких потоков будет атрибут stor_local.permission = True.

2. Перепишите функцию permission так, чтобы целевую задачу выполнил успешно только тот поток, кто дважды ее вызвал уже имея атрибут разрешения. В функции разрешено использовать только атрибуты stor_local.

В тестирующей системе определен класс, создаются экземпляры потоков, создано локальное хранилище потоков
stor_local = threading.local(), для некоторых потоков в некоторый момент времени создается и назначается атрибут stor_local.permission = True.
"""


def permission():
    if hasattr(stor_local, 'permission'):
        if getattr(stor_local, "permission") == True:
            if 'count' not in stor_local.__dict__:
                stor_local.__dict__['count'] = 1
            else:
                stor_local.__dict__['count'] += 1
            if stor_local.__dict__['count'] == 2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
