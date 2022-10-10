from CheGit import checkdigit
N = checkdigit(input('Введите количество элементов --> '))
numbers = list()
for i in range(N):
    i = checkdigit(input(f"Введите {i+1} число --> "))
    numbers.append(i)


def uniqnum(numbers):
    uniq = []
    for num in numbers:
        if num not in uniq:
            uniq.append(num)
    return uniq


print(f"Заданный список --> {numbers}")
print(f"Cписок уникальных элементов из заданного списка --> {uniqnum(numbers)}")
