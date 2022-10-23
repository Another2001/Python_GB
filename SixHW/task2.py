# from addlist import listrangeint
# from CheGit import checkdigit
# N = checkdigit(input('укажите кол-во элементов списка -->'))
# lis = list(listrangeint(N))
# print(f"Список введенных чисел: {lis}")
# listprod = list()
# for i in range(N):
#     count = N - i - 1
#     if count >= i:
#         sum = lis[i] * lis[count]
#         listprod.insert(i, sum)
# print(f"Произведение пар чисел списка --> {listprod}")

from random import randint
from CheGit import checkdigit
N = checkdigit(input('укажите кол-во элементов списка -->'))
lis = [randint(1, 21) for i in range(N)]
print(f"Список введенных чисел: {list(enumerate(lis,1))}")
listprod = [ ((lis[i] * lis[N - i - 1]))  for i in range(len(lis)) if int(round(N / 2 + 0.1)) > i]
print(f"Произведение пар чисел списка --> {listprod}")
