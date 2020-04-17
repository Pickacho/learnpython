code = "4812"


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


def test_if_4_but_not_others(user_input):
    if is_4_is_in_string(user_input) and not is_1_is_in_string(user_input) and not is_2_is_in_string(
            user_input) and not is_8_is_in_string(user_input):
        return True
    else:
        return False


def test_if_8_but_not_others(user_input):
    if is_8_is_in_string(user_input) and not is_1_is_in_string(user_input) and not is_2_is_in_string(
            user_input) and not is_4_is_in_string(user_input):
        return True
    else:
        return False


def test_if_2_but_not_others(user_input):
    if is_2_is_in_string(user_input) and not is_1_is_in_string(user_input) and not is_8_is_in_string(
            user_input) and not is_4_is_in_string(user_input):
        return True
    else:
        return False


def test_if_1_but_not_others(user_input):
    if is_1_is_in_string(user_input) and not is_2_is_in_string(user_input) and not is_8_is_in_string(
            user_input) and not is_4_is_in_string(user_input):
        return True
    else:
        return False


def test_if_two_numbers(user_input):
    # test something with
    user_input + 1
    return


def logic_test(user_input):
    if test_if_4_but_not_others(user_input) or test_if_8_but_not_others(user_input) or test_if_2_but_not_others(
            user_input) or test_if_1_but_not_others(user_input) == 1:
        print("you have one key")
    elif test_if_two_numbers(user_input):
        print("this is an else statement")
        return "not good"


# this_is_my_input = input("enter your 4 digit code")
this_is_my_input = "4000"
logic_test(this_is_my_input)
