from view import show_table
from createtable import rows_of_table , add_row, new_table 
# from view import show_table
# new_table(input('Имя создаваемой таблицы: '),int(input('Введите количество столбиков: ')))
# name = input("Какую таблицу вывести? укажите имя: ")
# show_table(name)
# rows_of_table(name)

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
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
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
            elif choice == "4":
                show_table(input('По какому столбику делаем поиск? --> '))
            elif choice == "5":
                name_table_5 = input('В какой таблице будем добавлять запись? -->')
                new_cols(name_table_5)
            elif choice == "6":
                show_table(input('Какую таблицу выводим? --> '))
            elif choice == "9": 
                flag = False
                exit
user_interface()