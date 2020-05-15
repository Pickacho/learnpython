with open('E:/thor/Documents/Python_Course/week3/resources/bank_passwd.txt') as bank_password:
    bank_password = bank_password.read().splitlines()
print(bank_password)
# i = 0
# l = ":"
# while i <= 2:
#     print(bank_password[i].index(l))
#     i += 1

j = 0
k = "FreddieMercury"
while j <= 2:
    if k in bank_password[j]:
        print(bank_password[j].find(f"{k}"))
    else:
        print("else statement")
    j += 1
