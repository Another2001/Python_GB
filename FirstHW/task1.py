day = int(input('Введите число от 1 до 7 : '))
while 0 > day or day > 7:
    day = int(input('Неверное число! повторите ввод : '))
if day == 6 or day == 7:
    print('Да, это выходной)')
else:
    print('Нет, будни :*(')
