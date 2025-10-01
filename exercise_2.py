def access_list_element():
    my_list = ["Great", "samuel", "chibuike"]
    try:
        
        index = int(input("Enter the index of the element: "))
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range. Please enter a valid index.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer index.")

# Call the function
access_list_element()