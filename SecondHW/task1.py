N = input()
sum = 0
count = 0
for i in N:
    if i.isdigit():
        sum += int(i)
    else:
        count += 1    # Подразумевается наличие точки как десятичной части числа, но если ввести не более 1 символа    
if count > 1:         # Не являющегося цифрой, код все равно сработает и подсчитает сумму цифр
    print('Это не число, это какой то набор символов! ')
else:
    print(f"сумма цифр в заданном значении = {sum}")
