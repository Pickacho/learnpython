list1 = [2, 8, 20, 28, 50, 82]
print(list1)
list2 = list1
print(id(list2))
list2.append(126)

print(list1)
print(id(list2))
print('-' * len(str(list1)))
print(list2)
print(id(list2))
print(len(str(list1)))
print((str(list1)))
print(id(list1))
