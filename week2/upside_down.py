def flip_me(string):
    if "0" in string:
        print("Sorry man, can't handle zero")
        status = False
        return status
    else:
        if len(string) == 2:
            print("The length is 2 digits long")
            print(string[::-1])
        else:
            print("apparently size does matter")
            status = False


my_string = input("Prompt: Enter a two digit number")
flip_me(my_string)
