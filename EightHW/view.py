def show_table(name):
    f = open(f"database/{name}.csv", "r")
    print(f.read())