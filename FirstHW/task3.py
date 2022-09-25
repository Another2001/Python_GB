quarter = ['1 четверть', '2 четверть', '3 четверть', '4 четверть']
x = int(input('x = '))
y = int(input('y = '))
while x == 0 or y == 0:
    print('Одна из координат равна нулю! повторите ввод')
    x = int(input('x = '))
    y = int(input('y = '))
if x > 0 and y > 0:
    print(quarter[0])
elif x < 0 and y > 0:
    print(quarter[1])
elif x < 0 and y < 0:
    print(quarter[2])
elif x > 0 and y < 0:
    print(quarter[3])
