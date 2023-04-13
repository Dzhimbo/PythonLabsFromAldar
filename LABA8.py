# 1 задание
def z1():

    from PIL import Image
    filename = "1970-01-01 03-00-00_1613973847164.JPG"
    image = Image.open(filename)  # С помощью функции интерпретатора (ImageOpen) открываем пнг файл
    image.show("1970-01-01 03-00-00_1613973847164.JPG")
    # Загрузите изображение
    filename = Image.open("1970-01-01 03-00-00_1613973847164.JPG")
    # Задайте координаты области, которую хотите обрезать
    left, upper, right, lower = 100, 100, 500, 300
    # Обрежьте изображение с заданными координатами (левый верхний угол, правый нижний угол)
    cropped_image = filename.crop((left, upper, right, lower))

    # Сохраните обрезанное изображение под новым именем
    cropped_image.save("new_1970-01-01 03-00-00_1613973847164.JPG")
    cropped_image.show("new_1970-01-01 03-00-00_1613973847164.JPG")


# 2 задание
def z2():

    from PIL import Image

    #словарь с праздниками и именами файлов
    holiday_dict = {
        "Новый год": "new_year.jpg",
        "День рождения": "birthday.jpg",
        "Пасха": "пасха.jpg",
        "Хеллоуин": "halloween.jpg",
        # добавьте другие праздники и имена файлов
    }

    #вводим название праздника
    holiday = input("Введите название праздника: ")

    #если праздник есть в словаре, то открываем изображение
    if holiday in holiday_dict:
        image_path = holiday_dict[holiday]
        image = Image.open(image_path)
        image.show()
    else:
        print("Праздник не найден")

# 3 задание
def z3():

    from PIL import Image, ImageDraw, ImageFont

    # Загрузите изображение
    image = Image.open("birthday.jpg")
    # Создайте объект для рисования
    draw = ImageDraw.Draw(image)
    # Введите имя человека, которого хотите поздравить
    name = input("Введите имя человека, которого хотите поздравить: ")
    # Задайте текст
    text = f"{name}, поздравляю!"

     # Выберите шрифт и размер
    font = ImageFont.truetype("ofont.ru_Montserrat Alternates.ttf", 25)

    # Выберите цвет и положение текста
    color = (0, 0, 0)  # белый цвет
    position = (image.width / 3 - 40, image.height / 3)

    # Нарисуйте текст на изображении
    draw.text(position, text, fill=color, font=font)

    # Сохраните новую открытку с расширением .png
    image.save("greeting_card.png")
    image.show("greeting_card.png")


z1()
z2()
z3()
