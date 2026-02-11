# 1) Use match to print day name based on day number (1–7).
day = int(input("Enter day number (1-7): "))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid day")

# 2) Match a number and print whether it is 10, 20, or 30.
num = int(input("Enter number: "))
match num:
    case 10: print("Number is 10")
    case 20: print("Number is 20")
    case 30: print("Number is 30")
    case _: print("Other number")

# 3) Create a menu-driven calculator using match-case.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
match op:
    case "+": print("Result:", a + b)
    case "-": print("Result:", a - b)
    case "*": print("Result:", a * b)
    case "/": print("Result:", a / b if b != 0 else "Cannot divide by zero")
    case _: print("Invalid operator")

# 4) Match a character and check vowel or consonant.
ch = input("Enter a character: ").lower()
match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")

# 5) Use match to display month name based on month number.
month = int(input("Enter month number (1-12): "))
match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case 8: print("August")
    case 9: print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")
    case _: print("Invalid month")

# 6) Match arithmetic operator (+, -, *, /) and perform operation.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")
match op:
    case "+": print(a + b)
    case "-": print(a - b)
    case "*": print(a * b)
    case "/": print(a / b if b != 0 else "Division by zero error")
    case _: print("Invalid operator")

# 7) Match user role (admin, user, guest) and print permissions.
role = input("Enter role: ").lower()
match role:
    case "admin": print("Full access")
    case "user": print("Limited access")
    case "guest": print("View only")
    case _: print("Unknown role")

# 8) Match HTTP status codes (200, 404, 500).
code = int(input("Enter status code: "))
match code:
    case 200: print("OK")
    case 404: print("Not Found")
    case 500: print("Server Error")
    case _: print("Unknown status code")

# 9) Match grade (A, B, C) and print remark.
grade = input("Enter grade: ").upper()
match grade:
    case "A": print("Excellent")
    case "B": print("Good")
    case "C": print("Average")
    case _: print("Needs Improvement")

# 10) Match traffic signal colors and print action.
color = input("Enter signal color: ").lower()
match color:
    case "red": print("Stop")
    case "yellow": print("Wait")
    case "green": print("Go")
    case _: print("Invalid color")

# 11) Match a tuple (x, y) and identify quadrant.
point = (int(input("Enter x: ")), int(input("Enter y: ")))
match point:
    case (x, y) if x > 0 and y > 0: print("Quadrant I")
    case (x, y) if x < 0 and y > 0: print("Quadrant II")
    case (x, y) if x < 0 and y < 0: print("Quadrant III")
    case (x, y) if x > 0 and y < 0: print("Quadrant IV")
    case _: print("On axis")

# 12) Match list length and print custom message.
lst = [1, 2, 3]
match len(lst):
    case 0: print("Empty list")
    case 1: print("One element")
    case 2 | 3: print("Few elements")
    case _: print("Many elements")

# 13) Match dictionary keys and display values.
data = {"name": "Rohit", "age": 21}
key = input("Enter key: ")
match key:
    case "name": print(data["name"])
    case "age": print(data["age"])
    case _: print("Key not found")

# 14) Match multiple values using | operator.
num = int(input("Enter number: "))
match num:
    case 1 | 3 | 5 | 7 | 9:
        print("Odd single digit")
    case 2 | 4 | 6 | 8:
        print("Even single digit")
    case _: print("Other number")

# 15) Match string commands like "start", "stop", "exit".
cmd = input("Enter command: ").lower()
match cmd:
    case "start": print("System Started")
    case "stop": print("System Stopped")
    case "exit": print("Exiting...")
    case _: print("Unknown command")

# 16) Match number ranges using guards (if).
num = int(input("Enter a number: "))
match num:
    case n if 1 <= n <= 10:
        print("Between 1 and 10")
    case n if 11 <= n <= 20:
        print("Between 11 and 20")
    case _:
        print("Out of range")

# 17) Create a simple ATM menu using match.
balance = 1000
choice = input("Enter choice (check/deposit/withdraw): ").lower()
match choice:
    case "check":
        print("Balance:", balance)
    case "deposit":
        amt = int(input("Enter amount: "))
        balance += amt
        print("Updated Balance:", balance)
    case "withdraw":
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Updated Balance:", balance)
        else:
            print("Insufficient balance")
    case _:
        print("Invalid option")

# 18) Match shape name and calculate area.
shape = input("Enter shape (circle/square/rectangle): ").lower()
match shape:
    case "circle":
        r = float(input("Enter radius: "))
        print("Area:", 3.14 * r * r)
    case "square":
        s = float(input("Enter side: "))
        print("Area:", s * s)
    case "rectangle":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area:", l * w)
    case _:
        print("Unknown shape")

# 19) Match weekday/weekend and print working status.
day = input("Enter day: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Working day")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")

# 20) Rewrite an if-elif ladder program using match-case.
num = int(input("Enter number: "))
match num:
    case n if n > 0:
        print("Positive")
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")
