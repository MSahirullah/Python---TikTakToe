game_still_going = True
winner = None
current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    return


def handle_turn(current_player):
    display_board()
    print(current_player + "'s turn.")
    position = input("Choose a postion from 1-9: ")

    while True:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a postion from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            break
        else:
            print("You can't go there. Go again.")

    board[position] = current_player


def check_if_game_over():
    check_if_win()
    check_if_tie()
    return


def check_if_win():
    global winner

    # check_rows()
    row_winner = check_rows()
    # check_columns()
    column_winner = check_columns()
    # check_diagnols()
    diagnols_winner = check_diagnols()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnols_winner:
        winner = diagnols_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagnols():
    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "0"

    elif current_player == "0":
        current_player = "X"
    return


def play_game():
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "0":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")

    return


play_game()
