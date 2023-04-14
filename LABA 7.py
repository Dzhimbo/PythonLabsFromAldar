# Задание 1
def z1():

    from PIL import Image

    # Вставляем в проект питона наш пнг файлик.
    filename = "43bcfa0a83.png"
    image = Image.open(filename) # С помощью функции интерпретатора (ImageOpen) открываем пнг файл
    image.show("43bcfa0a83.png")
    width, height = image.size # задаем картинке ширину и высоту с помощью функции размера(size)
    print("Размер изображения: {}px x {}px".format(width, height)) # Выводим изображение и приписываем ему формат в пикселях
    format = image.format
    print("Формат файла: {}".format(format))

# Задание 2
    mode = image.mode # задаем цветовую модель изображения
    print("Цветовая модель: {}".format(mode))
    # Уменьшение изображения в 3 раза
    new_size =(width// 3, height // 3)
    small_image = image.resize(new_size)
    small_image.save('small_image.png') # сохранение

    # отражаем картинку по вертикали и горизонтали
    horizontal_mirror_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    horizontal_mirror_image.save('horizontal_mirror.png') # сохранение
    vertical_mirror_image = image.transpose(method=Image.FLIP_TOP_BOTTOM)
    vertical_mirror_image.save('vertical_mirror.png') # сохранение
    horizontal_mirror_image.show('horizontal_mirror.png')
    small_image.show('small_image.png')
    vertical_mirror_image.show('vertical_mirror.png')


# Задание 3
def z2():
    from PIL import Image, ImageFilter

    filenames = ['1.JPG', '2.JPG', '3.JPG', '4.jpg', '5.jpg']
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save('new' + file)


# Задание 4

def z3():
    from PIL import Image, ImageDraw, ImageFont

    kartinki = ["bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg", "6798fddd7c080e727bc631370c87c64f.png", "D_J_Y7dxxcU.jpg"]

    for image in kartinki:
        # Открываем изображение
        img = Image.open(image)

        # Создаем объект для рисования водяного знака
        draw = ImageDraw.Draw(img)

        # Настраиваем шрифт для надписи водяного знака
        font = ImageFont.truetype("arial.ttf", 36)

        # Задаем текст и цвет водяного знака
        text = "ГУРАНЯЯ"
        color = (190, 190, 190)

        # Вычисляем размер текста в пикселях
        text_width, text_height = draw.textsize(text, font)

        # Располагаем текст в левом верхнем углу изображения
        x = 0
        y = 0

        # Рисуем текст водяного знака на изображении
        draw.text((x, y), text, fill=color, font=font)

        # Показываем изображение
        img.show()

        # Сохраняем измененное изображение с водяным знаком
        img.save("watermarked_" + image)

z1()
z2()
z3()
