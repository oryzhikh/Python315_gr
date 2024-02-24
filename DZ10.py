from marvel import full_dict

from pprint import pprint

user_input = input("Введите цифры через пробел: ")
numbers = list(filter(None, map(lambda x: int(x) if x.isdigit() else None, user_input.split())))

filtered_dict = dict(filter(lambda item: item[0] in numbers, full_dict.items()))

directors_set = {movie['director'] for movie in full_dict.values()}

str_years_dict = {key: {k: str(v) if k == 'year' and v is not None else v for k, v in value.items()} for key, value in full_dict.items()}

starts_with_ch_dict = dict(filter(lambda item: item[1]['title'] and item[1]['title'].startswith('Ч'), filter(lambda item: item[1]['year'] is not None, full_dict.items())))

sorted_by_one_param_dict = dict(sorted(full_dict.items(), key=lambda item: int(item[1]['year']) if isinstance(item[1]['year'], int) else float('inf') if item[1]['year'] is not None else float('inf')))

sorted_by_two_params_dict = dict(sorted(full_dict.items(), key=lambda item: (
    int(item[1]['year']) if (isinstance(item[1]['year'], int) or item[1]['year']  is None) else float('inf'),
    item[1]['title'] if item[1]['title'] is not None else ""
)))

filtered_and_sorted_one_liner_dict = dict(sorted(filter(lambda item: item[0] in numbers, full_dict.items()), key=lambda item: int(item[1]['year']) if isinstance(item[1]['year'], int) else float('inf') if item[1]['year'] is not None else float('inf')))

print("Результаты:")
pprint(numbers, indent=2)
pprint(filtered_dict, indent=2)
pprint(directors_set, indent=2)
pprint(str_years_dict, indent=2)
pprint(starts_with_ch_dict, indent=2)
pprint(sorted_by_one_param_dict, indent=2)
pprint(sorted_by_two_params_dict, indent=2)
pprint(filtered_and_sorted_one_liner_dict, indent=2)