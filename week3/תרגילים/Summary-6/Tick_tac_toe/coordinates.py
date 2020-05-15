var = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
####################################################################
# column  0         -1-         2
top_to_button0 = var[0][0] == var[1][0] == var[2][0]
top_to_button1 = var[0][1] == var[1][1] == var[2][1]
top_to_button2 = var[0][2] == var[1][2] == var[2][2]
####################################################################
# lines    0         -1-         2
top_line = var[0][0] == var[0][1] == var[0][2]
middle_line = var[1][0] == var[1][1] == var[1][2]
bottom_line = var[2][0] == var[2][1] == var[2][2]
####################################################################
# diagonal
diagonalL_to_R = var[0][0] == var[1][1] == var[2][2]
diagonalR_to_L = var[0][2] == var[1][1] == var[0][0]
####################################################################
player1 = "O"
player2 = "X"


def coordinates(list_num, place_holder):
    counter = 0
    while counter < 9:
        while var[list_num][place_holder] == player1 or var[list_num][place_holder] == player2:
            print("this coordinates is already Occupied")
            print(var)

            list_num = int(input("pick a list_num"))
            place_holder = int(input("pick a place_holder"))
            try:
                var[list_num][place_holder]
            except IndexError:
                print('coordinates were wrong, please try again')
    counter += 1

    return


# coordinates(1, 1)
def check_board(board):
    print(board[0][0])
    if top_to_button0:
        if board[0][0] == player1:
            return f"top_to_button0 {player1}"
        elif board[0][0] == player2:
            return f"top_to_button0 {player2}"
    elif top_to_button1:
        if board[0][1] == player1:
            return f"top_to_button1 {player1}"
        elif board[0][1] == player2:
            return f"top_to_button1 {player2}"
    elif top_to_button2:
        if board[0][2] == player1:
            return f"top_to_button2 {player1}"
        elif board[0][2] == player2:
            return f"top_to_button2 {player2}"
    elif top_line:
        if board[0][0] == player1:
            return f"top_line {player1}"
        elif board[0][0] == player2:
            return f"top_line {player2}"
    elif middle_line:
        if board[1][0] == player1:
            return f"middle_line {player1}"
        elif board[1][0] == player2:
            return f"middle_line {player2}"
    elif bottom_line:
        if board[2][0] == player1:
            return f"bottom_line {player1}"
        elif board[2][0] == player2:
            return f"bottom_line {player2}"
    elif diagonalL_to_R:
        if board[0][0] == player1:
            return f"diagonalL_to_R {player1}"
        elif board[0][0] == player2:
            return f"diagonalL_to_R {player2}"
    elif diagonalR_to_L:
        if board[0][2] == player1:
            return f"diagonalR_to_L {player1}"
        elif board[0][2] == player2:
            return f"diagonalR_to_L {player2}"
    else:
        print("No one wins")
        status = 0
        return "lets play Again"


player_marker = 0
counter = 0
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
while counter < 9:
    print(board[0])
    print(board[1])
    print(board[2])
    print(player_marker % 2)
    player_marker = counter % 2
    list_num = int(input("pick a line"))
    place_holder = int(input("pick a row"))
    spot_player_picked = board[list_num][place_holder]
    if counter == 0:
        print(f"Hi Players :)\nWelcome to a Tick tac toe \nboard[0]\nboard[1]\nboard[0]")
    if spot_player_picked != player1 and spot_player_picked != player2:
        if player_marker == 1:
            counter += 1
            marker = "0"
            try:
                board[list_num][place_holder] = marker
            except:
                pass
        else:
            counter += 1
            marker = "X"
            try:
                board[list_num][place_holder] = marker
            except:
                pass

    else:
        print("You picked already used spot, pick different spot")
    print(check_board(board))
