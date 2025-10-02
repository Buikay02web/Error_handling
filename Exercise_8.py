
def get_user_input():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Input is not a number. Please try again.")

def main():
    user_input = get_user_input()
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()