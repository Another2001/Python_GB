def checkdigit(N):
    while N.isdigit() == False:
        N = input('Введено не число! повторите ввод --> ')
    else:
        N = int(N)
        return N
