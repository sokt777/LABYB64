price = int(input('Введите цену одной тетради'))
count = int(input('Введите количество тетрадей'))
paid = int(input('Введите переданную сумму'))
cost = count * price
sdacha = paid - (price * count)
if paid >= price * count:
    print(cost, 'Стоимость')
    print(sdacha, 'Сдача')
else:
    print('У вас не хватает денег')