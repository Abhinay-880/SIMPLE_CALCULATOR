# creating a simple calculator

def add():
    c = a + b
    print(f"The Addition of Two Numbers is c = {c}")

def sub():
    c = a - b
    print(f"The Subtraction of Two Numbers is c = {c}")


def mul():
    c = a * b
    print(f"The Multiplication of Two Numbers is c = {c}")


def div():
    c = a / b
    print(f"The Division of Two Numbers is c = {c}")


# operation

start = True

while start:

    # input value

    a = int(input("enter a value : "))
    b = int(input("enter a value : "))

    # arithmatic symbol

    operation_symbol = input("enter a arithmatic operation ? enter + , - , * , /  :  ")

    if operation_symbol == '+':
        add()
    elif operation_symbol == '-':
        sub()
    elif operation_symbol == '*':
        mul()
    elif operation_symbol == '/':
        div()

    # Lopp

    repeat_calculatiion = input("Do you want to calculate again ? Yes or No :").lower()
    if repeat_calculatiion == 'yes':
        start = True
    else:
        start = False
