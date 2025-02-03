from users import User, Admin, Bank

def client_interface(bank):
    while True:
        print("Welcome to the User Interface!")
        print("1. Create Account")
        print("2. Log In")
        print("3. Exit")

        choice = int(input("Please Enter Your Choice: "))

        if choice == 1:
            name = input("Please Enter Your Full Name: ")
            email = input("Enter your Email: ")
            address = input("Enter Your Current Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            new_user = User(name, email, address, account_type, bank)
            bank.users.append(new_user)  
            print(f"Account created successfully! Your account number is : {new_user.account_num}")

            client_logged_in(new_user, bank)

        elif choice == 2:
            account_num = int(input("Enter Your Account Number: "))
            existing_user = None
            for user in bank.users:
                if user.account_num == account_num:
                    existing_user = user
                    break

            if existing_user:
                print("Login Successful!")
                client_logged_in(existing_user, bank)
            else:
                print("Account not found. Please create an account.")

        elif choice == 3:
            break

        else:
            print("Please provide a valid input.")

def client_logged_in(client, bank):
    while True:
        print(f"Welcome {client.name}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Log Out")

        choice = int(input("Please Enter Your Choice: "))

        if choice == 1:
            amount = int(input("Enter your deposit amount: "))
            client.deposit(amount)

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            client.withdraw(amount)

        elif choice == 3:
            print(f"Your Current Balance is: {client.check_balance()}")

        elif choice == 4:
            print("-------Transaction History-------")
            for transaction in client.check_transaction_history():
                print(transaction)

        elif choice == 5:
            if bank.loan_status:
                amount = int(input("Enter amount: "))
                client.take_loan(amount)
            else:
                print("Loan feature is currently turned off.")

        elif choice == 6:
            receiver_name = input("Enter the receiver name: ")
            receiver_account_num = int(input("Enter account number: "))
            amount = int(input("Enter amount: "))
            receiver = None
            for user in bank.users:
                if user.name == receiver_name and user.account_num == receiver_account_num:
                    receiver = user
                    break
            if receiver:
                client.transfer_money(receiver, amount)
            else:
                print("Account does not exist")

        elif choice == 7:
            break

        else:
            print("Please provide valid input")


def admin_interface(bank):
    admin_password = "admin123"  
    name = "admin"
    email = "admin@gmail.com"
    address = "Dhaka"
    account_type = "admin"
    password = input("Enter Admin Password: ")
    admin = Admin(name, email, address, account_type, admin_password, bank)

    if admin.password == password:
        while True:
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. Show Users")
            print("4. Total Balance")
            print("5. Total Loan")
            print("6. Off Loan")
            print("7. On Loan")
            print("8. Log out")

            choice = int(input("Please Enter Your Choice: "))

            if choice == 1:
                user_name = input("Enter user's full name: ")
                user_email = input("Enter user's email: ")
                user_address = input("Enter user's address: ")
                user_account_type = input("Enter user's account type (Saving/Current): ")
                new_user = User(user_name, user_email, user_address, user_account_type, bank)
                bank.users.append(new_user)  
                print(f"{user_name}'s account created successfully! Account number is {new_user.account_num}")

            elif choice == 2:
                account_num = int(input("Enter account number to delete: "))
                for user in bank.users:
                    if user.account_num == account_num:
                        bank.users.remove(user)
                        print(f"Account number {account_num} deleted successfully.")
                        break
                else:
                    print("Account doesn't exist")

            elif choice == 3:
                print("------All user accounts------")
                for user in bank.users:
                    print(f"Account Number: {user.account_num}, Name: {user.name}, Email: {user.email}")

            elif choice == 4:
                total_balance = sum(user.balance for user in bank.users)
                print(f"Total Balance in the bank: {total_balance}")

            elif choice == 5:
                total_loan = sum(user.loan_amount for user in bank.users)
                print(f"Total Loan in the bank: {total_loan}")

            elif choice == 6:
                bank.loan_status = False
                print("Loan feature is now turned off")

            elif choice == 7:
                bank.loan_status = True
                print("Loan feature is now turned on")

            elif choice == 8:
                break

            else:
                print("Please provide valid input")
    else:
        print("Invalid! Please try again.")



def main():
    bank = Bank()
    while True:
        print("1. Client")
        print("2. Admin")
        print("3. Exit")

        choice = int(input("Please Enter Your Choice: "))

        if choice == 1:
            client_interface(bank)

        elif choice == 2:
            admin_interface(bank)

        elif choice == 3:
            break

        else:
            print("Please provide valid input")

main()
