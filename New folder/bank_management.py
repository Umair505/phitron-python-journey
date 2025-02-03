import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(10000, 99999)
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Withdrawal amount exceeded.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1

    def transfer_amount(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to account number {receiver.account_number}")
            receiver.transaction_history.append(f"Received ${amount} from account number {self.account_number}")
        else:
            print("Insufficient balance to transfer amount.")


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.bank.users[user.account_number] = user
        print("Account created successfully! Your account number is:", user.account_number)

    def delete_account(self, account_number):
        if account_number in self.bank.users:
            del self.bank.users[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist.")

    def see_all_accounts(self):
        print("All User Accounts:")
        for account_number, user in self.bank.users.items():
            print(f"Account Number: {account_number}, Name: {user.name}, Email: {user.email}")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.users.values())
        print("Total Available Balance in the Bank:", total_balance)

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.balance for user in self.bank.users.values() if user.loan_taken > 0)
        print("Total Loan Amount in the Bank:", total_loan_amount)

    def toggle_loan_feature(self):
        self.bank.loan_feature_enabled = not self.bank.loan_feature_enabled
        status = "enabled" if self.bank.loan_feature_enabled else "disabled"
        print(f"Loan feature is now {status}.")


class Bank:
    def __init__(self):
        self.users = {}
        self.loan_feature_enabled = True


bank = Bank()
admin = Admin(bank)

# Sample Usage
admin.create_account("John Doe", "john@example.com", "123 Main St", "Savings")
admin.create_account("Jane Smith", "jane@example.com", "456 Elm St", "Current")

user1 = bank.users[10000]
user1.deposit(500)
user1.withdraw(200)
print("User1 Balance:", user1.check_balance())

admin.see_all_accounts()
admin.check_total_balance()
admin.toggle_loan_feature()

user1.take_loan(1000)
user2 = bank.users[10001]
user1.transfer_amount(user2, 300)

print("User1 Transaction History:", user1.check_transaction_history())
print("User2 Transaction History:", user2.check_transaction_history())
