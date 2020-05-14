var = [['X', 'O', 'X'], ['X', 'X', '-'], ['O', '-', 'X']]
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


player = 0
counter = 0
board = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']
while counter < 9:
    print(board[0])
    print(board[1])
    print(board[2])
    print(player % 2)
    player = counter % 2
    list_num = int(input("pick a line"))
    place_holder = int(input("pick a row"))
    spot_player_picked = board[list_num][place_holder]
    if spot_player_picked != player1 and spot_player_picked != player2:
        if player == 1:
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
