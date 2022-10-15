def delword(file, type, constat, file1, type1):
    f = open(file, type, encoding='utf-8')
    text = f.read()
    print('Данные из файла: \n' + text)
    words = text.split(' ')
    del_frag = constat
    corlist = []
    for word in words:
        if del_frag not in word:
           corlist.append(word)
        cortext = " ".join(corlist)
    f.close
    f = open(file1, type1, encoding='utf-8')
    f.write(cortext)
    return " ".join(corlist)


delword("FiveHW/text_for_1task.txt", "r",
        "абв", "FiveHW/correct_text.txt", "w")
