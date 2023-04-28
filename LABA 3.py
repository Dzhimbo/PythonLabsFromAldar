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

# Задание (3.4) 
def p3()
        import random
        def generate_expression():
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            expression = f"{a} + {b} = "
            answer = a + b
            return expression, answer


        correct_answers = 0
        mistake_count = 0
        while mistake_count < 3:
            expression, answer = generate_expression()
            user_answer = input(expression)
            if int(user_answer) == answer:
                print("Правильно!")
                correct_answers += 1
            else:
                print("Ответ неверный")
                mistake_count += 1
      print(f"Игра окончена. Правильных ответов: {correct_answers}")
    
p1()
p2()
p3()
