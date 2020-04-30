username = input("Please Enter Your User Name")
allowed_to_enter = False
Password = ""
if "wrong" == username:
    Password = input("Please Enter Your Password")
    if "ads sports" == Password:
        allowed_to_enter = True
        if allowed_to_enter:
                print("you may enter the castle")
        if Password != "ads sports":
            print("Sorry man it not personal")

if "wrong" != username:
    print("Sorry man it not personal")



copies_sold = int(input("הכנס את מספר האלבומים שנמכרו"))
print(copies_sold)
Diamond = 10000000
Platinum = 1000000
Gold = 500000
Silver = 100000

record: str = ""
if copies_sold < Silver:
    record = "Not a Best Seller"
    print("it a " + record + " record")
else:
    if Silver <= copies_sold < Gold:
        record = "Silver"
        print("it a " + record + " record")
    else:
        if Gold <= copies_sold < Platinum:
            record = "Gold"
            print("it a " + record + " record")
        else:
            if Platinum <= copies_sold < Diamond:
                record = "Platinum"
                print("it a " + record + " record")
            else:
                if copies_sold >= Diamond:
                record = "Diamond"
                print("it a " + record + " record")
