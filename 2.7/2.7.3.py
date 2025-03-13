"""
Решите прошлую задачу без сигнальных элементов, используя task_done и join очереди. Условия прошлой задачи почти не изменились.

Задача производителя: наполнить очередь элементами из генератора get_obj().

Задача потребителей: получить элемент из очереди и запустить функцию обработки handler(). Функция обработки получает единственный аргумент – элемент из очереди.

Поток-производитель должен иметь имя (атрибут .name) "producer".
Потоки-потребители должны иметь имена (атрибуты .name) "consumer_1" и "consumer_2".

Ваше решение должно быть выполнено в следующем порядке:

Напишите функции производителя и потребителя.
Создайте поток производителя. Запустите его выполнение.
Создайте потоки потребителей. Запустите их на выполнение. В целевой задаче потребителей, используя метод task_done  отмечайте обработанные элементы очереди.
Правильно организуйте ожидание завершения работы, используя join очереди и join производителя.
Генератор get_obj, функция обработки handler заданы в тестирующей системе. Не изменяйте их, только вызывайте.

Тестирующая система проверит время Вашего решения, порядок выполнения и вывод программы. Проверит, что все элементы из генераторы были обработаны.
"""

import threading
import queue

my_queue = queue.Queue()


def producer():
    for elem in get_obj():
        my_queue.put(elem)


def consumer():
    while True:
        elem = my_queue.get()
        handler(elem)
        my_queue.task_done()


thread_producer = threading.Thread(target=producer, name="producer", daemon=True)
thread_producer.start()
thread_consumer_1 = threading.Thread(target=consumer, name="consumer_1", daemon=True)
thread_consumer_2 = threading.Thread(target=consumer, name="consumer_2", daemon=True)
thread_consumer_1.start()
thread_consumer_2.start()
thread_producer.join()
my_queue.join()
