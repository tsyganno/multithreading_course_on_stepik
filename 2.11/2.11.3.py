"""
Создайте и запустите четыре потока с целевой задачей, которая выполняет (вызывает) две функции. Целевая задача должна выполнять две функции в два этапа, разделенные одним барьером. Вторая функция должна вызываться только после успешного выполнения первой функции всеми потоками-участниками.

Создайте объект барьера, создайте целевую функцию в аргументы которой передайте объект барьера и две функции: task_stage1, task_stage2. При преодолении барьера должна вызываться функция финализатора finalizer. Создайте и запустите четыре потока, выполняющую целевую функцию. Потоки должны иметь имена: "Thread #1", "Thread #2" и т.д.

Решите задачу, используя атрибут action.

Функции task_stage1, task_stage2 и finalizer заранее определены в тестирующей системе. Не изменяйте их.

Если бы в тестирующей системе были вот такие простые определения:

import time
import random


def finalizer():
    print("STAGE #1 ALL DONE!")


def task_stage1():
    time.sleep(random.uniform(0, 1))
    print(f"stage #1 done by {threading.current_thread().name}")


def task_stage2():
    time.sleep(random.uniform(0, 1))
    print(f"stage #2 done by {threading.current_thread().name}")

#  Ваше решение:

import threading

# Создайте объект барьера
# Создайте целевую функцию, выполняющую задачи в два этапа
# Создайте и запустите 4 потока
то в результате решения  должен быть аналогичный вывод:

stage #1 done by Thread #4
stage #1 done by Thread #3
stage #1 done by Thread #2
stage #1 done by Thread #1
STAGE #1 ALL DONE!
stage #2 done by Thread #4
stage #2 done by Thread #3
stage #2 done by Thread #2
stage #2 done by Thread #1
"""

import threading

# Создайте объект барьера
barrier = threading.Barrier(4, action=finalizer)

# Создайте целевую функцию, выполняющую задачи в два этапа
def task():
    task_stage1()
    barrier.wait()
    task_stage2()

# Создайте и запустите 4 потока c требуемыми именами
for i in range(4):
    threading.Thread(target=task, name=f'Thread #{i + 1}').start()
