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


def display_board():
    print('   1   2   3')
    print(' ┌───┬───┬───┐')
    for i in range(3):
        print(f'{i + 1}│ {board[i][0]} │ {board[i][1]} │ {board[i][2]} │')
        if i != 2:
            print(' ├───┼───┼───┤')
    print(' └───┴───┴───┘')


def player_move():
    move = []
    while True:
        print('Введите координаты хода')
        print('   Столбец и строку')
        print('Два числа от 1 до 3 через пробел')
        move = [x - 1 for x in list(map(int, str.split(input())))]
        if (0 <= move[0] <= 2) and (0 <= move[1] <= 2) and board[move[1]][move[0]] == ' ':
            board[move[1]][move[0]] = 'X'
            break
        else:
            print('Неверный ход. Попробуйте снова.')
    return


def check_win(mark):
    # Проверяем строки и столбцы
    for i in range(3):
        if all([board[i][j] == mark for j in range(3)]):
            return True
        if all([board[j][i] == mark for j in range(3)]):
            return True
    # Проверяем диагонали
    if all([board[i][i] == mark for i in range(3)]):
        return True
    if all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False


# Ход компьютера
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
display_board()
count = 1

# Основной цикл игры
while True:
    player_move()
    display_board()
    count += 1
    if (check_win('X')):
        print('Вы победили!')
        break
    if count == 9:
        print('{Ходов больше нет}')
        break
    computer_move()
    display_board()
    count += 1
    if (check_win('O')):
        print('Компьютер победил.')
        break
    if count >= 10:
        print('Ничья.')
        break