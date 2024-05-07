class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner      # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Add amount to the balance."""
        if amount > 0:
            self.__balance += amount
            print(f"Added ${amount} to the balance")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Remove amount from the balance if sufficient balance exists."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount} from the balance")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

    def get_balance(self):
        """Return the balance."""
        return self.__balance


# Create a BankAccount object
account = BankAccount("John Doe", 1000)

# Test the encapsulation
account.deposit(500)
account.withdraw(200)
print(account.get_balance())

# Trying to access the private variable (will cause an error)
print(account.__balance)
