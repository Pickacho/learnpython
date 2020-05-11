carbs = int(input("How many carbohydrates you have in the dish?"))
fat = int(input("How much fat does this product have?: "))
protein = int(input("How much protein does this product have?: "))

Total_calories = carbs * 4 + fat * 9 + protein * 4
print("This dish has ", Total_calories, "in It")
