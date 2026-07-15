'''
ASSIGNMENT

DATE:15-07-2026
TECHSTACK:PYTHON
TOPIC:Flow Control Statement
_________________________________________________________________________
TASK :
'''
#Write a program to check if a user has entered the correct OTP (1234). If correct, display "OTP Verified".

value=int(input('Enter your OTP:'))
if value==1234:
    print("OTP Verified.")



#Write a program to check if the mobile battery percentage is below 20. If yes, display "Please Charge Your Phone".

battery=int(input("Enter Battery percentage:"))
if battery <=20:
    print("Please Charge your phone")


#Write a program to check if a bank account balance is greater than ₹10,000. If yes, display "Eligible for Premium Account".

account=int(input("Bank account balance is " ))
if account>10000:
    print(1"You are Eligible for Premium Account")


#Write a program to check if a person has a valid ticket (has_ticket = True). If yes, display "Welcome to the Movie".

enter=True
if type(enter)==bool:
    print("Welcome to the Movie")
#or
'''
enter=input(“show your ticket:”)
if enter=='yes':
    print("Welcome to the Movie")
'''





#Write a program to check whether a person is eligible to vote.

age=int(input("Enter you age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Write a program to check whether a customer is eligible for free delivery (bill ≥ ₹1000).

bill=int(input("Enter your bill:"))
if bill>=10000:
    print("eligible for free delivery")
else:
    print("not eligible for free delivery")


#Write a program to check whether a user has enough balance to withdraw ₹5000.

user=int(input("Enter your Balance:"))
if user>=50000:
    print("You can withdraw your amount.")
else:
    print("Not have enough balance.") 


