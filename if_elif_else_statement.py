#1) Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#2) Check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#3) Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
#4) Check whether a year is a leap year
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
#5) Calculate grade based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
#6) Check whether a character is a vowel or consonant
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
#7) Check if a number is divisible by both 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")
#8) Check if a number is a 3-digit number
num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")
#9) Check whether a triangle is valid using angles
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
#10) Calculate electricity bill using slab rates
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill:", bill)
#11) Check if a number is a palindrome
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#12) Find profit or loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")
#13) Check character type
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")
#14) Determine type of triangle (by sides)
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
#15) Check whether a number lies between 50 and 100
num = int(input("Enter a number: "))

if 50 <= num <= 100:
    print("Number lies between 50 and 100")
else:
    print("Number not in range")
#16) Find the second largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Second largest:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second largest:", b)
else:
    print("Second largest:", c)
#17) Check if a number is divisible by 3 or 7 but not both
num = int(input("Enter a number: "))

if (num % 3 == 0 or num % 7 == 0) and not (num % 3 == 0 and num % 7 == 0):
    print("Divisible by 3 or 7 but not both")
else:
    print("Condition not satisfied")
#18) Validate login credentials
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
#19) Check whether a number is a perfect square
num = int(input("Enter a number: "))

root = int(num ** 0.5)

if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
#20) Calculate bonus
salary = float(input("Enter salary: "))

if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus:", bonus)