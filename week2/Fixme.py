age = int(input("Please enter your age: "))

if age < 0:
    print("Your age is invalid.")
elif age < 18:
    print("Younger than 18.")
else:
    print("You are so old!")
