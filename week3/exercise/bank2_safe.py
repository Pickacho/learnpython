code = '4812'
attempt = 0

while attempt <= 3:
    user_try = input("enter your code")
    counter = 0
    if "4" in user_try:
        counter += 1
    if "8" in user_try:
        counter += 1
    if "1" in user_try:
        counter += 1
    if "2" in user_try:
        counter += 1
    if user_try == code:
        print("The safe is now open")
        break
    else:
        print(f"you have {counter}  digits of the code ")
        attempt += 1
