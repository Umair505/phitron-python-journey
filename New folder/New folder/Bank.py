class Bank:
    users=[]
    admin=[]
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.bank_status=False
        self.loans_status=True
    def add_money(self,money):
        if money>0:
            self.balance+=money
    @classmethod
    def find_account(cls,id):
        for account in cls.users:
            if account.account_id==id:
                return account
        return None
    @classmethod
    def show_all_users(self):
        print("**********************************\n")
        print("Name:\tBalance\tAccount_id")
        for user in self.users:
            print(f"{user.name}\t{user.balance}\t{user.account_id}")
        print("**********************************\n")
    @classmethod
    def  delete_user(self,id):
        user=self.find_account(id)
        if user:
            self.users.remove(user)
            print("the user is deleted")
        else:
            print("The user Not exist")
    def show_balance(self):
        print(f"The bank have {self.balance} tk ")
        
    @classmethod
    def total_loans_amount(self):
        total=0
        for user in self.users:
            total+=user.loans
        return total
    def loan_status(self,status):
        self.loans_status=status
    @classmethod
    def valid_user_or_not(self,email,password):
        for user in self.users:
            if user.email==email and user.password==password:
                return user
        return None
    @classmethod
    def valid_admin_or_not(self,email,password):
        if len(self.admin)>=1:
            if self.admin[0].email==email and self.admin[0].password==password:
                return self.admin[0]
        else:
            return None
    
    
        
        




