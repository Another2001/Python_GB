# import user_interface as ui
# ui.rows_of_table()

from createtable import new_table, rows_of_table
from view import show_table
# new_table(input('Имя создаваемой таблицы: '),int(input('Введите количество столбиков: ')))
name = input("Какую таблицу вывести? укажите имя: ")
show_table(name)

