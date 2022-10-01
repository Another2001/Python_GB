list = [2, 3, 5, 9, 3]
sum = 0
stri = ''
for i in len(list + 1):
    if (list[i] % 2 == 1):
        sum += i
        i = str(i)
        stri += i + ", "
print(f"на нечётных позициях элементы - {stri} ответ: {sum}")
