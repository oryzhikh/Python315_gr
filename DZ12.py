from typing import Callable

len_threshold = 8
digit_threshold = 1
uppercase_threshold = 1
lowercase_threshold = 1
spec_symbol_threshold = 1
spec_symbols = "!@#$%^&*()_+{}|:\"<>?"

def password_checker(func: Callable) -> Callable:
    def wrapper(password: str) -> str:
        if len(password) < len_threshold:
            return "Длина пароля слишком короткая."
        if sum(1 for i in password if i.isdigit()) < digit_threshold:
            return "Пароль должен содержать хотя бы одну цифру."
        if sum(1 for i in password if i.isupper()) < uppercase_threshold:
            return "Пароль должен содержать хотя бы одну заглавную букву."
        if sum(1 for i in password if i.islower()) < lowercase_threshold:
            return "Пароль должен содержать хотя бы одну строчную букву."
        if sum(1 for i in password if i in spec_symbols) < spec_symbol_threshold:
            return "Пароль должен содержать хотя бы один специальный символ."
        return func(password)
    return wrapper

@password_checker
def register_user(password: str) -> str:
    return f"Пользователь {password} успешно зарегистрирован."

new_password = input("Введите пароль: ")
result = register_user(new_password)
print(result)