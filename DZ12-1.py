import csv
from typing import Callable

def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 1):
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError('Пароль слишком короткий')
            if sum(1 for i in password if i.isupper()) < min_uppercase:
                raise ValueError('Пароль должен содержать как минимум указанное количество заглавных букв')
            if sum(1 for i in password if i.islower()) < min_lowercase:
                raise ValueError('Пароль должен содержать как минимум указанное количество строчных букв')
            if sum(1 for i in password if i in "!@#$%^&*()_+-=[]{}|;':,.<>?") < min_special_chars:
                raise ValueError('Пароль должен содержать как минимум указанное количество специальных символов')
            return func(username, password)
        return wrapper
    return decorator

def username_validator(func: Callable) -> Callable:
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError('Имя пользователя не должно содержать пробелов')
        return func(username, password)
    return wrapper

@username_validator
@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
def registr_user2(username: str, password: str) -> None:
    with open('user.csv', 'a', encoding='windows-1251') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow([username, password])

registr_user2('username','SDffhgg88!@hv')