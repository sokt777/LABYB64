

chance = 0
while True:
    a = int(input("Введите целое положительное число: "))
    if a > 0:
        break
    chance += 1
    if a > 0:
        print("Введите другое число: ")

print("Квадрат положительного числа: ", a**2)
print("Количетсво попыток ввести: ", chance)