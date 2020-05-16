with open('E:\\Thor\\Documents\\Python_Course\\week3\\resources\\cereal.csv', 'r') as cereal_file:
    cereal_file.seek(0)
    cereal_lines = cereal_file.readlines()
    cereal_lines.pop(0)
    i = 0
    j = 0
    index = 0
    best_Cereal_ever = []
    biggest = 0
    biggest_index = 0
    while i < len(cereal_lines):
        cereal_lines[i] = cereal_lines[i].strip().split(',')
        print(cereal_lines[i][15:])
        i += 1
        if cereal_lines[i][15:] > biggest:
            biggest = cereal_lines[i][15:]
    #     while j < len(cereal_lines):
    #         if (cereal_lines[j][15]) > biggest:
    #             biggest = cereal_lines(j)
    #             biggest_index = j
    #
    # print(biggest_index)
    # print(biggest)
    # # while  str(cereal_lines[i][15:]) < len(cereal_lines):
    # #     if int(cereal_lines[i][15:]) > best_Cereal_ever:
    # #         best_Cereal_ever = cereal_lines[i]
    # #
    # # print(best_Cereal_ever)
