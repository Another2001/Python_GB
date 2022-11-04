from datetime import datetime as dt


def importing():
    time = dt.now().strftime('%H:%M')
    with open('file_imp.csv', 'r', encoding ='utf-8') as fi:
        fi = [line.split('\n') for line in fi]
    with open('phonebook.csv', 'a', encoding ='utf-8') as file1:
        file1.write(f"\n{time};-->;{fi}")
