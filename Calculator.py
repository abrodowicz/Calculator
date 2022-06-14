import sys


def welcome():
    print("Hello! This is your calculator.")


def instruction():
    print("""
This calculator works on two numbers.
You can perform actions from list below:
Adding-> +
Subtracting-> -
Multiplying-> *
Dividing-> /
To quit the program enter 'q'
Let's start!
    """)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    while True:
        if y == 0:
            print("The divisor must not be zero")
            again()
        else:
            return x / y


def getNumber():
    while True:
        number = (input("Enter your number: ")).replace(" ", "")
        if number == 'q':
            print("You quit calculator!")
            sys.exit()
        try:
            number = float(number)
            return number
        except ValueError:
            print("This input is invalid. Try again!")


def getOperator():
    while True:
        operator = input("Enter your operator: ")
        if operator == 'q':
            print("You quit calculator!")
            sys.exit()
        elif operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("This operator is invalid. Try again!")


# def getSecondNumber():
#     while True:
#         secondNumber = input("Enter your second number: ")
#         if secondNumber == 'q':
#             print("You quit calculator!")
#             sys.exit()
#         try:
#             secondNumber = float(secondNumber)
#             return secondNumber
#         except ValueError:
#             print("This input is invalid. Try again!")


def again():
    while True:
        next_calculation = input("Do you want do next calculation? (yes/no): ")
        if next_calculation == 'yes':
            calculate()
        elif next_calculation == 'no':
            print('Goodbye!')
            sys.exit()
        elif next_calculation == 'q':
            print("You quit calculator!")
            sys.exit()
        else:
            print("This input is invalid. Try again!")


def calculate():
    while True:
        x = float(getNumber())
        operator = getOperator()
        y = float(getNumber())
        if operator == '+':
            print(x, "+", y, "=", round((add(x, y)), 3))
        elif operator == '-':
            print(x, "-", y, "=", round((subtract(x, y)), 3))
        elif operator == '*':
            print(x, "*", y, "=", round((multiply(x, y)), 3))
        elif operator == '/':
            print(x, "/", y, "=", round((divide(x, y)), 3))
        else:
            print("Something is wrong. Try again")
        again()


welcome()
instruction()
calculate()