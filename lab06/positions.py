b = []
for w in input("Введите целые числа: ").split():
    b.append(int(w))

if not b:
    print("Нет данных")
else:
    maximum = max(b)
    v = []
    for i, value in enumerate(b):
        if value == maximum:
            v.append(i)
    print(v)
