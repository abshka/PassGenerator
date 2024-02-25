import random
import string


def generate_password(length, include_params):
    chars = string.ascii_letters + string.digits
    if include_params['include_symbols']:
        chars += string.punctuation
    if include_params['include_numbers']:
        chars += string.digits
    if include_params['include_letters']:
        chars += string.ascii_letters
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def generate_multiple_passwords(num_passwords, length, include_params):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, include_params)
        passwords.append(password)
    return passwords


def get_include_params():
    include_symbols = input('Включить символы? (да/нет): ').lower() == 'да'
    include_numbers = input('Включить цифры? (да/нет): ').lower() == 'да'
    include_letters = input('Включить буквы? (да/нет): ').lower() == 'да'
    return {'include_symbols': include_symbols, 'include_numbers': include_numbers, 'include_letters': include_letters}


def get_menu_choice():
    while True:
        try:
            choice = int(input('Введите номер действия: '))
            if 1 <= choice <= 4:
                return choice
            else:
                print('Некорректный ввод. Пожалуйста, введите число от 1 до 4.')
        except ValueError:
            print('Некорректный ввод. Пожалуйста, введите число от 1 до 4.')


def main_menu():
    print('Генератор паролей:')
    print('1. Создать пароль')
    print('2. Создать несколько паролей')
    print('3. Сохранить пароли в файл')
    print('4. Выход')


def save_passwords_to_file(passwords, file_name, num_passwords=1):
    with open(file_name, 'a') as file:
        for password in passwords:
            file.write(f'# {password}\n')


def main():
    while True:
        main_menu()
        choice = get_menu_choice()

        if choice == 1:
            length = int(input('Введите длину пароля: '))
            include_params = get_include_params()
            password = generate_password(length, include_params)
            print(f'Созданный пароль: {password}')
        elif choice == 2:
            num_passwords = int(input('Введите количество паролей: '))
            length = int(input('Введите длину паролей: '))
            include_params = get_include_params()
            passwords = generate_multiple_passwords(num_passwords, length, include_params)
            for i, password in enumerate(passwords):
                print(f'Пароль {i + 1}: {password}')
        elif choice == 3:
            file_name = input('Введите имя файла: ')
            num_passwords = int(input('Введите количество паролей для сохранения: '))
            length = int(input('Введите длину паролей: '))
            include_params = get_include_params()
            passwords = generate_multiple_passwords(num_passwords, length, include_params)
            save_passwords_to_file(passwords, file_name)
            print('Пароли сохранены в файл.')
        elif choice == 4:
            print('До свидания!')
            break
