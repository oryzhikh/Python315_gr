"""
Критерии проверки номера
Проверка длины номера (11 знаков ровно)
Номер может начинаться на 8 или +7 (плюс не считается знаком)
Проверка на числа - номер должен состоять только из чисел
Проверка должна проходить, если номер записан в любом формате (скобки, тире, +7, с пробелами
между цифрами, с с пробелами в начале и конце строки)
Все ниже перечисленные номера должны пройти проверку.

Вводные данные
+77053183958
+77773183958
87773183958
+(777)73183958
+7(777)-731-83-58
+7(777) 731 83 58

"""
phone_number_not_valid = ''
phone_number = input('Введите номер телефона: ')
if phone_number[0] != "8" and phone_number[0:2] != "+7": # Проверяем, что номер начинается на 8 или +7.
  phone_number_not_valid += 'Номер должен начинаться с 8 или +7\n'
phone_number = phone_number.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('+', '')
if not phone_number.isdigit(): # Проверяем, что номер состоит только из цифр.
  phone_number_not_valid += 'Номер должен состоять только из цифр\n'
if len(phone_number) != 11:  # Проверяем длину номера.
  phone_number_not_valid += 'номер должен состоять из 11 символов\n'
if phone_number_not_valid:
  print(f'Номер {phone_number} не прошел проверку. Причины:\n{phone_number_not_valid}')
else:
  print(f'Номер {phone_number} прошел проверку')


"""
Критерии проверки пароля
Должен содержать хотя бы один спецзнак
Не должен содержать пробел
Должен содержать символы разных регистров (большие и маленькие)
Должен быть более 7 символов длиной

"""

not_validate_password = ''
validate_password = input('Введите ваш пароль: ')
if " " in validate_password:
    not_validate_password = 'Пароль не должен содержать пробелов\n'
    # Проверяем, что пароль достаточно длинный.
if len(validate_password) < 8:
    not_validate_password += 'Пароль должен состоять не менее чем из 8 символов\n'
    # Проверка на спецзнаки
if  validate_password.isalnum():
    not_validate_password += 'Вы не использовали символы\n'
if validate_password.islower():
    not_validate_password += 'Пароль должен содержать буквы в верхнем регистре\n'
if validate_password.isupper():
    not_validate_password += 'Пароль должен содержать буквы в нижнем регистре\n'
if not_validate_password:
    print(f'Номер {validate_password} не прошел проверку. Причины:\n{not_validate_password}')
else:
    print(f'Номер {validate_password} прошел проверку')