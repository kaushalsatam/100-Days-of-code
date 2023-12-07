# Calculator project

from art import logo
from os import system

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+" : add,
             "-" : subtract,
             "*" : multiply,
             "/" : divide}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: \n"))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the second number?: \n"))

    calculate = operations[operation_symbol]
    answer = calculate(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    operation_continuing = True
    while operation_continuing:
        continue_operation = input(f"Type 'y' to continue calculating with {answer} \nType 'n' to start new calculaton \nType 'e' to exit.:\n")
        if continue_operation == 'e':
            operation_continuing = False
            break
        if continue_operation == 'n':
            system('cls')
            # Recursion of calculator() function
            calculator()
        operation_symbol = input("Pick another operation: ")
        next_num = float(input("What's the next number? :\n"))
        calculate = operations[operation_symbol]
        next_answer = calculate(answer, next_num)

        print(f"{answer} {operation_symbol} {next_num} = {next_answer}")

calculator()