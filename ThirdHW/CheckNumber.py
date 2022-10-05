from CheGit import checkdigit


def checkisnumb():
    lis = list()
    ranje = checkdigit(input('Укажите кол-во элементов списка -->'))
    for i in range(ranje):
        realstr = input('Введите вещественное число -->')
        count = 0
        sum = ''
        for j in realstr:
            if j.isdigit() or "." in realstr:
                sum += j 
                print(sum)
            else:    
                lis[i] = 'Введенны некорректные данные'
                #realstr = input('Введено не вещественное число! повторите ввод --> ')
        sum = float(sum)
        lis.insert(i, sum)
    return lis

listi = checkisnumb()
print(f"Наш список вещественных чисел--> {listi}")
