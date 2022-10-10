from CheGit import checkdigit
def Fact(numb):
    listoffac = []
    fac = 2
    while fac * fac <= numb:
        if numb % fac == 0:
            listoffac.append(fac)
            numb = numb // fac
        else:
            fac += 1
    if numb > 1:
        listoffac.append(numb)
    return listoffac
N = checkdigit(input('Введите число для выведения его простых множителей -->'))
print(f"Cписок простых множителей числа {N} - {Fact(N)}")
