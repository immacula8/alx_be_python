def perform_operation(num1, num2, operation):
    # Step 1: Check the type of the user's input
    # A. Check if num1 is a valid integer or float
    if not isinstance(num1,(int,float)):
        return 'Your first integer is not a valid number or float'
    # B. Check if num2 is a valid integer or float
    if not isinstance(num2,(int,float)):
        return 'Your second integer is not a valid number or float'
    # C. Check if operation is a valid string
    if not isinstance(operation,str):
        return 'Your operation is not a valid string'
    
    # - Check if operation is 'add', 'subract', 'multiply', 'divide'
 # - If it is, perform the operation
    if operation == "add":
        return float(num1 + num2)
    elif operation == "subtract":
        return float(num1 - num2)
    elif operation == "multiply":
        return float(num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            return "Error Cannot divide by zero"
        else:
            return float(num1 / num2)
    else:
        return "Error: Unknown operation"