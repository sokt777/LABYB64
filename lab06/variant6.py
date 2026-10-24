b = []
for w in input("Введите целые числа: ").split():
    b.append(int(w))

usl = [i for i in b if i%3!=0]
total = len(b)
summa = sum(b)
sort = sorted(b)
print(f"Cписок выполняющий условие: {usl}")
print(f"Исходный список чисел: {b}")
print(f"Количество в списке: {total}")
print(f"Сумма чисел в списке: {summa}")
print(f"Отсортированный список по возростанию: {sort}")