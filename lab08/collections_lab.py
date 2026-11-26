def word_counts(text):
    counts = {}
    for raw in text.lower().split():
        word = raw.strip(".,!?;:")
        if word:                      # пропускаем пустые строки
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_word_pairs(counts):
    """Выводит пары 'слово: количество' по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

def common_topics(first, second):
    """Отсортированный список общих тем (пересечение множеств)."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем (объединение множеств)."""
    return sorted(set(first) | set(second))

def demo_record_and_pair():
    """Создаёт запись-словарь, меняет её, делает кортеж и распаковывает его."""
    record = {"title": "Catan", "hours": 60}   # ключи — строки
    record["hours"] = 90                        # присваивание по существующему ключу
    record["completed"] = False                 # добавление нового ключа

    pair = (record["title"], record["hours"])   # кортеж-пара
    name, hours = pair                          # распаковка кортежа
    print(f"Пара: {name}, {hours}")
    return record, pair

records = [
    {"title": "Catan",          "category": "стратегия",     "amount": 4},
    {"title": "Pandemic",       "category": "кооперативная", "amount": 4},
    {"title": "Uno",            "category": "карточная",     "amount": 8},
    {"title": "Ticket to Ride", "category": "стратегия",     "amount": 5},
    {"title": "Codenames",      "category": "кооперативная", "amount": 8},
]


def totals_by_category(records):
    """Словарь сумм amount по категориям. Входной список и словари НЕ меняются."""
    totals = {}
    for rec in records:
        cat = rec["category"]
        totals[cat] = totals.get(cat, 0) + rec["amount"]
    return totals


def titles_in_category(records, category):
    """Названия записей данной категории в исходном порядке.
    Неизвестная категория -> []."""
    result = []
    for rec in records:
        if rec["category"] == category:
            result.append(rec["title"])
    return result
