#схватка двух людей
import random
from CheGit import checkdigit
greeting = ('Вы на канале игры "Забери все конфеты!" '
    'Основные правила игры:\n'
    'Дана куча из 2021 конфеты, \n'
    'За один ход берем не больше 28 шт, \n'
    'Ну а побеждает тот кто заберет посление конфеты из кучи \n'
    'Итак, начнём!')
            

messages = ['Берите конфеты', 'Возьмите конфеты',' Вам не надо? а вот ваш оппонент взял уже',
            'это ваш шанс ', 'берите, не стесняйтесь', 'Я думаю вам тоже нужны конфеты', 'Брать можно, есть - пока что нет']


def play_game(n, m, players, messages):
    count = 0
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        step = checkdigit(input())
        if step > n or step > m:
            print(f'Это слишком много, можно взять не более 28 конфет, у нас всего {n} конфет')
            att = 3
            while att > 0:
                if n >= step <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {att} попытки')
                step = checkdigit(input())
                att -=1
            else: 
                return print(f'А кто это у нас такой настырный? Для вас игра окончена!')
        n = n - step
        if n > 0: print(f'Осталось {n} конфет(-а/-ы)')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Ну а вас, как изволите называть?\n')
players = [player1, player2]

n = 2021
m = 28

win_sit = play_game(n, m, players, messages)
if not win_sit:
    print('Кто то правил игры не понял, до победителей и проигравших дело не дошло..')
else:
    print(
        f'В этот раз победил {win_sit}! Пожелаем ему не схлопотать диабет от стольких конфет!')