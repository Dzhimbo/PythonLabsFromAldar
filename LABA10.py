def z1():
    import json
    with open('файл.json', encoding='utf-8') as f:
        file = json.load(f)
    for product in file['products']:
        print('Название: ', product['name'])
        print('Цена: ', product['price'])
        print('Вес: ', product['weight'])
        if product['available']:
            print('В наличии.')
        else:
            print('Нет в наличии!')
        print('')

def z2():
    import json
    with open('файл.json', encoding='utf-8') as f:
        file = json.load(f)

    new = {}
    new['name'] = input('Введите название: ')
    new['price'] = input('Введите цену: ')
    new['weight'] = input('Введите вес: ')
    new['available'] = input('Товар в наличии? ').lower() == 'да'
    file['products'].append(new)

    with open('файл.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii = False, indent = 4)

    with open('файл.json', encoding='utf-8') as f:
        file = json.load(f)
    for product in file['products']:
        print('Название: ', product['name'])
        print('Цена: ', product['price'])
        print('Вес: ', product['weight'])
        if product['available']:
            print('В наличии.')
        else:
            print('Нет в наличии!')
        print('')

def z3():
    import subprocess


    file = {}
    with open('en-ru.txt', 'r', encoding ='utf-8') as f:
        for line in f:
            en_word, ru_words = line.strip().split('-')
            for ru_word in ru_words.split(','):
                if ru_word not in file:
                    file[ru_word] = [en_word]
                else:
                    file[ru_word].append(en_word)

    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word in sorted(file.keys()):
            en_words=','.join(sorted(file[ru_word]))
            f.write(f'{ru_word}-{en_words}\n')

        filename = "en-ru.txt"

        try:
            subprocess.Popen(["notepad.exe", filename])
        except FileNotFoundError:
            print("Не удалось открыть файл")



z1()
z2()
z3()