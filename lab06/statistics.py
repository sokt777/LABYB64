b = []

for w in input("Введите целые числа: ").split():
    b.append(int(w))

if not b:
    print("Нет данных")
elif b:
    min_val = b[0]
    max_val = b[0]
    for i in b[1:]:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    print(f"Количество чисел: {len(b)}")
    print(f"Cумма чисел: {sum(b)}")
    print(f"Максимальное число: {max_val}")
    print(f"Минимальное число: {min_val}")
    print(f"Cреднее арефметическое чисел: {(sum(b)/len(b)):.2f}")

