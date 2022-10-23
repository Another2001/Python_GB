from CheGit import checkdigit
def listrangeint(N):
    lis = list()
    for i in range(N):
        lis.insert(i, checkdigit(input(f"Введите {i+1} элемент списка --> ")))
    return lis