class NegativeAgeError(Exception):
    """Custom exception for negative age"""
    pass

def validate_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise NegativeAgeError("Age cannot be negative")
        print(f"Your age is {age}")
    except NegativeAgeError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid age.")

# Call the function
validate_age()
