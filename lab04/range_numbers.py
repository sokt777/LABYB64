a = int(input(" Введитие первое число: "))
b = int(input(" Введитие второе число: "))

if a < b:
    for i in range (a, b+1):
        print(i)
elif a > b:
    for i in range (a, b-1, -1):
        print(i)
else:
    print(a)