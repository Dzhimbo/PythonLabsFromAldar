def z1():
    # 9.1
    from PIL import Image, ImageDraw, ImageFont
    import os

    images_folder = r"D:\kartinki 9lab\\"  # Сюда писать путь до папки, в которой хранятся исходные картинки
    images_saving_folder = r"D:\otrab_kartinki_lab9\\"  # Сюда писать путь до папки, в которой хранятся уже обработанные картинки

    images_list = os.listdir(images_folder)

    for image in images_list:
        img = Image.open(os.path.join(images_folder, image))
        draw = ImageDraw.Draw(img)  # Создаем объект для рисования водяного знака
        font = ImageFont.truetype("arial.ttf", 36)  # Настраиваем шрифт для надписи водяного знака

        text = "ГУРАНЯЯ"  # Задаем текст и цвет водяного знака
        color = (190, 190, 190)

        x = 0  # Располагаем текст в левом верхнем углу изображения
        y = 0

        draw.text((x, y), text, fill=color, font=font)  # Рисуем текст водяного знака на изображении
        img.show()  # Показываем изображение

        if os.path.isdir(images_saving_folder):  # Сохраняем измененное изображение с водяным знаком
            img.save(os.path.join(images_saving_folder, "watermarked_" + image))
        else:
            os.mkdir(images_saving_folder)
            img.save(os.path.join(images_saving_folder, "watermarked_" + image))
def z2():
    # 9.2
    from PIL import Image, ImageDraw, ImageFont
    import os

    images_folder = r"D:\kartinki 9lab\\"  # Сюда писать путь до папки, в которой хранятся исходные картинки
    images_saving_folder = r"D:\otrab_kartinki_lab9\\"  # Сюда писать путь до папки, в которой хранятся уже обработанные картинки

    images_list = os.listdir(images_folder)

    for image in images_list:
        ext = os.path.splitext(image)
        if ext[1] not in ['.jpg', '.png']:
            # Используем format() для форматирования строки
            print("Файл {} с расширением {}. Данное расширение не поддерживается".format(ext[0], ext[1]))
            continue
        else:
            img = Image.open(os.path.join(images_folder, image))
            draw = ImageDraw.Draw(img)  # Создаем объект для рисования водяного знака
            font = ImageFont.truetype("arial.ttf", 36)  # Настраиваем шрифт для надписи водяного знака

            text = "ГУРАНЯЯ"  # Задаем текст и цвет водяного знака
            color = (190, 190, 190)

            x = 0  # Располагаем текст в левом верхнем углу изображения
            y = 0

            draw.text((x, y), text, fill=color, font=font)  # Рисуем текст водяного знака на изображении
            img.show()  # Показываем изображение

            if os.path.isdir(images_saving_folder):  # Сохраняем измененное изображение с водяным знаком
                # Добавляем "\\" к images_saving_folder, чтобы изображение сохранялось в нужной папке
                img.save(os.path.join(images_saving_folder, "watermarked_" + image))
            else:
                # Добавляем "\\" к images_saving_folder и создаем папку, если ее не существует
                os.makedirs(images_saving_folder, exist_ok=True)
                img.save(os.path.join(images_saving_folder, "watermarked_" + image))







def z3():
    import csv

    total_price = 0
    items_list = []

    with open('Товары.csv') as products:
        reader = csv.reader(products)
        headers = next(reader)  # получение заголовков и переход к следующей строке
        print("Нужно купить: ")

        for row in reader:
            try:
                name, quantity, price = row
                quantity = int(quantity)
                price = int(price)
            except ValueError:
                print(f"Ошибка данных в строке: {row}")
                continue

            items_list.append((name, quantity, price))

        for name, quantity, price in items_list:
            total_price += quantity * price
            print(f"{name} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total_price}")


z1()
z2()
z3()
