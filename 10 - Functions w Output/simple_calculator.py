import art

def add(n1, n2):
    """Adds n1 to n2"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts n1 to n2"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies n1 to n2"""
    return n1 * n2

def divide(n1, n2):
    """Divides n1 to n2"""
    return n1 / n2

def ask_operator():
    return input("[?] What mathematical operator would you like to use? Type the symbol."
          "\n'+' - Addition"
          "\n'-' - Subtraction"
          "\n'*' - Multiplication"
          "\n'/' - Division"
          "\n>> "
          )
math_ops = {'+': add, '-': subtract, '*': multiply, '/': divide}

while True:
    print(art.logo)
    n1 = int(input("\n\n[?] Give me the first number."
                   "\n>> "))
    operator = ask_operator()
    n2 = int(input("[?] Give me the second number."
                   "\n>> "))
    result = math_ops[operator](n1, n2)

    print(f"[RESULT] {n1} {operator} {n2} = {result}")

    while True:
        choice = input(f"[?] Do you want to continue working with the previous result ({result})? Type 'y' for yes or 'n' for no."
                  "\n>> ")
        if choice == 'y':
            n1 = result
            operator = ask_operator()
            n2 = int(input("[?] Give me the number you'd like to calculate it with."
                           "\n>> "))
            result = math_ops[operator](n1, n2)
            print(f"[RESULT] {n1} {operator} {n2} = {result}")
        else:
            break