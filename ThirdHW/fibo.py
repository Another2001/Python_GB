def fibo(n):
    fibolist = list()
    if n == 0:
        fibolist.append(0)
    else:
        a = b = 1
        for i in range(n):
            fibolist.append(a)
            b = a + b
            a = b - a
    return fibolist
