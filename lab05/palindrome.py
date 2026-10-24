
text = input("Введите текст: ")
text1 = text.replace(" ","")
if not text1:
    print("Нет текста")
else:
    if text1 == text1[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")