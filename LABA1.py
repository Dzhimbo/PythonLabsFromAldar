
 # 1 ЛАБА=ЗАДАНИЯ (A,Б,В,Г,Д)

# Задание (А):
password = input('ВВЕДИТЕ НОВЫЙ ПАРОЛЬ:')
if len(password) < 5:
    print('пароль слишком мал..')
    exit()
elif password[0:6] == "qwerty":
    print('НЕНАДЕЖНЫЙ ПАРОЛЬ!')
    exit()
else:
    print("OK.")
password = input('Повторите пароль:')
print('Введите пароль:')
PasswordConfim = input()
if PasswordConfim == password:
    print('Пароль совпадает, добро пожаловать, Сэр.')
else:
    print('Пароль не совпадает!')


def p1():
    place = int(input('Введите номер места в вагоне:'))
    if place % 2 != 0 and place <= 54:
        print('Нижнее боковое Купе')
    if place % 2 == 0 and place >= 36:
        print('Вверхний плацкарт')
    elif place % 2 == 0 and place <= 35:
        print('Нижний плацкарт')
    if place % 2 == 0 and place <= 54:
        print('Нижнее боковое купе')
    else:
        print('Вверхнее боковое купе')

def p2():

    year = int(input("Введите год, чтобы вычислить является ли год высокосным:"))
    print('Код считает, что год :')
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Высокосный')
    else:
        print('Невысокосный')




def p3():

# Задание (Г)
 color_list = ['Красный', 'Синий', 'Желтый']
 print('Введите 2 значения из 3 цветов (Красный,Синий,Желтый):')
 firstColor, secondColor = input(), input()
 if firstColor not in color_list and secondColor not in color_list:
     print('Ошибка палитры')
 elif firstColor == color_list[0] and secondColor == color_list[1]:
     print('Вы получили фиолетовый цвет')
 elif firstColor == color_list[1] and secondColor == color_list[0]:
     print('Вы получили фиолетовый цвет')
 elif firstColor == color_list[0] and secondColor == color_list[2]:
     print('Вы получили оранжевый цвет')
 elif firstColor == color_list[2] and secondColor == color_list[0]:
     print('Вы получили оранжевый цвет')
 elif firstColor == color_list[1] and secondColor == color_list[2]:
     print('Вы получили зелёный цвет')
 elif firstColor == color_list[2] and secondColor == color_list[1]:
     print('Вы получили зеленый цвет')

 else:

     print('Стоп че? Погоди.. Го еще раз, я не успел записать цвета..')

def p4():

# Задание (Д)

 words: str = ""
 word = input('Начинайте вводить слова, а их соединю вместе:')
 while word != "Stop":
     words = words + str(word) + ' '
 word = input()

 print('words')


p1()
p2()
p3()
p4()
