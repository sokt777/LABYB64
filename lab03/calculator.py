num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
d = input("операция (+, -, *, /): ")


if d == "+":
    result = num1 + num2
    print(f"Результат: {result:.2f}")
elif d == "-":
    result = num1 - num2
    print(f"Результат: {result:.2f}")
elif d == "*":
    result = num1 * num2
    print(f"Результат: {result:.2f}")
elif d == "/":
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")