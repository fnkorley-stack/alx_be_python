# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
