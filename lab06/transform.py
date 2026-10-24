
b = []
for w in input("Введите целые числа: ").split():
    b.append(int(w))

transformed = []
for i in b:
    if i < 0:
        transformed.append(-i)
    else:
        transformed.append(i)

print(f"Исходный список чисел: {b}")
print(f"Новый список чисел: {transformed}")