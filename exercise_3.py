def read_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
    else:
        print(f"File '{filename}' read successfully.")
        print("File Content:")
        print(content)

# Call the function
read_file()