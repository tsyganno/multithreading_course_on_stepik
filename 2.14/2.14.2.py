"""
Измените решение предыдущей задачи согласно дополнительным условиям:

Получите и распечатайте результаты вызова задач.
Ограничьте время ожидания получения результата одной секундой, используя таймаут метода map. Если время ожидания результата превышает таймаут, выведите сообщение в консоль:
Завершение работы по таймауту!
Все остальные условия задачи остались без изменений.
"""

# импортируйте необходимое
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import threading


# создайте функцию инициализации
def initial():
    name = threading.current_thread().name
    print(f"Поток {name} выполняет инициализацию")


# создайте пул потоков согласно условию задачи и
# запустите задачи, используя map и контекстный менеджер пула
pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix=f'task_pool', initializer=initial)
with pool:
    try:
        for result in pool.map(task, range(1, 11), timeout=1):
            print(result)
    except TimeoutError:
        print('Завершение работы по таймауту!')
