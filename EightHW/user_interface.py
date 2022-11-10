from view import show_table
from createtable import *
from CRUD import *

def user_interface():
    print("**** Добро пожаловать в базу данных! *****\n")
    flag = True
    while flag: 
        print("\nВыберите пункт меню для продолжения:")
        while flag == True:
            print("1 - Столбцы указанной таблицы")
            print("2 - Добавить столбец к таблице")
            print("3 - Показать всю информацию таблицы")
            print("4 - Выборка в таблице")
            print("5 - Добавить запись в таблицу")
            print("6 - Обновить запись в таблице")
            print("7 - Удалить запись в таблице")
            print("8 - Новая таблица")
            print("9 - Завершить работу")
            print("10 - Удалить таблицу")
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"]:
                print("!!Выбран неверный пункт меню!!\nПопробуйте ещё раз")
                continue
            elif choice == "1":
                rows_of_table(input('Столбики какой таблицы нужно вывести? --> '))
                break
            elif choice == "2":
                add_row(input('К какой таблице будем добавлять столбик? --> '))
                break
            elif choice == "3":
                show_table(input('Какую таблицу выводим? --> '))
                break
            elif choice == "4":
                selecting(input('Укажите таблицу для выборки --> '))
                break
            elif choice == "5":
                name = input('В какой таблице будем добавлять запись? -->')
                new_cols(name)
                break
            elif choice == "6":
                name = input('В какой таблице будем изменять запись? -->')
                upd_col(name)
                break
            elif choice == "7":
                name = input('В какой таблице будем удалять запись? -->')
                del_col(name)
                break
            elif choice == "8":
                new_table(input('Задайте имя таблицы --> '),input('\nКоличество столбцов -->'))
                break
            elif choice == "10":
                del_table(input('Какую таблицу хотите удалить? --> '))
            elif choice == "9": 
                flag = False
                exit