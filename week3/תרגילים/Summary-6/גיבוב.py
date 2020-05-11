def my_hash(string):
    i = 0
    temp_hash = 1
    while i < len(string):
        temp_hash = (temp_hash * ord(string[i])) * (i + 1) % 397643
        i += 1

    out_put_hash = temp_hash % 100297
    return out_put_hash


my_string = input("Enter your string here:  ")
print(my_hash(my_string))
