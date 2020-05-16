###################################
# This is the Givov Function: will get password string and return out_put_hash


def my_hash(string):
    i = 0
    temp_hash = 1
    while i < len(string):
        temp_hash = (temp_hash * ord(string[i])) * (i + 1) % 397643
        i += 1

    out_put_hash = temp_hash % 100297
    return out_put_hash


# תוכנה זו תציג למשתמש ברכה ולאחר מכן תבקש ממנו משתמש וסיסמא ותגיב בהתאם למה שיכניס
print("Dear user, welcome to our system")
print("Before you will be able to login you will need to first...")
with open('/week3/resources/bank_passwd.txt') as bank_passwd:
    user_and_password_list = bank_passwd.read(0)
    user_and_password_list = user_and_password_list.readlines()

print(user_and_password_list)


def check_user_and_password(username, password):
    from time import sleep
    try_again = 0
    while try_again == 0:
        # username = input("Enter your user name ")
        if username != "wrong" and username != "admin":
            print("No Such user")
            try_again = 0
            print("you will need to try something else\n\n\n")
            sleep(2.0)
            username = input("Enter a new user name")
            continue

        else:
            print("I have got your input\n \n \n")
            if username == "wrong" or "admin":
                print("Great ! this user is available")
                if (username == "wrong" and password == "ads sports") or (
                        username == "admin" and password == "is traitor"):
                    print("you are now logged in")
                    try_again = 1
                else:
                    print("one  or both of the details are wrong")
                    try_again = 0
                    username = input("Enter a new user name")
                    password = input("Enter your Password please")

# user_input = input("what is the user name you are trying to log with? ")
# password_input = input("what is the password of the user?")
# check_user_and_password(user_input, password_input)
#
# print(my_hash("my name is Ran"))
