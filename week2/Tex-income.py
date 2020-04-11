income = int(input("Tell me how much do you make for a living:"))
tax_rate1 = 0.1
sum1 = 6310
tax_rate2 = 0.14
sum2 = 9050
tax_rate3 = 0.2
sum3 = 14530
tax_rate4 = 0.31
sum4 = 20200
tax_rate5 = 0.35
sum5 = 42030
tax_rate6 = 0.47
sum6 = 54130
tax_rate7 = 0.5
sum7 = 54130
A0 = (sum1 * tax_rate1)
A1 = ((income - sum1) * tax_rate2)
A2 = ((income - sum2) * tax_rate3)
A3 = ((income - sum3) * tax_rate4)
A4 = ((income - sum4) * tax_rate5)
A5 = ((income - sum5) * tax_rate6)
A6 = ((income - sum6) * tax_rate7)
A7 = ((income - sum7) * tax_rate7)
# סכומים קבועים מראש
Num1 = (6310 * 0.1)  # income equal or less then 6310
Num2 = ((9050 - 6310) * 0.14)
Num3 = ((14530 - 9050) * 0.20)
Num4 = (20200 - 14530) * 0.31
Num5 = (42030 - 20200) * 0.35
Nun6 = (54130 - 42030) * 0.47
Num7 = (income - 54130) * 0.5
if income <= sum1:
    print("I see that your salary less than ", sum1, "This means that you will pay 10% Tax", income)
    total_tax = income * 0.1
    print("המס שתשלם הוא....", total_tax)
    print("הסכום שנשאר לך בכיס הוא...", income * 0.9)
    print()
    "מדרגת מס ראשונה 10%"
elif income <= sum2:
    print("I see that your salary is more than ", sum1, 'This means that you will pay 14% Tax')
    total_tax = ((income - sum1) * 0.14) + (sum1 * 0.1)
    print(total_tax)
    print("Your Total salary is ", (income - total_tax))
elif income <= sum3:
    print(" see that your salary is more than ", sum2, "This means that you will pay 20% Tax")
    total_tax = (Num1 + Num2 + A2)
    print(total_tax, "this is total_tax", Num1, Num2, A2)
    print("Your Total salary is ", (income - total_tax))
elif income <= sum4:
    print("I see that your salary is more than ", sum3, "This means that you will pay 31% Tax")
    total_tax = (Num1 + Num2 + Num3 + A3)
    print(total_tax, "this is total_tax", Num1, Num2, Num3, A3)
    print("Your Total salary is ", (income - total_tax))
elif income <= sum5:
    print("I see that your salary is more than ", sum4, "This means that you will pay 35% Tax")
    total_tax = (Num1 + Num2 + Num3 + Num4 + A4)
    print(total_tax, "this is total_tax", Num1, Num2, Num3, Num4, A4)
    print("Your Total salary is ", (income - total_tax))
elif income <= sum5:
    print("I see that your salary is more than ", sum4, "This means that you will pay 47% Tax")
    total_tax = (Num1 + Num2 + Num3 + Num4 + Num5 + A4)
    print(total_tax, "this is total_tax", Num1, Num2, Num3, Num4, Num5, A5)
    print("Your Total salary is ", (income - total_tax))
elif income <= sum6:
    print("I see that your salary is more than ", sum5, "This means that you will pay 47% Tax")
    total_tax = (Num1 + Num2 + Num3 + Num4 + Num5 + Nun6 + A5)
    print(total_tax, "this is total_tax", Num1, Num2, Num3, Num4, Num5, Nun6, A6)
    print("Your Total salary is ", (income - total_tax))
elif income > sum6:
    print("I see that your salary is more than ", sum6, "This means that you will pay 50% Tax")
    total_tax = (Num1 + Num2 + Num3 + Num4 + Num5 + Nun6 + Num7 + A6)
    print(total_tax, "this is total_tax", Num1, Num2, Num3, Num4, Num5, Nun6, Num7, A7)
    print("Your Total salary is ", (income - total_tax))
