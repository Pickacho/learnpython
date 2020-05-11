"""אם משתמש הקליד מספר שאינו בעל 3 ספרות, כמו "4", הניחו שהמשתמש התכוון להקליד 004 והשלימו עבורו את המלאכה.
הדפיסו למשתמש את מספר הקטגוריה אחרי התיקון, או "קטגוריה שגויה" אם הקלט שהוזן לא היה מספרי.

לדוגמה:

    אם משתמש הקליד 5, הדפיסו לו 005.
    אם משתמש הקליד 007, הדפיסו לו 007.
    אם משתמש הקליד 70, הדפיסו לו 070.
    אם משתמש הקליד 700, הדפיסו לו 700.
    אם משתמש הקליד -1, הדפיסו לו "Wrong Category".
    אם משתמש הקליד Art, הדפיסו לו "Wrong Category"""


def fix_number_of_digits(not_three_digits):
    if len(not_three_digits) == 1:
        one_to_three = "00" + not_three_digits
        return one_to_three
    elif len(not_three_digits) == 2:
        one_to_three = "0" + not_three_digits
        return one_to_three


user_input = input("Enter the Book Category you wish to have, input in format of 3 digit such as '700' :")
if user_input.isdigit() != 1 or user_input == "-1":  # Tests for Letters or non exist option named "-1"
    print("Wrong Category")
elif len(user_input) != 3:  # Tests for 3 digits - if x digit change to 00X => 1 => 001 , if two digits will convert from X0  to 0X0 => 20 => 020
    print("this will show that that you don\'t have three digits")
    print(fix_number_of_digits(user_input))
elif len(user_input) == 3:
    print(user_input)
    print("this will show that that you have three digits")

