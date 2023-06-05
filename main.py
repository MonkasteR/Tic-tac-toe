board = [[' '] * 3 for i in range(3)]
def greating():
    print(f'┌──────────────────────────────┐')
    print(f'│     Игра в крестики-нолики   │')
    print(f'├──────────────────────────────┤')
    print(f'│   Введите координаты хода    │')
    print(f'│     два числа от 1 до 3      │')
    print(f'│ номер столбца и номер строки │')
    print(f'└──────────────────────────────┘')
    return

# def display_board():
#     print(f'   1   2   3')
#     print(f' ┌───┬───┬───┐')
#     print(f'1│ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │')
#     print(f' ├───┼───┼───┤')
#     print(f'1│ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │')
#     print(f' ├───┼───┼───┤')
#     print(f'1│ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │')
#     print(f' └───┴───┴───┘')
#     return
def display_board():
    print('   1   2   3')
    print(' ┌───┬───┬───┐')
    for i in range(3):
        print(f'{i+1}│ {board[i][0]} │ {board[i][1]} │ {board[i][2]} │')
        if i != 2:
            print(' ├───┼───┼───┤')
    print(' └───┴───┴───┘')

def player_move():
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