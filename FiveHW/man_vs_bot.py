# Человек против бота 
from CheGit import checkdigit
from random import randint, choice

greeting = ('Это игра "Забери все конфеты!" '
            'Правила: \n'
            'Дана 2021 конфета, \n'
            'За один ход берем не более 28 конфет, \n'
            'Побеждает тот кто последним заберет конфеты\n')

messages = ['Берите конфеты', 'Возьмите конфеты','А вам не надо? я вот взял уже',
            'Ваш шанс урвать победу', 'берите, не стесняйтесь', 'Я думаю вам тоже нужны конфеты']


def nameplayer():
    player1 = input('Как к вам обращаться?\n')
    names_for_bot = ['Ivan','Genadiy','Petr']
    player2 = choice(names_for_bot)
    print(f'с вами сразится {player2}!')
    return [player1, player2]


def game_param(players):
    n = 2021
    m = 28
    first = int(input(
        f'{players[0]}, Кто забирает конфеты первым? Если хотите вы, то введите 1, иначе любой другой символ\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    while rules[0] > 0:
        if not count % 2:
            step = randint(1, rules[1])
            print(f'А я возьму {step} конфет')
        else:
            print(f'{players[0]}, {choice(messages)}')
            step = checkdigit(input())
            if step > rules[0] or step > rules[1]:
                print(
                    f'Мы же договорились, брать не более {rules[1]} конфет(-а/-ы)!, всего их, кстати, {rules[0]} конфет(-а/-ы)')
                att = 3
                while att > 0:
                    if rules[0] >= step <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {att} попытки')
                    step = checkdigit(input())
                    att -= 1
                else:
                    return print(f'Упорство не грех, но играть с вами я больше не буду. Всего хорошего!')
        rules[0] = rules[0] - step
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет(-а/-ы)')
        else:
            print('ВЫ. ВСЕ. ЗАБРАЛИ. кто там последний то был? ах да..')
        count += 1
    return players[count % 2]


print(greeting)

players = nameplayer()
rules = game_param(players)

winer = play_game(rules, players, messages)
if not winer:
    print('Кто то правил игры не понял, до победителей и проигравших дело не дошло..')
else:
    print(
        f'В этот раз победил {winer}! Пожелаем ему не схлопотать диабет от стольких конфет!')