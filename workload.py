par_math = 3
min_math = 90
par_fiz = 2
min_fiz = 90
dost_hours = 10

math_min = par_math * min_math
fiz_min = par_fiz * min_fiz
total_min = fiz_min + math_min
total_hours = total_min/60
ostatok = dost_hours - total_hours
math_hours = math_min/60
fiz_hours = fiz_min/60


nagruz_for4_weak = total_hours * 4

print('количество занятий в неделю по Математике', par_math)
print('количество занятий в неделю по Физике', par_math)
print('1 пара по математике', min_math, 'минут')
print('1 пара по физика', min_fiz, 'минут')
print('Доступное время на неделю', dost_hours , 'часов')
print('Общая нагрузка по математике',math_hours ,'часов')
print('Общая нагрузка по физике', fiz_hours ,'часов')
print('Общая нагрузка по математике', math_min ,'минут')
print('Общая нагрузка по физике',fiz_min  ,'минут')
print('Остаток времени', ostatok , 'часов')
print('Нагрузка за 4 недели', nagruz_for4_weak , 'часов')
