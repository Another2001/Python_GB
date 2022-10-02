import random
mylist = [int(i) for i in input(' Задайте список(каждый элемент через пробел ').split()]
print (mylist)
N = input('введите число повторений - ')
while N.isdigit() == False:
    print('введено не число! повторите попытку ввода!')
    N = input()
else:
    N = int(N)
    for i in range(N):
        ran = random.randint(1 , len(mylist))
        t = mylist[ran]
        ran1 = random.randint(1 , len(mylist))
        m = mylist[ran1] 
        while t == m:
            ran = random.randint(1 , len(mylist))
            t = mylist[ran]
            ran1 = random.randint(1 , len(mylist))
            m = mylist[ran1]  
        else:
            t , m = m , t
            print (f"перемешанный список {mylist}")
