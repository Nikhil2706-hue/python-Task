#1. Arithmetic Operators:
#Accept two numbers and display the results of +, -, , /, //, %, and *.

a=25
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

'''2.Assignment Operators:
Initialize a variable with 50 and perform +=, -=, =, /=, //=, %=, and *= operations,
displaying the value after each operation.'''

n=50 
print(n)
n+=20
print(n)
n-=7
print(n)
n/=4
print(n)
n//=5
print(n)
n%=12
print(n)
n*=7
print(n)

#3. Comparison Operators:
#Accept two numbers and display the results of ==, !=, >, <, >=, and <=.

m=177
n=223
o=177
print(m==n)
print(m!=n)
print(m>n)
print(m<n)
print(m>=n)
print(m<=n)


'''4. Logical Operators:
Accept a number and display the results of the following expressions:
num > 10 and num < 100
num % 2 == 0 or num % 5 == 0
not(num > 50)'''

num=70
print(num >10 and num<100)
print(num%2 ==0 or num%5 ==0)
print(not(num>50))


'''5. Identity Operators:
Create two lists with the same elements and another variable that references the first list.
Compare them using ==, is, and is not.'''

p=[27, 38,'hello','world']
q=[27, 38,'hello','world']
print(p==q)
print(p is q)
print(p is not q)
print(id(p),id(q))


'''6.Membership Operators:
take a character and check whether it is present in the string "PYTHON" using in and not in.'''

ch="PYTHON"
print('H' in ch)
print('YT' in ch)
print('YN' not in ch)
print('PY' not in ch)


#7. Student Marks Calculator:
#Accept marks of five subjects and calculate the total, average, and percentage using arithmetic operators.


sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())

total= sub1+sub2+sub3+sub4+sub5
print("total :",total)
avg= total/5
print("averge :",avg)
percentage= (total/500)*100
print("% :", percentage)


'''8. Shopping Bill Calculator:
Accept the price and quantity of three products, calculate the total bill, and then
use comparison operators to compare the totals of any two products.'''

p1=495
p2=120
p3=150
qty1=4
qty2=10
qty3=8
bill1=p1*qty1
bill2=p2*qty2
bill3=p3*qty3
total=bill1+bill2+bill3
print("total amt:", total)
print(total>(p1+p3))
print(total<=(p3+p2))
print(total!=(p2+p3))





'''9. Temperature Converter:
Accept temperature in Celsius, convert it to Fahrenheit, and compare whether the Fahrenheit
value is greater than 100 using comparison operators.'''

celsius= float(input())
fahrenheit=(celsius*(9/5))+32
print(fahrenheit)
print(fahrenheit > 100)
print(fahrenheit < 100)
print(fahrenheit == 100)
print(fahrenheit >= 100)
print(fahrenheit <= 100)
print(fahrenheit != 100)



















