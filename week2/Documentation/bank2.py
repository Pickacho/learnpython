baseaccount = 500
def password_generator(user_name):
    new_username = user_name.lower() + user_name.upper() + (len(user_name) * "X")
    return new_username


def login(user_name, password):
    if len(user_name) == 0 or len(password) == 0:
        print("user name can't be empty string")
    else:
        if password == true_password:
            print(f"Welcome {user_name} Login succeeded.")
            withdraw_amount = input("How much you'd like to withdraw?")
            if withdraw_amount <= baseaccount or withdraw_amount == 0 :
                leftover = baseaccount - withdraw_amount
                print(f"Please take your money: {withdraw_amount}NIS Your balance is: {leftover}}IS")
            else:
                print("Invalid amount")
        else:
            print("Wrong Password")


user_name_entered_by_user = input("enter username")  # Enter your username
password_entered_by_user = input("enter your password")  # Enter your Password

true_password = password_generator(user_name_entered_by_user)  # The password generated by password_generator

login(user_name_entered_by_user, password_entered_by_user)  # Call to Login function 
