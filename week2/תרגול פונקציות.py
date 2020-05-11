def is_divisible_by_4(number):
    reminder = number % 4
    if reminder == 0:
        print("the number is divisible by 4 !")
        return True
    else:
        print("not divisible by 4")
        return False


is_divisible_by_4(8)


def is_this_my_name(string_to_check):
    if string_to_check == "Ran":
        print("this is My name")
    else:
        print("No it's Not my name")


name = input("enter a name")
is_this_my_name(name)


def greet_user():
    print("Hello new user! Welcome")


def check_if_numbers_are_zero(first, second):
    if first == 0 or second == 0:
        print("One of the numbers is 0")
    else:
        print("Neither is 0 ")


first_num = int(input("enter a number"))
second_num = int(input("enter a number"))
check_if_numbers_are_zero(first_num, second_num)
