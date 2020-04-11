num1 = int(input("Please pick a number"))
num2 = int(input("Please pick another number"))
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
power = num1 ** num2
action = input('Please choose arithmetic action "+" "-"  "*"  "/" ')

if (action == "*") or (action == "x") or (action == "X"):
    print(mul)
elif (action == "-") or (action == "-"):
    print(dif)
elif action == "+":
    print(add)
elif action == "^" or action == "**":
    print(power)
elif action == "/":
    try:
        print(num1, '/', num2, '=', num1 / num2)
    except ZeroDivisionError:
        print(num1, '/', num2, ':', 'Division by zero!')
