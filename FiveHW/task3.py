from CheGit import checkdigit
print("*" * 13, " Крестики-нолики  ", "*" * 13)

board = list(range(1, 10))
rst_player = ''
ond_player = ''
win_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
    1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
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
for i in board:
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
    if pred == 'X':
        rst_player += str(move)
        player = 'O'
    elif pred == 'O':
        ond_player += str(move)
        player = 'X'
    if i > 5:
        for comb in range(len(win_combination)):
            stri = ''
            for j in range(len(win_combination[comb])):
                stri += str(win_combination[comb])
                print(stri)
                if rst_player == stri:
                    print(f"Победили {pred}, заняв следующую комбинацию:")
                    exit(0)
                elif ond_player == stri:
                    print(f"Победили {pred}, заняв следующую комбинацию:")
                    exit(0)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

print('||||||||||||||||||||||')
print(f"rst_player -->   {rst_player}")
print(f"ond_player -->   {ond_player}")
