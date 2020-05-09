clean_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# bb   -0- 0    1    2   -1- 0   1    2   -3-  0    1    2
var = [['X', 'X', 'X'], ['X', '-', '-'], ['X', '-', '-']]
long = """
  0  ['-', '-', '-'],
  1  ['-', '-', '-'],
  2  ['-', '-', '-']
"""
print(clean_board)
print(long)

print(var[0][0], var[1][0], var[2][0])
# column  0         -1-         2
top_to_button0 = var[0][0] == var[1][0] == var[2][0]
top_to_button1 = var[0][1] == var[1][1] == var[2][1]
top_to_button2 = var[0][2] == var[1][2] == var[2][2]

#
if top_to_button0:
    if var[0][0] == "X":
        marker = "X"
        print(f"{marker} wins")
    else:
        marker = "O"
        print(f"{marker} wins")
else:
    print("nope")
print(f"{var[0]}\n{var[1]}\n{var[2]}")

print(var[0][0])

if top_to_button1:
    if var[0][0] == "X":
        marker = "X"
        print(f"{marker} wins")
    else:
        marker = "O"
        print(f"{marker} wins")
else:
    print("nope")

if top_to_button2:
    if var[0][0] == "X":
        marker = "X"
        print(f"{marker} wins")
    else:
        marker = "O"
        print(f"{marker} wins")
else:
    print("nope")
