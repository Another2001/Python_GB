def negafibo(n):
    negfibolist = list()
    a = 1
    b = -1
    for i in range(n):
        negfibolist.append(a)
        b = a - b
        a = a - b
    return negfibolist
