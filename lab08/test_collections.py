if __name__ == "__main__":
    print("=== Задание 1: частоты слов ===")
    text = "Python python SQL! sql, python? ..."
    counts = word_counts(text)
    print_word_pairs(counts)
    print("Пустой текст ->", word_counts(""))
    print()

    print("=== Задание 2: темы ===")
    first = ["python", "sql", "git"]
    second = ["sql", "docker", "python"]
    print("Общие:", common_topics(first, second))
    print("Все:",   all_topics(first, second))
    print()

    print("=== Задание 3: запись и пара ===")
    demo_record_and_pair()
    print()

    print("=== Вариант 7: настольные игры ===")
    print("Сводка по категориям (алфавит):")
    for cat in sorted(totals_by_category(records)):
        print(f"  {cat}: {totals_by_category(records)[cat]}")
    print()

    user_cat = input("Введите категорию для поиска: ").strip()
    print(f"Названия в категории '{user_cat}':", titles_in_category(records, user_cat))