def bigger_string(string1, string2, string3):
    if len(string1) > len(string2) and len(string1) > len(string3):
        return print(string1, " is bigger ")
    elif len(string2) > len(string1) and len(string2) > len(string3):
        return print(string2, " is bigger ")
    else:
        if len(string3) > len(string2) and len(string3) > len(string1):
            return print(string3, " is bigger ")


string1 = input("enter your text here - this will be known as string 1")
string2 = input("enter your text here - this will be known as string 2")
string3 = input("enter your text here - this will be known as string 3")
bigger_string(string1, string2, string3)
