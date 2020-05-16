# כתבו פונקציה שמקבלת רשימה, ומחזירה רשימה בסדר איברים הפוך.
# השתמשו בפעולה pop.
# לדוגמה: אם תועבר לפונקציה הרשימה [3, 2, 1], הפונקציה תחזיר [1, 2, 3]


# print(input_number_output_list(user_input))
number = [1, 2, 3]
i = (len(number)) - 1
out_put_list = []
pop_result = []
while i >= 1:
    pop_result = number.pop(i)
    print(number.pop(i))
    # print(number[i])
    print("This is the index number", i)
    # out_put_list.append(number[::-1])
    i -= 1

print(out_put_list)
