# 5, 1, 6, 2, 3, 4, 8, 7, 10, 9
i_out = (input("Enter a list with 10 digits ").replace(" ", "")).split(",")
print(type(i_out))
print(len(i_out))
length = len(i_out)
i = 0
new_list = []
if len(i_out) < 10:
    print("That's not a valid length of list - you need 10 digits ")
    i_out = list(input("").split())
else:
    while i < length:
        new_list = i_out
        if new_list[i].isnumeric():
            new_list[i] = int(new_list[i])
            i += 1
        else:
            new_list[i] = str(new_list[i])
            new_list = new_list.sort()
            i += 1
print(new_list)
new_list.sort()
print(new_list)
third_form_the_right = new_list[(length - 3)]
print("third_form_the_right", third_form_the_right)
