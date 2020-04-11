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
Num1 = (6310 * 0.1)
Num2 = ((9050 - 6310) * 0.14)
Num3 = ((10000 - 9050) * 0.20)
X = 631
Y = 383.6
Z = 190

if income <= sum1:
    print("אם אתה מרוויח:", income)
    total_tax = income * 0.1
    print("המס שתשלם הוא....", total_tax)
    print("הסכום שנשאר לך בכיס הוא...", income * 0.9)
    print()
    "מדרגת מס ראשונה 10%"
elif income <= sum2:
    print("זהו סכום גבוה מ 6310 ולכן מצטרפת אלייך מדרגת מס נוספת של 14% ")
    print(sum1 * 0.1)
    print((income - sum1) * 0.14)
    print(A1, "A1")
    total_tax = ((income - sum1) * 0.14) + (sum1 * 0.1)
    "מדרגת מס ראשונה 10%+שניה 14%"
    print(total_tax)
elif income <= sum3:
    print("זהו סכום גבוה מ 9050 ולכן מצטרפת אלייך מדרגת מס נוספת של 20% ")
    print(sum1 * 0.1)  # 6310 * 0.1
    print((sum2 - sum1) * 0.14)  # (9050 - 6310) * 0.14 חישוב כמה המדרגה השניה סכום קבוע
    print((income - sum2) * 0.20)  # (income - 9050) * 0.20
    total_tax1 = (A2 + X + Y)
    print(total_tax1, "this is total_tax", A2, X, Y)
