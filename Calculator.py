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


def getFirstNumber():
    while True:
        firstNumber = input("Enter your first number: ")
        if firstNumber == 'q':
            sys.exit()
        elif int(firstNumber):
            return firstNumber
        else:
            print("This input is invalid. Try again!")
    getOperator()


def getOperator():
    while True:
        operator = input("Enter your operator: ")
        if operator == 'q':
            sys.exit()
        elif operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("This operator is invalid. Try again!")
    getSecondNumber()


def getSecondNumber():
    while True:
        secondNumber = input("Enter your second number: ")
        if secondNumber == 'q':
            sys.exit()
        elif int(secondNumber):
            return secondNumber
        else:
            print("This input is invalid. Try again!")
    calculate()


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


def calculate():
    while True:
        x = int(getFirstNumber())
        operator = getOperator()
        y = int(getSecondNumber())
        if operator == '+':
            print(x, "+", y, "=", round((add(x, y)), 3))
        elif operator == '-':
            print(x, "-", y, "=", round((subtract(x, y)), 3))
        elif operator == '*':
            print(x, "*", y, "=", round((multiply(x, y)), 3))
        elif operator == '/':
            print(x, "/", y, "=", round((divide(x, y)), 3))
        else:
            sys.exit()
        again()


welcome()
instruction()
calculate()