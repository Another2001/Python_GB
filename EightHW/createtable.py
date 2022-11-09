# def get_fullname():
#     return input('Введите свои ФИО: ')
# def get_phone_number():
#       return input('Укажите свой номер телефона: ')
# def get_description():
#       return  input('Описание(необязательно): ')
# def data_collection():
#     return f"{get_fullname()} , {get_phone_number()}, {get_description()}"

def rows_of_table(name):
    f = open(f'database/{name}.csv', 'r')
    p = f.readlines()
    m = list(p[0].replace('\n',"").split('                         |'))
    print(m[0:-1])
    # print(m[0]) работает
    return m

def new_table(name,rows):
    f = open(f'database/{name}.csv', 'w')
    i = 0
    while i < rows:
        i+=1
        f.write(input('Введите наименование столбика: '))
        if i != rows: f.write('                         |')

def add_row(name):
    f = open(f'database/{name}.csv', 'r')
    row = input('Имя нового столбика: ')
    lines = f.readlines()
    line_of_1 = list(lines[0].replace('\n','').split('                         |'))
    line_of_1.append(row)
    f.close
    f = open(f'database/{name}.csv', 'w')
    for i in line_of_1:
        f.writelines(f"{i}                         |")
    f.writelines(lines[1:])