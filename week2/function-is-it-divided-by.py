def by_3(number):
    checkfor3 = number % 3
    if checkfor3 != 0:
        print("can't be divided by 3 ")
        result3 = number
        return result3
    else:
        print("can be divided by 3 ")
        result3 = "Fizz"
        return result3


def by_5(result3):
    checkfor5 = result3 % 5
    if checkfor5 != 0:
        print("can't be divided by 5 ")
        result5 = result3
        return result5
    else:
        print("can be divided by 5 ")
        result5 = "Buzz"
        return result5


def print_the_results(result5, result3):
    if result5 and result3 is True:
        print("FizzBuzz")
        return
    elif result5 is True:
        print("Buzz")
    elif result3 is True:
        print("Fizz")
    else:
        print("Non of them good for us")


magic_number = int(input("enter an number"))
by_3(magic_number)
magic_number3 = by_3(magic_number)
magic_number5 = by_5(result3)
print_the_results(magic_number5, magic_number3)
