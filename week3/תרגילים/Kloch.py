# מקבל מספר ומוציא החוצא את מספר הפעולות הנדרשות כדי להגיע ל- 1
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


# עליי לכתוב פונקציה שתדע לקבל מספר ולהריץ את הפונקציה kloze ועבור כל i לקבל את התוצאה של קלוץ וליצור מזה רשימה
i = 1
biggest = 0
while i <= 1000:
    if kloze(i) > biggest:
        biggest = kloze(i)
    i += 1

print(biggest)
print(kloze(177))
# number_only = int(input("enter a number for Kloze"))
# print(type(kloze(number_only)))
# var_for_me = kloze(number_only)
# print(var_for_me)
# print(get_highest_grade(kloze(number_only)))
"""
x = input()
new_var = kloze(x)
print(new_var)

def list_creator():
    x = 1
    while x <= 1000:
        list = []
        list = list + kloze(x)[x]
        x += 1
        print(kloze(x))"""
