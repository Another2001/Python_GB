# 38.удаление из текста всех слов, содержащих "абв".

text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def clearing_text(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = clearing_text(text)
print(text)