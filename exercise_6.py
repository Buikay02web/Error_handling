class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid amount"""
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount < 0:
                raise InvalidAmountError("Deposit amount cannot be negative")
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        except ValueError:
            print("Error: Invalid deposit amount. Please enter a valid number.")
        except InvalidAmountError as e:
            print(f"Error: {e}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount < 0:
                raise InvalidAmountError("Withdrawal amount cannot be negative")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance for withdrawal")
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        except ValueError:
            print("Error: Invalid withdrawal amount. Please enter a valid number.")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")
        except InvalidAmountError as e:
            print(f"Error: {e}")

def main():
    account = BankAccount(1000)
    while True:
        print("\nBanking Application")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = input("Enter deposit amount: ")
            account.deposit(amount)
        elif choice == "2":
            amount = input("Enter withdrawal amount: ")
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: ${account.balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

