def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        try:
            num2 = int(input("Enter the second number: "))
            result = num1 / num2
            print(f"{num1} divided by {num2} is {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
        except ValueError:
            print("Error: Invalid second number. Please enter a valid integer.")
    except ValueError:
        print("Error: Invalid first number. Please enter a valid integer.")

# Call the function
divide_numbers()

