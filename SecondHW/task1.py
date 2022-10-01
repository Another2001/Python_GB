N = input()
sum = 0
count = 0
for i in N:
    if i.isdigit():
        sum += int(i)
    else:
        count += 1
if count > 1:
    print('Это не число, это какой то набор символов! ')
else:
    print(f"сумма цифр в заданном значении = {sum}")
