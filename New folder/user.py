import random

class User:
    
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.account_number()
        self.transaction_history = []
        self.loan_taken = 0

    def account_number(self): 
        ac_number = random.randint(1, 10000)  
        return ac_number

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit amount: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew amount: {amount}")

    def check_balance(self):
        return self.balance

    def view_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.transaction_history.append(f"Loan taken amount: {amount}")
        else:
            print("You already taken loan")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Account number: {self.account_number}"
    
    
    def transfer_to(self, recipient, amount):
        if amount <= 0:
            print("You should send positive money!")
        if self.balance < amount:
            print("Insufficient balance!")
        self.withdraw(amount)
        recipient.deposit(amount)
        self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
        print("Transfer successful.")