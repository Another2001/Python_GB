from CheGit import checkdigit


def realnumb():
    lis = list()
    ranje = checkdigit(input('Укажите кол-во элементов списка -->'))
    for i in range(ranje):
        realstr = input(f"Введите {i+1} вещественное число -->")
        realstr = float(realstr)
        lis.insert(i, realstr)
        # (9 <-0-> 11) while float(realstr) == True: --> не работает :(
        # else:
        #     realstr = input('Введите вещественное число -->')
        #     print('Введены некорректные данные! повторите ввод')
    return lis
