N = input()
while N.isdigit() == False:
    print('введено не число! повторите попытку ввода!')
    N = input()
else:
    lis = list()
    sum = 0
    posl = 0
    stri = ''
    N = int(N)
    for i in range(N):
        posl = round(((1+1)/(i+1))**(i+1),3) # при n = 1 будет 2/1 в степени 1 то есть "2" ,; а при n = 2 уже 2/2 и в степени 2, то есть 1^2 = 1...на сайте неверный пример?
        sum += posl                          # 2 + 1 + 0.28 + 0.0625 + 0.01024
        stri = f" {i + 1}: {sum}"
        lis.insert(i, stri) 
    print(f"сумма последовательности (1+1/n)^n от 1 до {N} для каждого элемента = {lis} ")

    