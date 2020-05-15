def kloze(user_input):
    counter = 0
    counter_as_list = []
    while user_input > 1:
        if 0 == user_input % 2:
            user_input = (user_input // 2)
            counter += 1
        else:
            user_input = (user_input * 3) + 1
            counter += 1
    counter_as_list = counter_as_list + [counter]
    return counter_as_list


i = 1
kloze_list = []
while i < 1000:
    kloze_list[i] = kloze(i)
    i += 1
