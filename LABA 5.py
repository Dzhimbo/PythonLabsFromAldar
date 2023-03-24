# Задания (5.1/5.2/5.3/5.4)
from random import randint
def z1():
    numbers = [3, 7, 12, 18, 25]
    # Запрашиваем у пользователя число
    user_number = int(input("Введите число: "))
    # Проверяем, есть ли число в списке
    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def z2():
    a = list('1234566789')
    s = set([v for v in a if a.count(v) > 1])
    if len(s) > 0:
        print(s)
    else:
        print('отсутвуют')


def z3():
    days_of_week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

    # Запрашиваем у пользователя количество выходных
    num_of_weekends = int(input("Сколько выходных на неделе вы хотите? "))

    # Разбиваем кортеж на рабочие и выходные дни
    weekend_days = days_of_week[-num_of_weekends]
    working_days = days_of_week[:-num_of_weekends]

    # Выводим рабочие и выходные дни
    print("Ваши выходные дни:", ", ".join(weekend_days))
    print("Ваши рабочие дни:", ", ".join(working_days))


def z4():
    a = ['Терновой', 'Савкар', 'Роновой',
         'Гойдов', 'Абобкин', 'Жабкин',
         'Иванов', 'Бурундук',
         'автореева', 'Германов']

    b = ['Картофан', 'Гиппопотам', 'Беляева',
         'Крылов', 'Асассинов', 'Бизевков',
         'Иванов', 'Башмаков', 'Пуджинов', 'Инсайтов']

    c = randint(0, 4)
    d = a[c:c - 5]
    e = b[c:c + 5]
    f = tuple(d + e)
    g = len(f)
    h = "Иванов" in f
    j = f.count("Иванов")
    k = sorted(f)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(j)
    print(k)

z1()
z2()
z3()
z4()