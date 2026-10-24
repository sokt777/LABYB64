text = input("Введите текст: ")
text1 = text.split()

b = []

for i in text1:
    clean = i.strip(".,!?;:").lower()
    if not clean:
        continue
    if "р" in clean:
        b.append(clean)
if not b:
    print("")
    print(0)
elif b:
    for v in b:
        print(v)
    print(len(b))
