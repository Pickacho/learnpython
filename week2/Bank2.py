##תוכנה זו תציג למשתמש ברכה ולאחר מכן תבקש ממנו משתמש וסיסמא ותגיב בהתאם למה שיכניס
print("Dear user, wellcome to our system")
print("Before you will be able to login you will need to first...")
username = input("Enter your user name ")

login = False

if username == "wrong" or "admin":
    PaSSword = input("Enter your Password please")
    if (username == "wrong" and PaSSword == "ads sports") or  (username == "admin" and PaSSword == "is trator"):
        print("you are now logged in")
    else:
        print("one  or both of the details are wrong")


##תוכנה זו תציג למשתמש ברכה ולאחר מכן תבקש ממנו משתמש וסיסמא ותגיב בהתאם למה שיכניס
print("Dear user, wellcome to our system")
print("Before you will be able to login you will need to first...")
username = input("Enter your user name ")

if username != "wrong" and username != "admin":
    print("No Such user")
else:
    print("Ok")
    if username == "wrong" or "admin":
        print("Great ! this user is available")
        print("Please enter the password")
        PaSSword = input("Enter your Password please")
        if (username == "wrong" and PaSSword == "ads sports") or (username == "admin" and PaSSword == "is trator"):
            print("you are now logged in")
        else:
            print("one  or both of the details are wrong")
