N = input()
if N.isdigit():
    N = int(N)
    index = ''
    factor = 1
    stroka = ''
    for i in range(N):
        factor = factor * (i+1)
        index = index + f" {i+1}  "
        stroka = stroka + f" {factor}  "
    print(f"числа от 1 до {N}: [{index}] , набор произведений : [{stroka}]")
else:
    print('Введено не число!') 