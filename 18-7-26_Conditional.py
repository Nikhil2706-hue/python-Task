

#Check whether a number is positive, negative, or zero

a=int(input("Enter num:"))
if a>0:
    print(a,"is a positive number.")
elif a<0:
    print(a,"is a negative number.")
else:
    print(a,"is a zero number.")


'''Assign grades based on marks:
90–100 → A
75–89 → B
60–74 → C
40–59 → D
Below 40 → Fail'''

marks=int(input("Enter your marks:"))
if marks>=90:
    print(marks,"Grade: A")
elif marks>=75:
    print(marks,"Grade: B")
elif marks>=60:
    print(marks,"Grade: C")
elif marks>=40:
    print(marks,"Grade: D")
else:
    print(marks,"Fail")    

#Check whether a person is a child, teenager, adult, or senior citizen based on age.
age=int(input("Enter you age:"))
if age<=12:
    print("child")
elif age<18:
    print("teenager")
elif age<60:
    print("adult")
elif age>=60:
    print("Senior citizen")

#Check whether a number is a one-digit, two-digit, three-digit, or more than three-digit number.hint : (0<=number<=9) for one digit number
digit=int(input("Enter num:"))
if 0<=digit<=9:
    print("one-digit number")
elif 10<=digit<=99:
    print("two-digit number")
elif 100<=digit<=999:
    print("three-digit number")
else:
    print("more than three-digit number")

#Check whether a customer can withdraw money (correct PIN and sufficient balance).
pin=int(input("Enter your PIN"))
if pin==2728:
    bal=int(input("Enter your balance."))
    if bal>=1000:
        print("You can withdraw money")
    else:
        print("Not have sufficient blance")
else:
    print("you enter wrong PIN")
    
#Check whether a scholarship is awarded (marks ≥ 85%, then family income below limit).
marks = int(input("Enter your total marks:"))
per=(marks/600)*100
limit = 50000
if per >= 85:
    fam_income = int(input("family income:"))
    if fam_income <= limit:
        print("Scholarship is Awarded.")
    else:
        print("Family income exceeds the limit.")
else:
    print("Not eligible for Scholarship.")

#Check whether an online order is confirmed (stock available, then payment successful).
stock_available = True
if stock_available:
    payment= False
    if payment_successful:
        print("Order is CONFIRMED")
    else:
        print("Order Failed Payment was unsuccessful")
else:
    print("Item is out of stock")

#Check whether an employee is eligible for a bonus (service ≥ 5 years and performance rating ≥ 4).
ser=int(input("Enetr service years:"))
if ser>=5:
    perf=int(input("Enter your rating:"))
    if perf>=4:
        print("You are eligible for a bonus")
    else:
        print(perf,"due to less rating you are not eligible for a bonus")
else:
    print("you are not eligible for a bonus.")
