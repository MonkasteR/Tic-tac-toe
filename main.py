def greating():
    print(f'┌──────────────────────────────┐')
    print(f'│     Игра в крестики-нолики   │')
    print(f'├──────────────────────────────┤')
    print(f'│ Введите координаты хода, два │')
    print(f'│ числа от 1 до 3 через пробел │')
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


def player_move():  # Ход человека
    while True:
        print('Введите координаты хода')
        print('   Столбец и строку')
        print('Два числа от 1 до 3 через пробел')
        move = [x - 1 for x in list(map(int, str.split(input())))]  # хитрожопо запоминаем потенциальный ход
        if (0 <= move[0] <= 2) and (0 <= move[1] <= 2) and board[move[1]][move[0]] == ' ':  # проверяем ход
            board[move[1]][move[0]] = '╳'  # если условия позволяют заносим ход на игровое поле
            break
        else:
            print('Неверный ход. Попробуйте снова.')  # Что-то не подошло, сами пусть ищут где накосячили
    return


def check_win(mark):
    # Проверяем строки и столбцы, делаем очень красиво в одну строчку, чтобы никто не догадался, что полдня делал
    if any(all(board[i][j] == mark for j in range(3)) for i in range(3)) or \
            any(all(board[j][i] == mark for j in range(3)) for i in range(3)):
        return True
    # Проверяем диагонали по аналогии с предыдущим в одну строчку
    if all(board[i][i] == mark for i in range(3)) or \
            all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False


def computer_move():  # Ход компьютера
    for i in range(3): # Пытаемся поставить хоть куда-то нолик...
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = '◯'
                if (check_win('◯')): # ...если побеждаем этим ходом, то оставляем
                    return
                else:
                    board[i][j] = ' ' # Если ход ничего не дает ставим пустоту и пытаемся иначе
    for i in range(3): # По такому же принципу ставим крестик за игрока
        for j in range(3):
            if (board[i][j] == ' '):
                board[i][j] = '╳'
                if (check_win('╳')): # Если такой ход игрока ведет к победе...
                    board[i][j] = '◯' # То мы ставим в это место свой нолик, чтобы кожаный мешок не выиграл
                    return
                else:
                    board[i][j] = ' ' # Если для игрока удачных ходов нет, то попробуем как-то еще
    if (board[1][1] == ' '): # Если центральное поле пустое...
        board[1][1] = '◯' # ...ставим в центр доски свой 0, все чемпионы так делают
        return
    for i in range(3): # больше фантазии нет, ставим куда попало, если и центр занят.
        for j in range(3):
            if (board[i][j] == ' '): # ну как куда попало - в первую найденную свободную клетку
                board[i][j] = '◯'
                return


board = [[' '] * 3 for i in range(3)]  # Заполняем поле пустыми значениями
greating()  # Выводим приветствие и правила ввода хода
count = 1  # Инициализируем счетчик ходов, чтобы вовремя прекратить игру
display_board()  # Рисуем начальное поле


while True: # Основной цикл игры, бесконечный
    print(f'Ход № {count} ')
    player_move()
    display_board()
    if count >= 9:  # Проверяем не закончились ли клетки. Если закончились - выходим из игры
        print('Ничья.')
        break
    count += 1  # После хода человека увеличиваем счетчик
    if (check_win('╳')):
        print('Вы победили!')
        break
    print(f'Ход № {count} ')
    computer_move()
    display_board()
    count += 1  # После хода компа увеличиваем счетчик
    if (check_win('◯')):
        print('Компьютер победил.')
        break
