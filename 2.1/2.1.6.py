import requests
from time import perf_counter
import threading

sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0
for source in sources:
    start_tmp = perf_counter()
    headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta

print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(len(headers_stor.items()))
print()
print('------------------------------------------------------------------------------------------------------------')
print()

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0
threads = []


def get_request_header(url: str) -> None:
   headers_stor[url] = requests.get(url).headers  # получает заголовки и формирует словарь


for source in sources:
    start_tmp = perf_counter()
    thread = threading.Thread(target=get_request_header, args=(source, ))
    thread.start()
    threads.append(thread)
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta

for thread in threads:
    thread.join()

print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(len(headers_stor.items()))  # Выводим наши заголовки
