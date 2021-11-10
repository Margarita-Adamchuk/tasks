# 2)Дан список стран и языков на которых говорят в этой стране в формате <Название Страны> : <язык1> <язык2> <язык3> ... в файле task2/input.txt.
# На ввод задается N - длина списка и список языков. Для каждого языка укажите, в каких странах на нем говорят.
# Ввод
# 3
# Вывод
# азербайджанский  Азербайджан
# греческий  Кипр Греция
# китайский  Китай Сингапур
my_list = [input("Введите язык:  ") for _ in range(int(input("Сколько языков будем проверять: ")))]
x = []
with open("language", encoding="utf+8") as fail:
    for item2 in my_list:
        for line in fail:
            word = line.split()
            for item in word:
                if item2 == item.replace(",", ""):
                    x.append(word[0].replace(":", ""))


        print(f"{item2} {x}")




