import os
import random

class BankAccount:
    def __init__(self, name, account_type, balance=0):
        self.balance = balance
        self.account_type = account_type
        self.name = name
        self.account_id = random.randint(1000, 9999)
        self.file_name = f"{self.name}_{self.account_type}_{self.account_id}.txt"
        self._create_statement_file()

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self._record_transaction(f"Withdrawn: ${amount}")
            else:
                print("Insufficient funds, please check your balance.")
        else:
            print("Please enter a valid amount to withdraw.")

    def _record_transaction(self, transaction_details):
        with open(self.file_name, 'a') as file:
            file.write(f"{transaction_details} - New Balance: ${self.balance}\n")

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record_transaction(f"Deposited: ${amount}")
        else:
            print("Please enter a valid amount to deposit.")

    def get_transaction_history(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return file.read()
        else:
            return "Transaction history is not available."

    def get_account_id(self):
        return self.account_id

    def _create_statement_file(self):
        with open(self.file_name, 'w') as file:
            file.write(f"Account Statement for {self.name} ({self.account_type}) - Account ID: {self.account_id}\n")
            file.write("Transaction History:\n")
            file.write(f"Initial Balance: ${self.balance}\n")

    def get_name(self):
        return self.name

    def get_account_type(self):
        return self.account_type

# Example usage:

account = BankAccount("Ahmed Osama", "Savings")

account.deposit(1000)
account.withdraw(500)
account.withdraw(600)  # Insufficient funds

print(account.get_balance())  # Balance
print(account.get_account_id())  # Account ID
print(account.get_name())  # Name
print(account.get_account_type())  # Account Type

print(account.get_transaction_history())  # Transaction History
