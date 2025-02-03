from abc import ABC,abstractmethod
from datetime import datetime
from Bank import Bank
class Account:
    def __init__(self,name,email,address,account_type,password):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.password=password
        self.balance=0
        self.account_id=0
class User(Account):
    def __init__(self,name,email,address,account_type,password):
        super().__init__(name,email,address,account_type,password)
        self.transection_history=[]
        self.loans=0
        self.loan_time=0
        self.account_id=100+len(Bank.users)
        Bank.users.append(self)     
    def diposit(self,bank,amount):   
        if amount>0:
            self.balance+=amount
            bank.balance+=amount
            self.transection_history.append(f"{datetime.now()} deposit {amount}")
    def wihdraw(self,bank,amount):

        if self.balance>=amount and amount>0:
            if bank.bank_status==True:
                print(" the bank is bankrupt ")
                return
            self.balance-=amount
            bank.balance=amount
            self.transection_history.append(f"{datetime.now()} withdraw {amount}")
        else:
            print("Withdrawal amount exceeded")
    def check_balance(self):
        print(f"{self.name} your account Balance is {self.balance} Now !")
    def check_history(self):
        print("**********************************************\n")
        print("******************History*********************")
        print(f"***Date\t\tAmount***")
        for history in self.transection_history:
            print(history)
        print("\n**********************************************\n")
    def take_loan(self,bank,amount):
        if self.loan_time < 2 and bank.balance >= amount and bank.bank_status==False and amount>0 and bank.loan_status==True:
            self.loan_time+=1
            bank.balance-=amount
            self.loans+=amount
            print(f"You took loan successfully {amount} tk !")
        else:
            print("Sorry your request is rejected")
    def transfer_money(self,bank,account_id,amount):
        if self.balance>=amount:
            account=bank.find_account(account_id)
            if account:
                self.balance-=amount
                account.balance+=amount
                print(f"{amount} tk successfully tansfer {account_id}")
                self.transection_history.append(f"From {self.account_id} transfer {amount} to {account_id}")
            else:
                print("Account does not exist !")
        else:
            print("Sorry your request is cancelled !")
    def show_balance(self):
        print(f"{self.account_id} Your current balance is {self.balance}")

class Admin(Account):
    def __init__(self, name, email, address, account_type,password):
        super().__init__(name, email, address, account_type,password)
        Bank.admin.append(self)
    def add_money_to_bank(self,bank,money):
        if money>0:
            bank.add_money(money)
    def show_bank_balance(self,bank):
       bank.show_balance()
    def see_all_user_account_list(self,bank):
        bank.show_all_users()
    def delete_user(self,bank,id):
        bank.delete_user(id)
    def set_loan_status(self,bank,status):
        bank.loan_status(status)
    def show_total_loans_amount(self,bank):
        t=bank.total_loans_amount()
        print(f"The total loans taken by user are: {t} tk !")