board = [[' '] * 3 for i in range(3)]
def greating():
    print(f'|------------------------------|')
    print(f'|     Игра в крестики-нолики   |')
    print(f'|------------------------------|')
    print(f'|   Введите координаты хода    |')
    print(f'|     два числа от 1 до 3      |')
    print(f'| номер столбца и номер строки |')
    print(f'|------------------------------|')
    return

def display_board():
    print('\n'.join(['|'.join(row) for row in board]),'\n')
    return

def move():
    return

def check_win():
    return

def draw_check():
    return

# Определяем функцию для хода компьютера
def computer_move():
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = 'O'
                if (check_win('O')):
                    return
                else:
                    board[i][j] = ' '
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = 'X'
                if (check_win('X')):
                    board[i][j] = 'O'
                    return
                else:
                    board[i][j] = ' '
    if (board[1][1] == ' '):
        board[1][1] = 'O'
        return
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = 'O'
                return


greating()
print(display_board())

# Основной цикл игры
display_board()
while (True):
    player_move()
    display_board()
    if (check_win('X')):
        print('Вы победили!')
        break
    computer_move()
    display_board()
    if (check_win('O')):
        print('Компьютер победил.')
        break