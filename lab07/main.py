from functions import sum_digits, average, normalize_text, select_numbers

print(f"Cумаа цифр числа модуля: {sum_digits(int(input("Введите число: ")))}")
print(f"Среднее арифметическое: {average([int(x) for x in input('Введите числа через пробел или запятую: ').replace(',', ' ').split()])}")
print(f"Нормализированныйтекст: {normalize_text(input("Введите текст: "))}")
print(f"Числа, не равные порогу: {select_numbers(nums, int(input('Введите порог (неотрицательное число): ')))}")