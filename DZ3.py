
"""
ДЗ 3
Проверяет, является ли слово палиндромом.
word: Слово, которое нужно проверить.
True, если слово палиндром, False - в противном случае.
"""
"""
Вариант 1
"""
def is_palindrome(word):
  return word == word[::-1]
def main():
  word = input("Введите слово: ")
  if is_palindrome(word):
    print(f'{word} - палиндром.')
  else:
    print(f'{word} - не палиндром.')
if __name__ == "__main__":
  main()

"""
Вариант 2
Функция strip удаляет все начальные и конечные пробелы из строки.
"""

a = input('Введите слово: ').strip().lower()
b = a[::-1].strip().lower()
print(f'Слово "{a}" {"палиндром" if b == a else "не палиндром"}')

