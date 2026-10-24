stroka = input("Введите текст: ")

normalized = " ".join(stroka.lower().split())
print(f"Длина первозначальной строки: {len(stroka)}")
print(f"Длина новой строки: {len(normalized)}")
print(f"Слов: {len(normalized.split())}")

