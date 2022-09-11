from random import randint


game = [' ' for _ in range(9)]
winner = ' '


def print_game(game):
    print(f'''
{game[0]} | {game[1]} | {game[2]}
---------
{game[3]} | {game[4]} | {game[5]}
---------
{game[6]} | {game[7]} | {game[8]}
''')


def check_winner(game):
    global winner
    possible_wins = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]
    for win in possible_wins:
        if game[win[0]] == game[win[1]] == game[win[2]] and game[win[2]] != ' ':
            winner = game[win[0]]
            print_game(game)
            return True
    return False


def check_tie(game):
    if ' ' not in game:
        print_game(game)
        return True
    return False


def computer(game):
    while True:
        random = randint(0, 8)
        if game[random] != ' ':
            continue
        else:
            game[random] = 'O'
            break
    print_game(game)


game_is_on = True
user = ''
print_game(game)
while game_is_on:
    while True:
        try:
            user = int(input('Enter a number from 1 to 9: ')) - 1
            if user < 0 or user > 8:
                raise ValueError('Number must be between 1 and 9')
            if game[user] != ' ':
                raise ValueError('This position is already taken')
        except ValueError as e:
            if "invalid literal for int() with base 10:" in str(e):
                e = 'You must enter a number'
            print(e)
            user = ''
        else:
            game[user] = 'X'
            break

    if check_winner(game):
        print(f'{winner} wins!')
        game_is_on = False
    else:
        if check_tie(game):
            print('Game is a tie!')
            game_is_on = False
        else:
            print('Computer\'s turn...')
            computer(game)
            if check_winner(game):
                print(f'{winner} wins!')
                game_is_on = False
