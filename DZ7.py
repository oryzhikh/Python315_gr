#Импорт библиотеки cities, которая содержит список городов для игры.
from cities import cities_list
#создание symbols_bad, содержащего символы, которые не могут быть первыми буквами в названии города.
symbols_bad = {"ь", "ъ", "ы", "ц", "й"}
#Создание cities содержащего все города из списка cities_list.
cities = set(city["name"] for city in cities_list)
#Вывод сообщения о начале игры и условиях игры.
print("Игра в города.\nЧто бы закончить игру введите слово стоп.\nЕсли пользователь ввёл стоп - он проиграл компьютеру.")
#Иницилизация переменной game, отвечающей за то, продолжаеться ли игра.
game = False
# Первый ход - делает компьютер
city = next(iter(cities)) #Извлекает первый элемент из cities.
print(city) #Выводит название города на экран.
word = city[-1] #Сохраняет последнюю букву названия города в переменную word.
step = "user" #Устанавливает значение переменной step равным "user", что означает что следующий ход делает пользователь.
cities_list.append(city) #Добавляет город, сделанный компьютером, в список cities_list.

moves_user = 0
moves_ai = 0

#Цикл, в котором происходит ход пользователя.
#Значение переменной correct равным False, пока пользователь не введёт правильный город.
#Цикл, в котором пользователь вводит название города.
#Если пользователь вводит слово "стоп", игра заканчивается.
#Если название города начинается с нужной буквы, переменная correct получает значение True.
#Если название города не начинается с нужной буквы, пользователю выводится сообщение об ошибке.
#Проверка того, что такой город существует и что его ещё не называли.
#Устанавливает значение переменной step равным "AI", что означает, что следующий ход делает компьютер.


while game == False:
    if step == "user":
        correct = False
        while correct == False:
            city = input("Введите ваш город: на букву: " + word + ". Ваш город: ")
            if city == "стоп":
                game = True
                correct = True
            else:
                correct = city[0].lower() == word
                if not correct:
                    print("Не верно. Назовите город на букву", word)

        # Проверить что такой город существует
        if city not in cities:
            correct = False
            print("Не верно!!! Такого города не существует!!!")

        # Проверить что ранее этот город не называли
        if city in cities_list:
            correct = False
            print("Не верно. Такой город уже называли")

        step = "AI"
        moves_user += 1

#Цикл в котором происходит ход компьютера.
#Цикл, в котором компьютер ищет город, начинающийся с буквы word.
#Если такой город не найден, игра заканчивается, и пользователю выводится сообщение о победе.
#Если такой город найден, компьютер называет его и устанавливает значение переменной step равным "user", что означает, что следующий ход делает пользователь.
    

    else:
        city = ""
        for city_next in cities:
            if city_next[0].lower() == word:
                city = city_next
                break
        if city == "":
            print("Вы победили")
            print("Не найден город на букву", word)
            game = True
        else:
            print(city)
            step = "user"
            moves_ai += 1

#Эти строки кода являются частью  цикла, который отвечает за повторение игры до тех пор,
#пока не будет объявлен победитель.Код внутри инструкции if выполняется, если игра еще не закончена.


    if game == False:
        cities.remove(city)   #Удаляет недавно сыгранный город из набора городов
        cities_list.append(city)   #Добавляет недавно сыгранный город в список cities_list, в котором хранятся все города, в которые были сыграны на данный момент.
        word = city[-1]    #В этой строке извлекается последняя буква недавно воспроизведенного города и сохраняется в переменной word.
        if word in symbols_bad:   #Эта строка проверяет, содержится ли последняя буква недавно воспроизведенного города в наборе symbols_bad, который содержит специальные символы, которые не могут быть первой буквой названия города.
            word = city[-2]   #Если последняя буква находится в наборе symbols_bad, в этой строке переменной word присваивается предпоследняя буква города.
        if word in symbols_bad:   #та строка такая же, как и предыдущая, но она проверяет, есть ли предпоследняя буква также в наборе symbols_bad.
            word = city[-3]   #Если и последняя буква, и предпоследняя буква находятся в наборе symbols_bad, в этой строке переменной word присваивается предпоследняя буква города.
    else:
        pass

if moves_user < moves_ai:
    print("Победитель: Пользователь")
else:
    print("Победитель: Компьютер")