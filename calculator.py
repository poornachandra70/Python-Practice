# Accepts two users inputs from user and then accept operation (+,-,*,/) according to the operation provided execute the neccessary operation
# eg : num1 = 10 
#      num2 = 20
#      operation = +  then op = 30 


# Accept two numbers from the user (converted to float to support decimals)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Accept the operation choice
operation = input("Enter operation (+, -, *, /): ")

# Execute the necessary operation using conditional statements
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":

    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please choose from +, -, *, /.")