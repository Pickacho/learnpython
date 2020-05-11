def check_if_number_is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def check_if_number_minus_1_is_divisible_by_5(number):
    number_minus_1 = number - 1
    if number_minus_1 % 5 == 0:
        return True
    else:
        return False


def check_zoom_or_boom(number):
    is_number_even = check_if_number_is_even(number)
    is_number_minus_one_divisible_by_5 = check_if_number_minus_1_is_divisible_by_5(number)
    if is_number_even and is_number_minus_one_divisible_by_5:
        print("Boom")
    else:
        print("Zoom")


variable = int(input("enter number"))
check_zoom_or_boom(variable)
