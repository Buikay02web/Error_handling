def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"{num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

# Call the function
divide_numbers()