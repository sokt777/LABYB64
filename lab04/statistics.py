n = int(input(" Введитие какое количество чисел хотите ввести: "))

summa = 0
polozh_count = 0
maximum = 0

for i in range(n):
    x = int(input(" Введите числа: "))
    summa += x
    if x > 0:
        polozh_count += 1
    if i ==0:
        maximum = x
    elif x > maximum:
        maximum = x

print("Количество положительных числел: " , polozh_count)
print("Сумма всех числел: " , summa)
print("Максимальное число: " ,maximum)