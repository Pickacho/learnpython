var = [['X', 'O', 'X'], ['X', 'X', '-'], ['O', '-', 'X']]

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
    counter += 1
    list_num = int(input("pick a list_num"))
    place_holder = int(input("pick a place_holder"))
    if player == 1:
        marker = "0"
        try:
            board[list_num][place_holder] = marker
        except:
            pass
    else:
        marker = "X"
        try:
            board[list_num][place_holder] = marker
        except:
            pass
