"""
Повторяем старое задание с новыми знаниями.

Есть список интернет-ресурсов sources. Необходимо получить заголовки всех этих страниц и сохранить результаты в словаре headers_stor, где ключ — адрес, ссылка на ресурс (str), а значение — словарь заголовков этого ресурса.

Функция получения заголовков get_request_header уже определена в тестирующей системе. В качестве единственного аргумента она принимает строковый адрес из списка ресурсов, а выдает словарь заголовков.

def get_request_header(url: str) -> dict:
    ...
Вам необходимо организовать создание и работу пула потоков и заполнить словарь . Тестирующая система проверяет время решения и вывод содержимого хранилища заголовков следующим образом:

for url, headers in headers_stor.items():
    print(f"{url}: {headers}")
Порядок ключей в headers_stor должен соответствовать порядку в списке sources.

Напишите решение с использованием метода map.
"""

from concurrent.futures import ThreadPoolExecutor

headers_stor = {}


def next_sources(sources):
    for source in sources:
        yield source


gen = next_sources(sources)

with ThreadPoolExecutor() as pool:
    for result in pool.map(get_request_header, sources):
        headers_stor[next(gen)] = result
