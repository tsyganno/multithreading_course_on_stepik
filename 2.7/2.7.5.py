"""
Ваш работодатель участвует в конкурсе цифровизации работы таможенного управления. На первом этапе конкурса от каждого участника просят предоставить упрощённую модель решения взаимодействия таможенных инспекторов, проверяющих таможенные декларации.

Таможенное управление получает грузовые таможенные декларации на проверку. Каждая декларация проверяется одним из инспекторов. Декларации должны обрабатываться с учетом категории груза, т.к. груз может быть скоропортящимся, а значит его нужно проверить и выпустить как можно скорее. Но максимальным приоритетом обладают грузы из стран таможенного союза, они обрабатываются в первую очередь.

Ваша команда уже определилась, что очередность обработки будет реализована через PriorityQueue и пока она думает над деталями реализации, Вам поручают написать класс, представляющий грузовую таможенную декларацию.

Напишите класс грузовой таможенной декларации, экземпляры которого будут использоваться в качестве объектов очереди с приоритетом:

Имя класса CCD.
При инициализации экземпляра будет передаваться словарь с информацией о грузе со следующими парами ключ: <значение>:
"cat": <категория товара по коду ТН ВЭД, тип str>
"union": <признак груза таможенного союза ЕАЭС, тип bool>
"cargo": <дополнительная информация о грузе: вес, упаковка и т.п., тип iterable>
"id": <идентификационный номер, уникальный код который назначается декларации, соответствует входящему номеру, тип int>
Экземпляры класса согласно п. 2 должны иметь соответствующие публичные атрибуты: cat, union, cargo, id.
Экземпляры класса должны поддерживать сравнение, это значит, что Вам необходимо написать метод сравнения "меньше" (__lt__).
Сравнение должно быть реализовано по следующему правилу: в первую очередь обрабатываются грузы таможенного союза. Если таких грузов несколько, то приоритет отдается грузам с категорией скоропортящихся (это грузы с категорией "0201", "0202" и т.д. до 0209", причем между ними не должно быть приоритета, все они одинаково важные). Если и таких грузов несколько — то в первую очередь обрабатываются грузы с наименьшим входящим номером (id).
Тестирующая система создаст несколько экземпляров CCD, отсортирует их. А затем проверит этот порядок, обращаясь к id отсортированных экземпляров деклараций CCD.

Вы можете протестировать свое решение самостоятельно перед отправкой в тест. систему. Вот несколько простых экземпляров словарей с информацией о грузе для этих целей:

d1 = {"cat": "0210", "union": True, "cargo": {"stew", 2}, "id": 1}
d2 = {"cat": "0208", "union": True, "cargo": {"liver", 1.78}, "id": 2}
d3 = {"cat": "0208", "union": True, "cargo": {"liver", 56}, "id": 3}
d4 = {"cat": "0209", "union": False, "cargo": {"pork fat", 100}, "id": 4}
d5 = {"cat": "87", "union": False, "cargo": {"bombardier", 1}, "id": 5}
d6 = {"cat": "0201", "union": False, "cargo": {"veal", 120}, "id": 7}
d7 = {"cat": "0201", "union": False, "cargo": {"veal", 79}, "id": 6}

dataset= [CCD(d) for d in (d1, d2, d3, d4, d5, d6, d7)]
print(*(ccd.id for ccd in sorted(dataset)))

# Если класс CCD реализован правильно, то отсортированный список id деклараций будет распечатан так:
# 2 3 1 4 6 7 5
"""

class CCD:
    # Категории скоропортящихся товаров
    PERISHABLE_CATEGORIES = {f"020{i}" for i in range(1, 10)}

    def __init__(self, d: dict):
        self.cat = d["cat"]
        self.union = d["union"]
        self.cargo = d["cargo"]
        self.id = d["id"]

    def __lt__(self, other):
        """Определяет порядок сортировки в очереди с приоритетом."""
        return (
            not self.union,  # Грузы ЕАЭС (True) приоритетнее (False < True)
            self.cat not in self.PERISHABLE_CATEGORIES,  # Скоропортящиеся приоритетнее (False < True)
            self.id  # Меньший ID приоритетнее
        ) < (
            not other.union,
            other.cat not in self.PERISHABLE_CATEGORIES,
            other.id
        )
