from CheGit import checkdigit
print("*" * 13, " Крестики-нолики  ", "*" * 13)
flag = False
board = list(range(1, 10))
count = 0
rst_player = []
ond_player = []
win_combination = [123, 456, 789, 147, 258, 369, 159, 357]
print("-" * 13)
for i in range(3):
    print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
    print("-" * 13)
print("Итак, первый игрок, чем вы будете играть? 'Х' или 'О' \n"
      "X --> нажмите 1\n"
      "O --> нажмите 2")
first_move = 0
while first_move not in (1, 2):
    first_move = checkdigit(input('Введите 1 или 2 --> '))
curplayer = ('X', 'O')
if first_move == 1:
    player = curplayer[0]
else:
    player = curplayer[1]
print(f"Отлично, вы выбрали '{player}'. Вы начинаете игру --> ")
m = 0
for i in board:
    m += 1
    move = checkdigit(input('Введите номер клетки которую хотите заполнить: '))
    while move > len(board):
        move = checkdigit(
            input('Вы вводите номер клетки вне диапозона, нужно выбрать(1-9): '))
    if (board[move-1] != 'X') and (board[move-1] != 'O'):
        board[move-1] = player

    else:
        while board[move-1] == 'X' or board[move-1] == 'O':
            move = checkdigit(
                input('Bыбрано уже занятое поле, выберете другое: '))
        board[move-1] = player
    pred = player
    if m % 2 == 0:
        if pred == 'X':
            rst_player += str(move)
            player = 'O'
        elif pred == 'O':
            rst_player += str(move)
            player = 'X'
    else:
        if pred == 'X':
            ond_player += str(move)
            player = 'O'
        elif pred == 'O':
            ond_player += str(move)
            player = 'X'
    rst_player.sort()
    ond_player.sort()
    if m >= 5:
        for comb in range(len(win_combination)):
            stri = ''
            stri += str(win_combination[comb])
            stri = list(stri)
            stri.sort()
            count = 0
            for i in stri:
                for j in rst_player:
                    if i == j:
                        count += 1
                        if count == 3:
                            print(
                                f"Победили {pred}, заняв следующую комбинацию: {stri}\n")
                            flag = True
                            exit()
            count = 0
            for n in stri:
                for k in ond_player:
                    if n == k:
                        count += 1
                        if count == 3:
                            print(
                                f"Победили {pred}, заняв следующую комбинацию: {stri}\n")
                            flag = True
                            exit()
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)
print('||||||||||||||||||||||')
if not flag:
    print('Победила дружба!')
print(f"точки первого игрока -->   {rst_player}")
print(f"точки второго игрока -->   {ond_player}")
