obsh_obem = int(input("Введите Количество саженцев: "))
vmest_1sazh = int(input("Введите вместимость одной единицы: "))
total = obsh_obem // vmest_1sazh
ostat = obsh_obem % vmest_1sazh
min = (obsh_obem + vmest_1sazh - 1) // vmest_1sazh
print("Количество заполненных рядов:", total)
print("Остаток саженцев:", ostat)
print("Минимальное число рядов:", min)

