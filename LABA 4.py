# Задание 4.1
a = int(input('Введите число чтобы узнать делится ли число на 3: '))
if a%3 == 0 and a != 0:
    print('Число', a, 'делится на 3')
else:
    print('Число', a, 'не делится на 3')

def z2():
    # задание 4.2
    try:
        a = int(input('Введите число чтобы узнать, делится ли число на 100 : '))
        b = 100 / a
    except ZeroDivisionError:
        print('Введён 0')
    except ValueError:
        print('Введено не число ')
    else:
        print('100 / 2 = ', b)

def z3(): # Задание 4.3
    a= input("Введите дату чтобы узнать является ли дата магической или нет?: ")
    if int(a[:2]) * int(a[3:5]) == int(a[-2:]):
        print("True")
    else:
        print("False")

def z4(): # Задание 4.4
    a= input("Введите номер билета,чтобы узнать счастливчик ты или неудачник?: ")
    if len(a) % 2 == 1:
            print("увы братец, ты неудачник")
    else:
        b = int(len(a)/2)
        s = 0
        for i in range(b):
            s += int(a[i])
        s2 = 0
        for i in range(b):
            s2 += int(a[-(i+1)])
        else:
            if s == s2:
                print("Это счастливый билет")
            else:
                print("Это не счастливый билет")
z2()
z3()
z4()