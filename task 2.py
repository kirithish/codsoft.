def calculator():
    print("Welcome to the Calculator!")
    while True:
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("Choose an operation:")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Modulus(%)")
        print("6. Exponentiation(^)")
        operation = input("Enter the operation (+, -, *, /, %, ^): ")
        if operation == '+':
            result = num1 + num2
            operation_name = "addition"
        elif operation == '-':
            result = num1 - num2
            operation_name = "subtraction"
        elif operation == '*':
            result = num1 * num2
            operation_name = "multiplication"
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                operation_name = "division"
            else:
                print("Error: Division by zero is not allowed.")
                continue
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
                operation_name = "modulus"
            else:
                print("Error: Division by zero is not allowed.")
                continue
        elif operation == '^':
            result = num1 ** num2
            operation_name = "exponentiation"
        else:
            print("Invalid operation choice. Please try again.")
            continue

        print(f"The result of the {operation_name} is: {result}")
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

    print("Thank you for using the Calculator. Goodbye!")

calculator()

