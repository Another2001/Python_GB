# lllBBtttttttttttIIccXXXXXXppp{{{}}}
# PPffffWWWWWnnnnMMMqqTkkkkkkkk+++
text = input('Введите желаемый текст для кодировки : \n')

f = open('FiveHW/RLEdecode.txt', 'w' , encoding="UTF-8")


def encode(ss):
    beg_str = ''
    pred = ''
    count = 1
    for char in ss:
        if char != pred:
            if pred:
                beg_str += str(count) + pred
            count = 1
            pred = char
        else:
            count += 1
    beg_str += str(count) + pred
    f.write(beg_str)
    return beg_str


upd = encode(text)
print('Сжатая строка методом RLE : ' + upd)


def decoding(ss: str):
    count = ''
    upd_str = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            upd_str += char * int(count)
            count = ''
    t = open('FiveHW/RLEencode.txt', 'w' , encoding="UTF-8")     # FiveHW/RLEencode.txt
    t.write(upd_str)
    return upd_str


upd_str = decoding(upd)
print('Восстановленная строка после RLE обработки :' + upd_str)
print ('Все данные сохранены в файлах..')
