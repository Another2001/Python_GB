import time
import json

def read_from_json(path_to_file,db_list):  
    with open(path_to_file, "r", encoding="UTF-8") as file:
        text = file.read()
        if db_list in text:
            return text if text else "В файле отсутствуют данные"
        else:
            return "Таких данных нет"

def read_all_from_json(path_to_file):  
    with open(path_to_file, "r", encoding="UTF-8") as file:
        text = file.read()
        return text if text else "В файле отсутствуют данные"


def append_to_json(path_to_file, db_list):
    with open(path_to_file, 'a', encoding="UTF-8") as file:
        file.write(" ".join(db_list) + "\n")
    print(f"\nДанные сохранены в {path_to_file}.\n")
    time.sleep(1)
    return

def delete_from_json(path_to_file, db_list):
    file = open(path_to_file,"w").read()
    file = file.replace(db_list,'')