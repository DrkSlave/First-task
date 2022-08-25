from csv import DictReader
from pprint import pprint


def main(csv_file: str) -> 'dict_table'':   # Функция чтения из CSV-файла

    try:
        dict_table = {}     # Создаем пустой словарь для последующей записи в него таблицы судов из файла
        with open(csv_file, encoding='cp1251') as file:     # Открываем файл
            reader = DictReader(file, delimiter=';')    # Читаем таблицу из файла, как словарь,
                                                            # где ключ - заголовок столбца, значение - значение
                                                            # соответствующего столбца
            for index, row in enumerate(reader, 1):         # Перебираем таблицу по строкам
                dict_table[index] = row                     # Создаем словарь с ключем index (начиная с 1) и значением
                                                            # каждой строки таблицы в виде словаря
        return dict_table
    except FileNotFoundError:                               # Если заданного файла нет,
        print('No such file!')                              # вывод: No such file!


def csv_write(text_file: str, table: dict):     # Функция записи таблицы судов в текстовый файл

    r = open(text_file, 'w'); r.close()        # Создаем файл для записи или очещаем файл, если он существует
    with open(text_file, 'a', encoding='cp1251') as file:   # Открываем текстовый файл для записи таблицы
        for row in table.values():          # Перебираем таблицу и
            file.write(str(row) + '\n')     # записываем ее построчно в файл
    print('Copy is end to', text_file)


def value_search(csv_value: str, table: dict):      # Функция поиска в таблице судов по значению
    tmp = 0 # Переменная для проверки правильности ввода данных
    for row in table.values():      # Перебираем строки таблицы
        for key, value in row.items():      # Перебираем ключи и значения строк таблицы
            if value == csv_value:      # Если значение csv_value совпадает со значением в таблице,
                print(row)              # выводим строку из таблицы содержащую значение csv_value
                tmp += 1
    if tmp == 0: # Если введенных данных в таблице нет,
        print('No such value!')  # выводит No such value!



if __name__ == '__main__':

    input_csv = input('Input csv file: ')       # Вводим CSV-файл с таблицей судов
    ship_table = main(input_csv)  # Даем ссылку переменной ship_table на словарь с таблицей

    while True:
        print(' 1. Display the table of ships. \n 2. Write table of ships in txt file. \n 3. Search value in table of ships. \n 4. Exit. ')

        choise = int(input('Choose number of action:'))    #Выбор действия

        if choise == 1:

            pprint(ship_table, sort_dicts=False)     # Вывод таблицы судов

        if choise == 2:

            input_txt = input('Input txt file: ')       # Вводим текстовый файл для записи в него таблицы судов
            csv_write(input_txt, ship_table)        # Вызываем функцию записи таблицы судов в текстовый файл
        if choise == 3:

            input_value = input('Input value: ')        # Вводим элемент для поиска в таблице судов
            value_search(input_value, ship_table)       # Вызываем функцию поиска в таблице судов по значению

        if choise == 4:
            break