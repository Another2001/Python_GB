# 38.удаление из текста всех слов, содержащих "абв".

text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def clr_txt(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = clr_txt(text)
print(text)