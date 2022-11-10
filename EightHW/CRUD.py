from createtable import rows_of_table
def new_cols(name):
    f = open(f'database/{name}.csv', 'a')


def selecting(name):
    row_sel = []
    f = open(f'database/{name}.csv', 'r')
    lines = f.readline(0)
    print(lines)
    for i in lines:
        txt = f.readline()
        print(txt)

    # row = input('Какие столбики выбираем?(если их несколько пишите через пробел) -->')
    # for i in row.split():
    #     if i in rows_of_table(name):
    #         row_sel.append(i)
    # data = [cols[i] for i f]
    # return print(sel_total) 

def upd_col(name):
    return name

def del_col(name):
    return name

selecting('mhmh')