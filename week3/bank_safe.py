code = "4812"
try_count = 0


def is_4_is_in_string(user_input):
    if "4" in user_input:
        print("True 4")
        return True
    else:
        print("False 4")
        return False


def is_8_is_in_string(user_input):
    if "8" in user_input:
        print("True 8")
        return True
    else:
        print("False 8")
        return False


def is_1_is_in_string(user_input):
    if "1" in user_input:
        print("True 1")
        return True
    else:
        print("False 1")
        return False


def is_2_is_in_string(user_input):
    if "2" in user_input:
        print("True 2")
        return True
    else:
        print("False 2")
        return False


def logic_test_one_key(user_input):
    if is_4_is_in_string(user_input) or is_8_is_in_string(user_input) or is_1_is_in_string(
            user_input) or is_2_is_in_string(user_input):
        text = "you have one key"
        return text


# eight = is_8_is_in_string(user_input)


print(code[0], "code[0]", code[1], "code[1]", code[2], "code[2]", code[3], "code[3]")
# user_string = int(input("enter your number"))

# Limits user to three guesses
guesses_remaining = 3
code = 4812
allow_user_to_enter_password = True
while allow_user_to_enter_password:
    user_string = int(input("Enter a 4 digits code to open the safe"))
    # Each attempt for the code will decrease the number of guesses remaining.
    guesses_remaining -= 1
    logic_test_one_key(user_string)
    if user_string == code:
        print("The safe is now open, the loot is yours!")
        # There is no need for more input from the user since the safe is now open
        allow_user_to_enter_password = False
    else:
        #  counter to determine amount of guesses left
        if guesses_remaining == 0:
            print("you are out'a luck son...")
            allow_user_to_enter_password = False
        elif user_string != code:
            print("Sorry you are wrong ", guesses_remaining, " guesses left before the safe will self distract")
