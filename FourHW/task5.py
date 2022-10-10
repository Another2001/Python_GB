from CheGit import checkdigit
def writing(f ,r ,f1 ,r1 , f2, w):
    file = open (f,r)
    file1 = open (f1,r1)
    rst = file.readlines()
    ond = file1.readlines()
    polyn = rst[0] + "+" + ond[0]
    file.close
    file1.close
    print(polyn)
    # print('Введите значения x и y для решения многочлена:')     сделать так, чтобы выражение решалось, я не могу сообразить как
    # x = checkdigit(input(' х =>'))
    # y = checkdigit(input(' y =>'))
    # polyn1 = polyn.replace('x' , str(x))
    # polyn1 = polyn1.replace('y' , str(y))
    f = open(f2,w) 
    f.write(f"our polynome: {polyn}")
    f.close 
    # polyn = float(polyn)
    # print(f"Сумма многочлена по заданным x и y => {polyn}")
writing("FourHW/1st_polyn.txt", "r", "FourHW/2nd_polyn.txt", "r" ,'FourHW/result.txt', 'w')

