class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

# Example usage:
my_account = Account("John", 1000)
print(f"Account owner: {my_account.owner}")
print(f"Initial balance: ${my_account.balance}")

my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)  # Should print an error message
my_account.deposit(-100)  # Should print an error message
