try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print("Result:", x/y)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input")