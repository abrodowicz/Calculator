import sys


def welcome():
    greeting_text = "Hello! This is your calculator."
    print(greeting_text)
    return greeting_text


def instruction():
    information_text = """
This calculator works on two numbers.
You can perform actions from list below:
Adding-> +
Subtracting-> -
Multiplying-> *
Dividing-> /
To quit the program enter 'q'
Let's start!
    """
    print(information_text)
    return information_text


def add(x, y):
    return roundToThird(x + y)


def subtract(x, y):
    return roundToThird(x - y)


def multiply(x, y):
    return roundToThird(x * y)


def divide(x, y):
    while True:
        if y == 0:
            print("The divisor must not be zero")
            again()
        else:
            return roundToThird(x / y)


def roundToThird(x):
    return round(x, 3)


def getNumber(variable_alias: str) -> float:
    while True:
        number = (input(f"Enter your number {variable_alias}: ")).replace(" ", "").replace(",", ".")
        if number == 'q':
            print("You quit calculator!")
            sys.exit()
        try:
            number = float(number)
            return number
        except ValueError:
            print("This input is invalid. Try again!")


def getOperator(operator):
    if operator == 'q':
        print("You quit calculator!")
        sys.exit()
    elif operator in ('+', '-', '*', '/'):
        return operator
    else:
        print("This operator is invalid. Try again!")


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
        x = getNumber("X")
        while True:
            operator = getOperator(input("Enter your operator: "))
            if operator is not None:
                break
        y = getNumber("Y")
        if operator == '+':
            print(x, "+", y, "=", add(x, y))
        elif operator == '-':
            print(x, "-", y, "=", subtract(x, y))
        elif operator == '*':
            print(x, "*", y, "=", multiply(x, y))
        elif operator == '/':
            print(x, "/", y, "=", divide(x, y))
        else:
            print("Something is wrong. Try again")
        again()


def main():
    welcome_text = welcome()
    instruction_text = instruction()
    calculate()
    return welcome_text
    return instruction_text
    return calculator_input


if __name__ == '__main__':
    main()