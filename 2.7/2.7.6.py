"""
Таможенное управление в среднем может проверить 30 грузовых таможенных деклараций за рабочий день, если все инспекторы работают в обычном темпе. Но дни бывают разные. Например, в предпраздничные дни количество деклараций увеличивается. Если часть деклараций остается необработанной, оставшиеся декларации будут обработаны в следующий менее нагруженный рабочий день.

Вам нужно создать две очереди:
рабочая (основная) очередь деклараций main_queue с ограничением размера в 30 деклараций и вспомогательная очередь "работы на завтра" sup_queue.

Пока команда дорабатывает сервис передачи таможенных деклараций, включая валидацию деклараций, вам поручили написать и протестировать основную логику взаимодействия программы.

Кроме двух очередей Вам нужно:

Определить целевую функцию производителя. Эта простая функция всего лишь добавляет декларацию (экземпляр класса CCD) в основную очередь, если очередь не заполнена. А если заполнена – то добавление происходит в вспомогательную очередь. Сервис доставки деклараций еще не готов, поэтому для тестов Вам подготовили так называемую mock-функцию, имитирующую доставку информаций о грузе (а фактически генератор фейковых, но валидных словарей для создания экземпляров класса CCD). Функция get_next_declaration() является таким генератором. Ваша функция производителя должна работать в цикле, пока возвращаемый объект генератора не будет None.
Определить целевую функцию потребителя. Эта функция всего лишь получает декларацию из основной очереди, обрабатывает ее и после завершения помечает как обработанную. Функция обработки тоже еще не готова, поэтому в качестве обработки для каждого экземпляра CCD полученного из очереди, нужно вызвать функцию handler() и передать в нее декларацию в качестве аргумента. После успешной обработки, handler() вернет True, после чего задачу нужно пометить выполненной. Вашу функцию потребителя запустите в бесконечном цикле.
Запустите один поток-производитель и дождитесь его завершения, чтобы он наполнил рабочую очередь и очередь работы на завтра.
Запустите три потока-инспектора, с соответствующими именами (атрибуты .name): "inspector_1", "inspector_2", "inspector_3". Потоки-инспекторы запустите в демоническом режиме.
В основном потоке программы дождитесь завершения обработки всех деклараций из очереди, а затем переместите все декларации из второстепенной очереди в основную, чтобы обработать их в следующий рабочий день.
В тестирующей системе уже определен класс CCD из прошлой задачи (инициализатор класса принимает единственный позиционный аргумент – словарь с информацией о грузе), функции get_next_declaration и handler. Система проверяет время выполнения программы, итоговое содержание и очередность деклараций в очередях.
"""

import queue
import threading

# создайте две очереди, подумайте над типом основной очереди.
main_queue = queue.PriorityQueue(maxsize=30)
sup_queue = queue.Queue()


# напишите функцию производителя
def producer():
    for elem in get_next_declaration():
        if elem is not None:
            ccd = CCD(elem)
            if not main_queue.full():
                main_queue.put(ccd)
            else:
                sup_queue.put(ccd)


# напишите функцию потребителя
def consumer():
    while True:
        try:
            elem = main_queue.get()
            handler(elem)
            main_queue.task_done()
        except queue.Empty:
            break


# создайте и запустите потоки потребителей и поток производителя
thread_producer = threading.Thread(target=producer, name="producer")
thread_producer.start()
thread_producer.join()

thread_consumer_1 = threading.Thread(target=consumer, name="inspector_1", daemon=True)
thread_consumer_2 = threading.Thread(target=consumer, name="inspector_2", daemon=True)
thread_consumer_3 = threading.Thread(target=consumer, name="inspector_3", daemon=True)
thread_consumer_1.start()
thread_consumer_2.start()
thread_consumer_3.start()

main_queue.join()

# после завершения обработки всех деклараций из главной очереди,
# переместите в главную очередь все декларации из вспомог. очереди для работы на завтра

while not sup_queue.empty():
    main_queue.put(sup_queue.get())
