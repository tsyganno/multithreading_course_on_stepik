"""
Напишите функцию логирования print_msg, которая подготавливает и печатает сообщение о работе потока по шаблону:
<Сообщение>, fileno=<файловый дескриптор>, <право доступа>
где: <Сообщение> — атрибут msg локального хранилища потока;
<файловый дескриптор> — файловый дескриптор, атрибут fileno хранилища, целое число;
<право доступа> — доступ к файлу, атрибут permission, строка.

Например:
deleted ID 4660, fileno=11128, DOMAIN\admin

При этом, если атрибут permission не установлен, в правах доступа следует выводить guest
Если атрибуты msg или fileno не установлены, вместо них следует выводить failure

Например, предыдущая запись без атрибута msg и permission:
failure, fileno=11128, guest

Внимание! соблюдайте пробелы и запятые.

Тестирующая функция создаст и запустит несколько потоков, которые в процессе жизни вызовут Вашу функцию print_msg.
Локальное хранилище создано в тестирующей системе: stor_local = local()
"""

from threading import local


def print_msg(stor_local: local) -> None:
    fileno = 'failure'
    msg = 'failure'
    permission = 'guest'
    if hasattr(stor_local, "fileno"):
        fileno = stor_local.fileno
    if hasattr(stor_local, "msg"):
        msg = stor_local.msg
    if hasattr(stor_local, "permission"):
        permission = stor_local.permission
    print(f'{msg}, fileno={fileno}, {permission}')
