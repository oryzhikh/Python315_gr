#часть 2
import json


class JsonFileHandler:
    def read_file(self, filepath, as_dict=False):
        """Метод для чтения данных из JSON файла.

        Args:
            filepath (str): Путь к файлу.
            as_dict (bool): Флаг, определяющий формат данных.

        Returns:
            list or dict: Данные из JSON файла.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        if as_dict:
            return data
        else:
            return list(data.values())

    def write_file(self, filepath, data, as_dict=False):
        """Метод для записи данных в JSON файл.

        Args:
            filepath (str): Путь к файлу.
            data (list or dict): Данные для записи.
            as_dict (bool): Флаг, определяющий формат данных.
        """
        if as_dict:
            data = {key: value for key, value in data.items()}
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def append_file(self, filepath, data):
        """Метод для дописывания данных в JSON файл.

        Args:
            filepath (str): Путь к файлу.
            data (list or dict): Данные для дозаписи.

        Raises:
            TypeError: Ошибка, если тип файла не поддерживает дозапись.
        """
        raise TypeError("Дозапись данных в JSON файл не поддерживается.")


# Пример использования класса JsonFileHandler
handler = JsonFileHandler()

# Чтение данных из файла
#data = handler.read_file("data.json")

# Запись данных в файл
handler.write_file("data.json", {"key": "value"})

# Попытка дозаписи данных в файл (вызовет исключение)
try:
    handler.append_file("data.json", {"key": "value"})
except TypeError as e:
    print(e)