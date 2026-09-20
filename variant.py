zakaz = input("Название заказа ")
name = input("Имя заказчика ")

poz1_name = input("Название первой позиции")
poz1_kol = int(input("Количество первой позиции "))
poz1_cen = float(input("Цена единицы первой позиции"))
sum1 = poz1_kol + poz1_cen

poz2_name = input("Название второй позиции ")
poz2_kol = int(input("Количество второй позиции"))
poz2_cen = float(input("Цена единицы второй позиции"))
sum2 = poz2_kol + poz2_cen

dost = float(input("Стоимость доставки "))
summa = float(input("Внесённая сумма "))

obsh_sum = sum1 + sum2
total = dost + obsh_sum
total_kol = poz1_kol + poz2_kol
ostat = summa - total

print("Заказ", zakaz)
print("Заказчик", name)
print("Стоимость товаров", obsh_sum)
print("Общая сумма с доставкой", total)
print("Общее количество единиц", total_kol)
print("Сдача", ostat)
#Магазин электроники
#Алексей
#Кабели
#3
#12.50
#Адаптеры
#2
#20.00
#10.00
#100.00
