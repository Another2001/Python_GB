from CheGit import checkdigit
n = checkdigit(input('Введите число для перевода его в двоичную СС --> '))
b = ''
while n > 0:
    b += str(n % 2)
    n = n // 2
print(f" Число в двоичной СС --> {b}")
