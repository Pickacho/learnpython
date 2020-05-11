animals = ['pig', 'shark', 'lion', 'duck', 'duck', 'zebra', 'camel', 'pig', 'camel', 'rabbit', 'pig', 'camel', 'rabbit',
           'camel', 'dove', 'pig', 'camel']
length = len(animals)
print(length)
i = 0
j = 0
while i < 17:
    print(animals[i])
    if animals[i] == 'shark':
        j = i + 1
        animals.insert(j, "Mega Fish")
    i += 1
