#часть 3
class TxtFileHandler:
    def read_file(self, filepath):
        """Метод для чтения данных из TXT файла.

        Args:
            filepath (str): Путь к файлу.

        Returns:
            str: Данные из TXT файла.
        """
        with open(filepath, 'r') as f:
            data = f.read()
        return data

    def write_file(self, filepath, data):
        """Метод для записи данных в TXT файл.

        Args:
            filepath (str): Путь к файлу.
            data (str): Данные для записи.
        """
        with open(filepath, 'w') as f:
            f.write(data)

    def append_file(self, filepath, data):
        """Метод для дописывания данных в TXT файл.

        Args:
            filepath (str): Путь к файлу.
            data (str): Данные для дозаписи.
        """
        with open(filepath, 'a') as f:
            f.write(data)

# Пример использования класса TxtFileHandler
handler = TxtFileHandler()

# Чтение данных из файла
#read_data = handler.read_file("data.txt")

# Запись данных в файл
handler.write_file("data.txt", "Новые данные")

# Дописывание данных в файл
handler.append_file("data.txt", "\nДополнительные данные")