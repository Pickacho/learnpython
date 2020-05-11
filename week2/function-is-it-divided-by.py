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
    if result5 == "Buzz" and result3 == "Fizz":
        print("Fizz Buzz")
        newresult = "Fizz Buzz"
        return newresult
    elif result5 == "Buzz":
        print("Buzz")
    elif result3 == "Fizz":
        print("Fizz")
    else:
        print(magic_number, "This is the Else  working")


magic_number = int(input("enter an number"))
magic_number3 = by_3(magic_number)
magic_number5 = by_5(magic_number)
print_the_results(magic_number5, magic_number3)
