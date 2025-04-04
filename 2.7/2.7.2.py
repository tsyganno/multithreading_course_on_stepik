"""
Перед Вами код, написанный стажером. Позже он будет использоваться как часть общего решения, над которым работает команда, но сначала его нужно исправить. Найдите все ошибки и исправьте код.

Стажер должен был реализовать простую модель: два потребителя – один производитель. Поток-производитель должен получать элемент из источника (функция-генератор get_obj()) и, если элемент проходит проверку, то отправлять его на обработку потребителям. Обработка выполняется двумя потоками-потребителями.

Проверка должна выполняться функцией is_valid(). Функция принимает элемент и возвращает True или False. Если элемент не проходит проверку (is_valid возвращает False), производитель добавляет элемент в очередь none_valid_queue. Если проходит проверку – добавляет элемент в очередь valid_queue.

Два потока-потребителя должны получать элементы из очереди валидных элементов и обрабатывать их, запуская функцию обработчика handler(). Функция handler в качестве аргумента принимает один элемент – объект из валидной очереди.

Для контроля завершения работы, команда договорилась использовать подход с двумя сигнальными элементами None. Это значит, что в конце работы валидная очередь должна оказаться пустой.

Функция-генератор get_obj и функция обработки handler заданы в тестирующей системе. Не изменяйте их, только вызывайте.

Тестирующая система проверит время Вашего решения, порядок выполнения и вывод программы. Проверит, что все элементы из генераторы были обработаны. Также проверит содержание обоих очередей. В момент проверки очередь valid_queue должна быть пустой, а очередь none_valid_queue должна содержать только невалидные элементы.
"""

from queue import Queue
from threading import Thread

valid_queue = Queue()
none_valid_queue = Queue()


def main():
    for elem in get_obj():
        if is_valid(elem):
            valid_queue.put(elem)
        else:
            none_valid_queue.put(elem)
    valid_queue.put(None)
    valid_queue.put(None)


main_th = Thread(target=main)
main_th.start()


def task():
    while True:
        elem = valid_queue.get()
        if elem is None:
            break
        handler(elem)


t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()

t1.join()
t2.join()
