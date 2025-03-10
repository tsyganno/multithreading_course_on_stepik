"""
Решите простую задачу в концепции один производитель — два потребителя.

Задача производителя: наполнить очередь элементами из генератора get_obj().

Задача потребителей: получить элемент из очереди и запустить функцию обработки handler(). Функция обработки получает единственный аргумент — элемент из очереди.

Поток-производитель должен иметь имя (атрибут name) "producer".
Потоки-потребители должны иметь имена (атрибуты name) "consumer_1" и "consumer_2".

Ваше решение должно быть выполнено в следующем порядке:

Напишите функции производителя и потребителя.
Создайте поток производителя. Запустите его выполнение. Дождитесь завершения его работы, чтобы наполнить очередь.
Создайте потоки потребителей. Запустите их на выполнение. Дождитесь завершения их работы, чтобы все элементы из очереди были обработаны.
Генератор get_obj, функция обработки handler заданы в тестирующей системе. Не изменяйте их, только вызывайте.

Тестирующая система проверит время Вашего решения, порядок выполнения и вывод программы. Проверит, что все элементы из генераторы были обработаны.
"""

import threading
import queue

my_queue = queue.Queue()


def producer():
    for el in get_obj():
        my_queue.put(el)


def consumer_1():
    while not my_queue.empty():
        handler(my_queue.get())


def consumer_2():
    while not my_queue.empty():
        handler(my_queue.get())


thread_producer = threading.Thread(target=producer, name="producer")
thread_producer.start()
thread_producer.join()

thread_consumer_1 = threading.Thread(target=consumer_1, name="consumer_1")
thread_consumer_2 = threading.Thread(target=consumer_2, name="consumer_2")
thread_consumer_1.start()
thread_consumer_2.start()
thread_consumer_1.join()
thread_consumer_2.join()
