def return_valid_input(statement, valid_values):
    # 아래 문구는 docstring이라는 함수를 설명하는 문장
    # IDLE에서 함수 위에 마우스를 hover하면 아래 내용이 설명으로 나옴
    """
    statement을 요청하고 유효한 값이 입력되지 않으면 statement를 재요청
    """
    data = input(statement).lower()
    while(data not in valid_values):
        print("Wrong Input")
        print("Valid values are ", valid_values)
        data = input(statement).lower()
    return data
    
def cal(a, op, b):
    """
    연산자에 따라 계산을 수행하는 함수
    """
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

