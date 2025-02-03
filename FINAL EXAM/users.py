import random
from datetime import datetime

class Bank:
    def __init__(self):
        self.users = []
        self.loan_status = True

class User:
    def __init__(self, name, email, address, account, bank):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account
        self.balance = 0
        self.loan_taken = 0
        self.loan_amount = 0
        self.account_num = random.randint(100, 1000)
        self.transaction_history = []
        self.bank = bank

    def deposit(self, amount):
        self.balance += amount
        transaction_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        self.transaction_history.append((transaction_time, f"You have Deposited {amount} Taka"))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.transaction_history.append((transaction_time, f"Withdraw {amount} Taka"))
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance
    
    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.bank.loan_status and self.loan_taken < 2:
            self.loan_amount += amount
            self.loan_taken += 1
            self.balance += amount  

    def transfer_money(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            transaction_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.transaction_history.append((transaction_time, f'Transferred {amount} Taka to {receiver.account_num}'))
            receiver.transaction_history.append((transaction_time, f"Received {amount} Taka from {self.account_num}"))
        else:
            print("Sorry you don't have enough money to transfer")

class Admin(User):
    def __init__(self, name, email, address, account, password, bank):
        super().__init__(name, email, address, account, bank)
        self.password = password

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type, self.bank)
        self.bank.users.append(user)
        print(f"Account created successfully! Your account number is {user.account_num}")

    def delete_account(self, account_num):
        for user in self.bank.users:
            if user.account_num == account_num:
                self.bank.users.remove(user)
                print(f"{account_num} user account deleted successfully.")
                return
        print("Account doesn't exist")

    def show_users(self):
        print("------All user accounts------")
        for user in self.bank.users:
            print(f"Account Number: {user.account_num}, Name: {user.name}, Email: {user.email}")

    def total_balance(self):
        Total_balance = sum(user.balance for user in self.bank.users)
        print("Total available balance:", Total_balance)

    def total_loan(self):
        total_loan = sum(user.loan_amount for user in self.bank.users)
        print(f"Total loan amount in the Bank: {total_loan} Taka")

    def off_loan(self):
        self.bank.loan_status = False
        print("Loan features status is now Off")

    def on_loan(self):
        self.bank.loan_status = True
        print("Loan features status is now On")

