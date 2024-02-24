import json #Импортирует jsonмодуль для работы с данными JSON.
from typing import List, Dict, Any, Set #импортирует подсказки по типам для ясности и возможной проверки типов.
CITIES_JSON = 'cities.json' #определяет константу для пути к файлу JSON, хранящему названия городов.
print("Игра в города.\n")
def write_cities_to_json(cities_list: List[Dict[str, Any]], file_path=CITIES_JSON) -> None:
    data = [city['name'] for city in cities_list]
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_cities_from_json(file_path: str = CITIES_JSON) -> Set[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    city_names = [city['name'] for city in data]
    return set(city_names)

def get_unique_letters_set(cities_set: Set[str]) -> Set[str]:
    return set(''.join(cities_set).lower())

def get_bad_letters_set(cities_set: Set[str], unique_letters_set: Set[str]) -> Set[str]:
    bad_letters_set = set()
    for letter in unique_letters_set:
        if all(city[0].lower() != letter for city in cities_set):
            bad_letters_set.add(letter)
    return bad_letters_set

def is_last_letter_match(first_city: str, second_city: str) -> bool:
    return first_city[-1].lower() == second_city[0].lower()

def main() -> None:
    cities_set = read_cities_from_json()
    unique_letters_set = get_unique_letters_set(cities_set)
    bad_letters_set = get_bad_letters_set(cities_set, unique_letters_set)
    computer_city = None

    while True:
        user_city = input('Введите город: ').strip().title()

        if user_city == '0':
            print('Ты проиграл')
            break

        if user_city not in cities_set:
            print('Такого города нет')
            break

        if computer_city:
            if not is_last_letter_match(computer_city, user_city):
                print('Не та буква')
                break

        cities_set.remove(user_city)

        last_user_letter = user_city[-1]

        for city in cities_set:
            if is_last_letter_match(user_city, city):
                if city[-1].lower() in bad_letters_set:
                    continue

                cities_set.remove(city)
                print(f'ПК: {city}')
                computer_city = city
                break
        else:
            print('Ты выиграл ')
            break

if __name__ == '__main__': #вызывает main()функцию для запуска игры.
    main()