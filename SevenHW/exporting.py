def exporting():
    file1 =  open('file_exp.csv' , 'a', encoding='utf-8') 
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if len(line) != 1:
                f = f + line
                file1.write(f"{line}")

def take_text():
    f = []
    with open('phonebook.csv', 'r', encoding='utf-8') as file:        
        for line in file:
            f.append(line)
    return f