def get_minimum(numbers):
    print(f"inside the function {numbers} ")
    numbers.sort()
    print(f"inside the function2 {numbers} ")
    return numbers


numbers = "8, 9, 10, 11, 12".split(', ')
print(type(numbers))
minimum_number = get_minimum(numbers)
print(f"The minimum number is {minimum_number}")
