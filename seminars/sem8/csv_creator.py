def creat_csv():
    FILE_NAME = "seminars\sem8\data_base.csv"
    with open (FILE_NAME, "w", encoding = 'UTF-8') as f:
        f.write(f"Фамилия, Имя, \n")
        