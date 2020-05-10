clean_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# bb   -0- 0    1    2   -1- 0   1    2   -3-  0    1    2
var = [['X', 'X', 'X'], ['X', '-', '-'], ['X', '-', '-']]
long = """
  0  ['-', '-', '-'],
  1  ['-', '-', '-'],
  2  ['-', '-', '-']
"""
####################################################################
player1 = "O"
player2 = "X"
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
print(clean_board)
print(long)
print(var[0][0], var[1][0], var[2][0])


def check_board(board):
    if top_to_button0 == player1 or top_to_button0 == player2:
        if var[0][0] == player1:
            return player1
        else:
            return player2
    elif top_to_button1 == player1 or top_to_button1 == player2:
        if var[0][0] == player1:
            return player1
        else:
            return player2
    elif top_to_button2 == player1 or top_to_button2 == player2:
        if var[0][0] == player1:
            return player1
        else:
            return player2
    elif top_line == player1 or top_line == player2:
        if var[0][0] == player1:
            return player1
        else:
            return player2
    elif middle_line == player1 or middle_line == player2:
        if var[1][0] == player1:
            return player1
        else:
            return player2
    elif bottom_line == player1 or bottom_line == player2:
        if var[2][0] == player1:
            return player1
        else:
            return player2
    elif diagonalL_to_R == player1 or diagonalL_to_R == player2:
        if var[0][0] == player1:
            return player1
        else:
            return player2
    elif diagonalR_to_L == player1 or diagonalR_to_L == player2:
        if var[0][2] == player1:
            return player1
        else:
            return player2
    else:
        print("No one wins")


print("this is when i call to check_board")
print(check_board(clean_board))
# if top_to_button0:
#     if var[0][0] == "X":
#         marker = "X"
#         print(f"{marker} wins")
#     else:
#         marker = "O"
#         print(f"{marker} wins")
# else:
#     print("nope")
# print(f"{var[0]}\n{var[1]}\n{var[2]}")
#
# print(var[0][0])
#
# if top_to_button1:
#     if var[0][0] == "X":
#         marker = "X"
#         print(f"{marker} wins")
#     else:
#         marker = "O"
#         print(f"{marker} wins")
# else:
#     print("nope")
#
# if top_to_button2:
#     if var[0][0] == "X":
#         marker = "X"
#         print(f"{marker} wins")
#     else:
#         marker = "O"
#         print(f"{marker} wins")
# else:
#     print("nope")
