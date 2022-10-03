N = input('Задайте кол-во элементов списка: ')
while N.isdigit() == False:
    print('Введено не число! повторите попытку ввода!')
    N = input()
else:
    stri = ''
    sum = 0
    N = int(N)
    lis = list()
    for i in range(N):
        lis.insert(i, input('Введите элемент списка(число) --> '))
        lis[i] = int(lis[i])
        if (i-1) % 2 == 1:                #так визуальнее более правильно :)
            stri += f" {lis[i]} , "
            sum += lis[i]
    print(f"Готовый список: {lis} , на нечётных позициях элементы - {stri} их сумма: {sum}")



