def return_valid_input(statement, valid_values):
    data = input(statement).lower()
    while(data not in valid_values):
        print("Wrong Input")
        print("Valid values are ", valid_values)
        data = input(statement).lower()
    return data
    
def cal(a, op, b):
    if (op == '+'):
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        result = a / b
    return result

while(True):
    result = 0
    a = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    op = return_valid_input("Pich an operation: ", ["+", "-", "*", "/"])
    b = float(input("What's the next number?: "))
    result = cal(a, op, b)
    print(f"{a} {op} {b} = {result}")
    should_continue = return_valid_input(f"Type 'y' to continue calculatinf with {result}, or type 'n' to start a new calculation:  ", ['y', 'n'])
    while(should_continue == 'y'):
        print("+\n-\n*\n/")
        a = result
        op = return_valid_input("Pich an operation: ", ["+", "-", "*", "/"])
        b = float(input("What's the next number?: "))
        result = cal(a, op, b)
        print(f"{a} {op} {b} = {result}")
        should_continue = return_valid_input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ", ['y', 'n']) 

