# 1) Дан словарь task1/en-ru.txt с однозначным соответствием английских и русских слов в таком формате:
# cat - кошка
# dog - собака
# mouse - мышь
# house - дом
# eats - ест
# in - в
# too - тоже
# Здесь английское и русское слово разделены двумя табуляциями и минусом: '\t-\t'.
# В файле task4/input.txt дан текст для перевода, например:
# Mouse in house. Cat in house.
# Cat eats mouse in dog house.
# Dog eats mouse too.
# Требуется сделать подстрочный перевод с помощью имеющегося словаря и вывести результат в output.txt. Незнакомые словарю слова нужно оставлять в исходном виде.

diction = dict()
with open("dictionary", encoding="utf+8") as fail, open("Text", encoding="utf+8") as fail2, open("Result", "w", encoding="utf+8") as fail3:
    for line2 in fail:
        word = line2.split()
        diction.update({word[0]: word[-1] for _ in word})
    for line in fail2:
        text = line.split()
        for item in text:
            if item.replace(".", "").lower() in diction.keys():
                fail3.write(f"diction.get(item.replace('.', '').lower()) ")
            else:
                fail3.write(f'item.replace(".", "").lower() ')
        fail3.write("\n")

int(input())