from CheGit import checkdigit
N = checkdigit(input('укажите кол-во элементов списка -->'))
sum = 0
stri = ''
lis = list()
for i in range(N):
    lis.insert(i, checkdigit(input(f"Введите {i+1} элемент списка(число) --> ")))
    lis[i] = int(lis[i])
    if (i-1) % 2 == 1:  # так визуальнее более правильно :)
        stri += f" {lis[i]} , "
        sum += lis[i]
print(f"Готовый список: {lis} , на нечётных позициях элементы - {stri} их сумма: {sum}")
