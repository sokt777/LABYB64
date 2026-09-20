total_seconds = int(input("Введите количество секунд "))
hours = abs(total_seconds) // 3600
ostatok = total_seconds % 3600
min = ostatok // 60
sek = ostatok % 60
print(hours,'ч' , min , 'мин', sek, 'c')