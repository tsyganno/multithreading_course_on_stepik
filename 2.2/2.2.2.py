"""
Возвращаемся к прошлой задаче.
При тестировании было выявлено, что решение может зависать в случае проблем с соединением и долгого ожидания ответа от ресурса. Тимлид решает, что на каждый запрос надо отводить не более 1.5 секунды и не ждать дольше этого времени. Вместо заголовков для ресурсов, ответ от которых превышает этот лимит, необходимо заполнять строковым значением "no_response".

Перепишите Ваше предыдущее решение с учетом этого нового условия. Все определения предыдущей задачи не изменились. Тестирующая система проверяет время выполнения решения и содержание словаря headers_stor.
Ваше решение может содержать не только операции с потоками, но и дополнительную работу со словарем заголовков.

Если бы в тестирующей системе были следующие простые определения:

from time import sleep

headers_stor = {}

sources = ["bing.com",
           "google.ru",
           "yahoo.com",
           "mail.ru",
           "ya.ru"]


def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"


import threading


# Ваше решение



# Работа тестирующей системы:
for url, headers in sorted(headers_stor.items()):
    print(f"{url}: {headers}")
то вследствие выполнения вашего решения:
- время выполнения программы не должно превышать ~1.5 секунды;
- в консоль должно быть выведено:

bing.com: ok
google.ru: ok
mail.ru: no_response
ya.ru: ok
yahoo.com: no_response
В тестирующей системе другой список ресурсов другой длины и другие таймауты ответов. Тест. система проверит время Вашего решения и содержимое headers_stor.
"""

import threading
from time import sleep


headers_stor = {
    'https://baidu.cn': 'no_response',
    'https://mail.ru': 'no_response',
    'https://www.bing.com': 'no_response',
    'https://www.google.ru': 'no_response',
    'https://www.yahoo.jp': 'no_response',
    'https://ya.ru': 'no_response'
}

sources = [
    'https://baidu.cn',
    'https://mail.ru',
    'https://www.bing.com',
    'https://www.google.ru',
    'https://www.yahoo.jp',
    'https://ya.ru'
]


def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"


threads = []
for source in sources:
    thread = threading.Thread(target=get_request_header, args=(source, ), daemon=True)
    thread.start()
    threads.append(thread)

sleep(1.5)

print()
# Работа тестирующей системы:
for url, headers in sorted(headers_stor.items()):
    print(f"{url}: {headers}")


