print(
    'Это программа для зашифровки и расшифровки шифра Цезаря\nПожалуйста выберите что вам необходимо сделать('
    'a-зашифровать,b-расшифровать)\n')
question = input()


# Второй алфавит на случай если шифруем последние буквы которые выйдут за алфавит
def encrypt_func():
    alphabet_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_ru = 'абвгдежзийклмнопрстуфхцчъыьэюяабвгдежзийклмнопрстуфхцчъыьэюя'
    encrypt = input('Введите текст\n')
    encrypt = encrypt.lower()
    if encrypt[0] in alphabet_en:
        key = int(input('Введите ключ для зашифровки(от 1 до 26)\n'))
        if key > 25:
            print('ключ больше 25')
            exit()
        encrypted = ''
        # Проход по каждой букве и присваивание ей нового номера
        for letter in encrypt:
            position = alphabet_en.find(letter)
            new_position = position + key
            if letter in alphabet_en:
                encrypted += alphabet_en[new_position]
            else:
                encrypted += letter
        print(encrypted)
    elif encrypt[0] in alphabet_ru:
        key = int(input('Введите ключ для зашифровки(от 1 до 32)\n'))
        if key > 32:
            print('ключ больше 32')
            exit()
        encrypted = ''
        # Проход по каждой букве и присваивание ей нового номера
        for letter in encrypt:
            position = alphabet_ru.find(letter)
            new_position = position + key
            if letter in alphabet_ru:
                encrypted += alphabet_ru[new_position]
            else:
                encrypted += letter
        print(encrypted)


def encrypted_func():
    alphabet_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypt1 = input('Введите текст\n')
    encrypt1 = encrypt1.lower()
    if encrypt1[1] in alphabet_en:
        key1 = int(input('Введите ключ для расшифровки(от 1 до 25)\n'))
        if key1 > 25:
            print('ключ больше 25')
            exit()
        encrypted1 = ''
        # Проход по каждой букве и присваивание ей нового номера
        for letter1 in encrypt1:
            position1 = alphabet_en.find(letter1)
            new_position1 = position1 - key1
            if letter1 in alphabet_en:
                encrypted1 += alphabet_en[new_position1]
            else:
                encrypted1 += letter1
        print(encrypted1)
    elif encrypt1[1] in alphabet_ru:
        key1 = int(input('Введите ключ для расшифровки(от 1 до 32)\n'))
        if key1 > 32:
            print('ключ больше 32')
            exit()
        encrypted1 = ''
        # Проход по каждой букве и присваивание ей нового номера
        for letter1 in encrypt1:
            position1 = alphabet_ru.find(letter1)
            new_position1 = position1 - key1
            if letter1 in alphabet_ru:
                encrypted1 += alphabet_ru[new_position1]
            else:
                encrypted1 += letter1
        print(encrypted1)
    else:
        print('Ошибка')

if question == 'a':
    encrypt_func()
elif question == 'b':
    encrypted_func()
else:
    print('Ошибка ввода')
    exit()
