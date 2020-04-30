code = "4812"
try_count = 0
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
