from user import User
from admin import Admin

def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    account_type = input("Enter Account Type (Savings/Current) : ")
    customer = User(name, email, address, account_type)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            customer.deposit(amount)
        
        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            customer.withdraw(amount)
        
        elif choice == 3:
            print("Current Balance:", customer.check_balance())
        
        elif choice == 4:
            print("Transaction History:")
            for transaction in customer.view_transaction_history():
                print(transaction)
        
        elif choice == 5:
            amount = int(input("Enter loan amount: "))
            customer.take_loan(amount)
        
        elif choice == 6:
            recipient_name = input("Enter recipient name: ")
            recipient_account_number = int(input("Enter recipient account number: "))
            amount = int(input("Enter transfer amount: "))
            recipient = None
            for user in Admin.users:
                if user.name == recipient_name and user.account_number == recipient_account_number:
                    recipient = user
                    break
            if recipient:
                customer.transfer_to(recipient, amount)
            else:
                print("Recipient not found.")
        
        elif choice == 7:
            break
        else:
            print("Invalid Input")


def admin_menu():
    admin = Admin()

    while True:
        print(f"Welcome Admin!!")
        print("1. Create account")
        print("2. Delete account")
        print("3. All accounts")
        print("4. Total balance")
        print("5. Total loan amount")
        print("6. Toggle loan feature")
        print("7. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            name = input("Enter user name : ")
            email = input("Enter user email : ")
            address = input("Enter User Address : ")
            account_type = input("Enter user account type (savings/current) : ")
            user = User(name=name, email=email, address=address, account_type=account_type)
            admin.create_account(user)
        
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            admin.delete_account(account_number)
        
        elif choice == 3:
            admin.list_accounts()
        
        elif choice == 4:
            print("Total balance:", admin.total_balance())
        elif choice == 5:
            print("Total loan amount:", admin.total_loan_amount())
        
        elif choice == 6:
            status = input("Enter 'on' to enable loan feature or 'off' to disable: ")
            admin.toggle_loan_feature(status)
        
        elif choice == 7:
            break
        else:
            print("Invalid input")


while True:
    print("Welcome!!")
    print("1. USer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input!!")