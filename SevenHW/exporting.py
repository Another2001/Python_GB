from datetime import datetime as dt
def exporting():
    time = dt.now().strftime('%H:%M')
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        file = [line.split('\n') for line in file]
    with open('file_exp.csv' , 'a', encoding='utf-8') as file1:
        file1.write(f"\n{time};-->;{file}")

        
