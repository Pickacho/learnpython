#  תוכנה זו תציג למשתמש ברכה ולאחר מכן תבקש ממנו משתמש וסיסמא ותגיב בהתאם למה שיכניס
# print("Dear user, welcome to our system")
# print('Before you will be able to login you will need to first...')
# username = input("Enter your user name ")

# if username == "wrong" or "admin":
#     PaSSword = input("Enter your Password please")
#     if (username == "wrong" and PaSSword == "ads sports") or (username == "admin" and PaSSword == "is traitor"):
#         print("you are now logged in")
#     else:
#         print("one  or both of the details are wrong")

# תוכנה זו תציג למשתמש ברכה ולאחר מכן תבקש ממנו משתמש וסיסמא ותגיב בהתאם למה שיכניס
print("Dear user, welcome to our system")
print("Before you will be able to login you will need to first...")

try_again = 0
while try_again == 0:
    username = input("Enter your user name ")
    if username != "wrong" and username != "admin":
        print("No Such user")
        try_again = 0
        print("you will need to try something else")
        continue
    else:
        print("I have got your input\n \n \n")
        if username == "wrong" or "admin":
            print("Great ! this user is available")
            print("Please enter the password")
            PaSSword = input("Enter your Password please")
            if (username == "wrong" and PaSSword == "ads sports") or (username == "admin" and PaSSword == "is trator"):
                print("you are now logged in")
                try_again = 1
            else:
                print("one  or both of the details are wrong")
                try_again = 0
