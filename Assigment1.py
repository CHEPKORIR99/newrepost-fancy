def Calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2 if num2 != 0 else 'Error: Division by zero'}
    
    print(f"{num1} {operation} {num2} = {operations.get(operation, 'Invalid operation')}")

Calc()3


