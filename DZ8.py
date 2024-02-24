# Импортирует модуль json, который позволяет работать с JSON-файлами.
import json
#Импортирует список городов из модуля cities.
from cities import cities_list
# Сортировка cities_list по ключу name
cities = set(city['name'] for city in cities_list)
# Запись набора в JSON
with open('cities.json', 'w', encoding='utf-8') as f:
    json.dump(cities_list, f, indent=4, ensure_ascii=False)
# Чтение набора из JSON
with open('cities.json', 'r', encoding='utf-8') as f:
    cities_list = json.load(f)
print(cities)
