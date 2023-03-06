# Задание (3.1)
N = int(input("Введите количество слов: "))
result = ""
for i in range(N):
    word = input("Введите слово: ")
    result += word + " "
print("Результат:", result)

def p1():
# Задание (3.2)
    result = ""
    while True:
        word = input("Пишите слова, пока вам не надоест. Если надоест, напишите stop: ")
        if word.lower() == "stop":
            break
        result += word + " "


print("Результат:", result)


def p2():
    # Задание (3.3)

    word = input("Введите слово, которое считается редким (обычно это слова на Ф или f): ")
    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


p1()
p2()
