

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, user):
        self.users.append(user)
        print("Account created successfully.")

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("Account deleted successfully.")
        print("Account not found.")

    def all_accounts(self):
        for user in self.users:
            print(user)

    def total_balance(self):
        total = sum(user.balance for user in self.users)
        return total

    def total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.users)
        return total_loan

    def toggle_loan_feature(self, status):
        print("Loan feature is now", "on" if status else "off")