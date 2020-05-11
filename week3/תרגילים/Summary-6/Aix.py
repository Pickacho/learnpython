clean_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# bb   -0- 0    1    2   -1- 0   1    2   -3-  0    1    2
var = [['X', 'O', 'X'], ['X', 'X', '-'], ['O', '-', 'X']]
####################################################################
player1 = "O"
player2 = "X"
status = ""
counter = ""
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
# Full Board with no victory
def full_Board_with_no_victory(status, counter):
    if status == 0 and counter == 9:
        status = 2
        return status


# print(clean_board)
# print(var[0][0], var[1][0], var[2][0])


def check_board(board):
    print(board[0][0])
    if top_to_button0:
        if board[0][0] == player1:
            return f"top_to_button0 player1"
        elif board[0][0] == player2:
            return f"top_to_button0 player2"
    elif top_to_button1:
        if board[0][1] == player1:
            return f"top_to_button1 player1"
        elif board[0][1] == player2:
            return f"top_to_button1 player2"
    elif top_to_button2:
        if board[0][2] == player1:
            return f"top_to_button2 player1"
        elif board[0][2] == player2:
            return f"top_to_button2 player2"
    elif top_line:
        if board[0][0] == player1:
            return f"top_line player1"
        elif board[0][0] == player2:
            return f"top_line player2"
    elif middle_line:
        if board[1][0] == player1:
            return f"middle_line player1"
        elif board[1][0] == player2:
            return f"middle_line player2"
    elif bottom_line:
        if board[2][0] == player1:
            return f"bottom_line player1"
        elif board[2][0] == player2:
            return f"bottom_line player2"
    elif diagonalL_to_R:
        if board[0][0] == player1:
            return f"diagonalL_to_R player1"
        elif board[0][0] == player2:
            return f"diagonalL_to_R player2"
    elif diagonalR_to_L:
        if board[0][2] == player1:
            return f"diagonalR_to_L player1"
        elif board[0][2] == player2:
            return f"diagonalR_to_L player2"
    else:
        print("No one wins")
        status = 0
        return "lets play Again"


new_var = f"{var[0]}\n{var[1]}\n{var[2]}"
print("this is when i call to check_board")
print(check_board(var))
