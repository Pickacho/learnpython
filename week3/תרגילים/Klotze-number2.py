# Get number from user
# if number is even devide by 2 till you get to 1
# if number is odd multiply by 3 and add 1 - run the loop again

def kloze(user_input):
    counter = 0
    while user_input > 1:
        if 0 == user_input % 2:
            user_input = (user_input // 2)
            counter += 1
        else:
            user_input = (user_input * 3) + 1
            counter += 1
    return counter


biggest_index = 0
the_real_big_one = 0
biggest = 0
i = 1
while i < 1000:
    if kloze(i) > biggest:
        biggest = kloze(i)
        biggest_index = i

        # print(f" if we pick the number {i}  we will need  {kloze(i)}  action to get to 1")
    i += 1
    the_real_big_one = f"The number {biggest_index} need  {biggest} actions to get to 1 "

print(the_real_big_one)
