# def get_fullname():
#     return input('Введите свои ФИО: ')
# def get_phone_number():
#       return input('Укажите свой номер телефона: ')
# def get_description():
#       return  input('Описание(необязательно): ')
# def data_collection():
#     return f"{get_fullname()} , {get_phone_number()}, {get_description()}"
def new_table(name,rows):
    f = open(f'database/{name}.csv', 'w')
    i = 0
    while i < rows:
        i+=1
        f.write(input('Введите наименование столбика: '))
        if i != rows: f.write('                         |')

def rows_of_table(name):
    f = open(f'database/{name}.csv', 'r')
    print(list(f.read().split('                         |')))