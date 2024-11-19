def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation! Please choose +, -, *, or /."

def main():
    print("Welcome to the Simple Calculator! 🧮")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        result = calculator(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

main()
