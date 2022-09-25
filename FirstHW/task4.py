range = ['[x > 0 ; y > 0]', '[x < 0 ; y > 0]',
         '[x < 0 ; y < 0]', '[x > 0 ; y < 0]']
quarter = int(input('Введите четверть : '))
while 0 > quarter or quarter > 4:
    print('Неверное число! повторите ввод ')
    quarter = int(input('Введите четверть : '))
else:
    if quarter == 1:
        print(f'Диапозон координат - {range[0]}')
    elif quarter == 2:
        print(f'Диапозон координат - {range[1]}')
    elif quarter == 3:
        print(f'Диапозон координат - {range[2]}')
    elif quarter == 4:
        print(f'Диапозон координат - {range[3]}')
