var = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# bb   -0- 0    1    2   -1- 0   1    2   -3-  0    1    2
"""[
  0  ['-', '-', '-'],
  1  ['-', '-', '-'],
  2  ['-', '-', '-']
]"""

print(var[0][0], var[1][0], var[2][0])
# column 0-1-2
top_to_button0 = var[0][0] == var[1][0] == var[2][0]
top_to_button1 = var[0][1] == var[1][1] == var[2][1]
top_to_button2 = var[0][2] == var[1][2] == var[2][2]

#
if top_to_button0:
    print("status")
