n = int(input(" Введитие какое количество чисел хотите ввести: "))

necrat = 0
summa = 0

for i in range(n):
    x = int(input(" Введите числа: "))
    if x % 3 != 0:
        necrat += 1
        summa += x


print("Число подходящих значений: ",necrat)
print("Сумма всех чисел подходящих чисел: ",summa)