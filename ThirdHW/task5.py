from fibo import fibo
from negafibo import negafibo
from CheGit import checkdigit
N = checkdigit(input('Введите границу ряда Фибоначчи --> '))
print(f"Cписок чисел Фибоначчи, в том числе для отрицательных индексов --> {list(reversed(negafibo(N))) +fibo(0) + fibo(N)}")
