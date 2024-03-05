#часть 1
import csv

class CsvFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self, as_dict=False):
        with open(self.filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            if as_dict:
                headers = data[0]
                data = [dict(zip(headers, row)) for row in data[1:]]
        return data

    def write_file(self, data, as_dict=False):
        with open(self.filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if as_dict:
                headers = list(data[0].keys())
                writer.writerow(headers)
                data = [[row[header] for header in headers] for row in data]
            writer.writerows(data)

    def append_file(self, data, as_dict=False):
        with open(self.filepath, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if as_dict:
                headers = list(data[0].keys())
                if headers not in data:
                    writer.writerow(headers)
                data = [[row[header] for header in headers] for row in data]
            writer.writerows(data)

# Пример использования
csv_handler = CsvFileHandler('data.csv')

# Чтение данных из CSV файла
#data_read = csv_handler.read_file()
#print("Прочитанные данные из CSV файла:")
#print(data_read)

# Запись данных в CSV файл в виде списка списков
data_to_write = [[1, 'John', 'Doe'], [2, 'Jane', 'Smith']]
csv_handler.write_file(data_to_write)

# Дописывание данных в CSV файл в виде списка списков
data_to_append = [[3, 'Alice', 'Johnson'], [4, 'Bob', 'Brown']]
csv_handler.append_file(data_to_append)

# Чтение данных из CSV файла как словарей
data_read_as_dict = csv_handler.read_file(as_dict=True)
print("\nПрочитанные данные из CSV файла как словари:")
print(data_read_as_dict)
