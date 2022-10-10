import random
from CheGit import checkdigit
def coefs (K , file, type): 
    amount = checkdigit(input('Введите кол-во элементов для определения коэффициентов --> '))
    f1 = open (file , type)
    f1.write('Examp of coef in a polyn:\n')
    for i in range(amount):
        T = f"{random.randint(0 , 100)}x^{K} + {random.randint(0 , 100)}X + {random.randint(0 , 100)}\n"
        f1.write(T)
    f1.close
coefs(checkdigit(input('Введите натуральную степень(число) --> ')),"FourHW/polyn_for_4_task", "w" )
# NX**K+NX+N