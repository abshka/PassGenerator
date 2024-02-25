# Пароль-генератор на Python

Простой пароль-генератор на Python, который позволяет создавать пароли с разной длиной и набором символов.

## Установка

Скопируйте код из файла `password_generator.py` и вставьте его в свой проект.

## Использование

1. Импортируйте функции из модуля `password_generator`:

```python
from password_generator import get_menu_choice, main_menu, main
```

2. Запустите функцию main() для начала работы с генератором паролей:
   
```python
if __name__ == '__main__':
    main()
```

3. Введите номер действия, которое вы хотите выполнить:
  1) Создать пароль
  2) Создать несколько паролей
  3) Сохранить пароли в файл
  4) Выход
   
4. В зависимости от выбранного действия, выполните соответствующие действия:
* Создать пароль: введите длину пароля и настройки включения символов, цифр и букв. Генератор создаст пароль и выведет его на экран.
* Создать несколько паролей: введите количество паролей, длину паролей и настройки включения символов, цифр и букв. Генератор создаст и выведет все пароли.
* Сохранить пароли в файл: введите имя файла, количество паролей для сохранения, длину паролей и настройки включения символов, цифр и букв. Генератор создаст пароли, сохранит их в файл и выведет сообщение о успешном сохранении.
* Выход: закройте генератор паролей.

  
# Примеры кода
## Пример использования функций из модуля password_generator:

```python
from password_generator import get_menu_choice, main_menu, main

if __name__ == '__main__':
    main()
```
### Пример создания пароля:

```python
from password_generator import generate_password

length = 10
include_params = {'include_symbols': True, 'include_numbers': True, 'include_letters': True}
password = generate_password(length, include_params)
print(f'Созданный пароль: {password}')
```

### Пример создания нескольких паролей:

```python
from password_generator import generate_multiple_passwords

num_passwords = 5
length = 10
include_params = {'include_symbols': True, 'include_numbers': True, 'include_letters': True}
passwords = generate_multiple_passwords(num_passwords, length, include_params)
for i, password in enumerate(passwords):
    print(f'Пароль {i + 1}: {password}')
```

### Пример сохранения паролей в файл:

```python
from password_generator import save_passwords_to_file

passwords = ['password1', 'password2', 'password3']
file_name = 'passwords.txt'
save_passwords_to_file(passwords, file_name)
print('Пароли сохранены в файл.')
```
